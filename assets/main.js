// ============================================================
// Youna Global – Main JS
// ============================================================

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM Content Loaded - Initializing navigation');
  
  // Mobile nav toggle
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  
  console.log('navToggle element:', navToggle);
  console.log('navLinks element:', navLinks);
  
  if (navToggle && navLinks) {
    console.log('✓ Navigation elements found - Attaching event listener');
    console.log('Initial navLinks computed style:', {
      display: window.getComputedStyle(navLinks).display,
      visibility: window.getComputedStyle(navLinks).visibility,
      opacity: window.getComputedStyle(navLinks).opacity
    });
    
    navToggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      
      console.log('=== MENU BUTTON CLICKED ===');
      console.log('Before toggle - className:', navLinks.className);
      console.log('Before toggle - has "open" class:', navLinks.classList.contains('open'));
      
      navLinks.classList.toggle('open');
      
      console.log('After toggle - className:', navLinks.className);
      console.log('After toggle - has "open" class:', navLinks.classList.contains('open'));
      
      const computedStyle = window.getComputedStyle(navLinks);
      console.log('After toggle - computed style:', {
        display: computedStyle.display,
        visibility: computedStyle.visibility,
        opacity: computedStyle.opacity,
        position: computedStyle.position,
        'z-index': computedStyle.zIndex
      });
      
      console.log('Menu state:', navLinks.classList.contains('open') ? '✓ OPEN' : '✗ CLOSED');
    });
    
    // Close on link click
    const navLinkItems = navLinks.querySelectorAll('a');
    console.log('Found nav links:', navLinkItems.length);
    
    navLinkItems.forEach((link, index) => {
      link.addEventListener('click', () => {
        console.log(`Menu link ${index} clicked - closing menu`);
        navLinks.classList.remove('open');
      });
    });
  } else {
    console.error('✗ Navigation elements NOT found!');
    console.error('navToggle:', navToggle);
    console.error('navLinks:', navLinks);
  }
});

// Contact form handler - FormSubmit integration
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function (e) {
    // Allow form to submit normally to FormSubmit API
    // FormSubmit will handle data storage and email notification
    // User will be redirected to success page via _next parameter
  });
}

// Check for success parameter and show modal
document.addEventListener('DOMContentLoaded', function() {
  if (window.location.search.includes('success=true')) {
    const successModal = document.getElementById('successModal');
    if (successModal) {
      successModal.style.display = 'flex';
      // Clear the URL parameter
      window.history.replaceState({}, document.title, window.location.pathname);
      // Auto-hide modal after 5 seconds
      setTimeout(() => {
        successModal.style.display = 'none';
      }, 5000);
    }
  }
});

// Trust Carousel - Infinite scroll animation
document.addEventListener('DOMContentLoaded', function() {
  const trustCarousel = document.querySelector('.trust-carousel');
  if (!trustCarousel) return;

  const trustTrack = trustCarousel.querySelector('.trust-track');
  if (!trustTrack) return;
  
  // Pause on hover - target the carousel, not the track
  trustCarousel.addEventListener('mouseenter', function() {
    trustTrack.style.animationPlayState = 'paused';
  });
  
  trustCarousel.addEventListener('mouseleave', function() {
    trustTrack.style.animationPlayState = 'running';
  });
  
  // Pause on touch
  trustCarousel.addEventListener('touchstart', function() {
    trustTrack.style.animationPlayState = 'paused';
  });
  
  trustCarousel.addEventListener('touchend', function() {
    trustTrack.style.animationPlayState = 'running';
  });
  
  // Responsive animation speed adjustment
  function adjustAnimationSpeed() {
    const width = window.innerWidth;
    let speed = '30s';
    
    if (width <= 640) {
      speed = '20s';
    } else if (width <= 900) {
      speed = '25s';
    }
    
    trustTrack.style.animationDuration = speed;
  }
  
  adjustAnimationSpeed();
  window.addEventListener('resize', adjustAnimationSpeed);
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Navbar scroll effect
const navbar = document.querySelector('.navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.style.boxShadow = window.scrollY > 10 ? '0 2px 20px rgba(0,0,0,0.08)' : 'none';
  });
}

// Animate elements on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.service-card, .why-card, .testimonial-card, .step, .value-card, .country-item').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});
