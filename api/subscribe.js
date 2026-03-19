// api/subscribe.js
// Vercel Serverless Function for Mailchimp Integration
// Auto-detects or creates Audience - no List ID needed!

module.exports = async function handler(req, res) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email } = req.body;

  // Validate inputs
  if (!email) {
    return res.status(400).json({ error: 'Missing email address' });
  }

  // Validate email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return res.status(400).json({ error: 'Invalid email address' });
  }

  // Mailchimp API Key (from environment variable or fallback)
  const apiKey = process.env.MAILCHIMP_API_KEY || '12674870ec448ff583c21398701e8d83-us10';
  const dataCenter = apiKey.split('-')[1];

  try {
    // Step 1: Try to find existing audience
    let listId = await findOrCreateAudience(apiKey, dataCenter);

    // Step 2: Add subscriber to the audience
    const mailchimpUrl = `https://${dataCenter}.api.mailchimp.com/3.0/lists/${listId}/members`;

    const subscriberData = {
      email_address: email,
      status: 'pending' // Double opt-in
    };

    const response = await fetch(mailchimpUrl, {
      method: 'POST',
      headers: {
        'Authorization': 'Basic ' + Buffer.from(`anystring:${apiKey}`).toString('base64'),
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(subscriberData)
    });

    const data = await response.json();

    // Handle responses
    if (response.ok) {
      return res.status(200).json({ 
        success: true, 
        message: 'Subscription successful. Please check your email to confirm.' 
      });
    } else if (data.title === 'Member Exists') {
      return res.status(200).json({ 
        success: true, 
        message: 'Email already subscribed',
        existing: true 
      });
    } else {
      return res.status(400).json({ 
        success: false, 
        message: data.detail || 'Subscription failed' 
      });
    }

  } catch (error) {
    console.error('Error:', error);
    return res.status(500).json({ 
      success: false, 
      message: 'Server error: ' + error.message 
    });
  }
};

// Helper function: Find or Create Audience
async function findOrCreateAudience(apiKey, dataCenter) {
  // First, try to get all lists
  const listsUrl = `https://${dataCenter}.api.mailchimp.com/3.0/lists`;
  
  const response = await fetch(listsUrl, {
    method: 'GET',
    headers: {
      'Authorization': 'Basic ' + Buffer.from(`anystring:${apiKey}`).toString('base64'),
      'Content-Type': 'application/json'
    }
  });

  const data = await response.json();

  // If we have lists, return the first one
  if (data.lists && data.lists.length > 0) {
    return data.lists[0].id;
  }

  // No lists exist, create one
  const createUrl = `https://${dataCenter}.api.mailchimp.com/3.0/lists`;
  
  const newListData = {
    name: 'Youna Global Newsletter',
    contact: {
      company: 'Youna Global',
      address1: 'China',
      city: 'Shanghai',
      zip: '200000',
      country: 'CN'
    },
    permission_reminder: 'You subscribed to our newsletter',
    campaign_defaults: {
      from_name: 'Youna Global',
      from_email: 'longxin3639@gmail.com',
      subject: 'Welcome to Youna Global Newsletter',
      language: 'en'
    },
    email_type_option: true
  };

  const createResponse = await fetch(createUrl, {
    method: 'POST',
    headers: {
      'Authorization': 'Basic ' + Buffer.from(`anystring:${apiKey}`).toString('base64'),
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(newListData)
  });

  const createData = await createResponse.json();

  if (createResponse.ok && createData.id) {
    return createData.id;
  } else {
    throw new Error('Failed to create audience: ' + (createData.detail || 'Unknown error'));
  }
}
