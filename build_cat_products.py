# -*- coding: utf-8 -*-
import os, json

OUT = r"D:\GitHub\youna-global\products"
IMG = "../assets/images/Products/Pet%20Supplies/CAT"
BLOG = "../blog/blog-designer-cat-clothes-collection.html"
BLOG_IMG = "../assets/images/blog/2026.7.10/cat-fashion-duo-gothic-victorian.webp"
PHONE = "8619898484442"

# shared section texts
WHO = [
    ("Pet Boutiques", "fas fa-store", "Stock a cohesive original cat-fashion line with pieces your competitors cannot source from open commodity platforms. High-margin, photo-ready, and exclusive to your catalog."),
    ("Amazon & Shopify Sellers", "fas fa-shopping-cart", "Premium cat outfits with strong listing photos and a clear 'original design' story. Small, light, and easy to ship via FBA - ideal for differentiated SKUs."),
    ("Pet Influencers & Creators", "fas fa-camera", "Outfits built for the camera: structured hats, tactile fabrics, and coordinated accessories that read instantly in thumbnails and Reels. Great for sponsored content."),
    ("Gift & Specialty Shops", "fas fa-gift", "Birthday, holiday, and 'just because' purchases for doting cat parents. The drama and detail make an unforgettable present - and a high average order value."),
    ("Private Label Brands", "fas fa-tags", "Add your logo tag, custom colorway, and branded hangtag. We help you build a complete cat-apparel line with consistent quality and a real design point of view."),
    ("Photo Studios & Event Stylists", "fas fa-images", "Wedding, holiday, and portrait sessions need a 'wow' cat look. Our gowns and gothic pieces deliver editorial results with minimal styling effort."),
]

PACKAGE_NOTE = "Retail prices are estimates based on comparable premium cat outfits on Amazon US, Chewy, and Etsy. Cat apparel is a high-margin pet category - small, light, and cheap to ship."

products = [
{
 "slug":"cat-silver-quilted-vest","h1":"Silver Quilted Vest Set","unit":"/ set",
 "price_low":"14.00","price_high":"18.00",
 "main":"silver-quilted-vest-cat.webp","t1":"white-victorian-gown-cat.webp","t2":"black-gothic-dress-cat.webp",
 "title":"Silver Quilted Vest Set for Cats | Original Designer Cat Clothing | Youna Global",
 "meta":"Wholesale original designer silver quilted vest set for cats - quilted vest, white shirt & wide-brim hat. MOQ 200 pcs from $14. Factory-direct original cat fashion from Youna Global.",
 "short":"A tailored silver quilted vest paired with a crisp white shirt and a sculpted wide-brim hat - a couture daywear look engineered for the discerning cat. An original Youna design, built for boutique shelves and camera-ready content alike.",
 "specs":[
   ["Material","Quilted poly-cotton shell with light padding; inner shirt in soft cotton poplin; hat in molded felt"],
   ["Size Range","XS (2-3 kg) - S (3-4 kg) - M (4-5 kg) - L (5-6.5 kg)"],
   ["Colors / Variants","Silver + White (as shown); custom colorways available on MOQ"],
   ["MOQ","200 pcs per colorway"],
   ["Lead Time","12-20 days after sample approval; sample in 5-7 days"],
   ["Customization","Woven logo tag, custom color, custom hangtag"],
   ["Packaging","Individual OPP bag with branded hangtag; master carton for wholesale"],
   ["Care","Hand wash cold or gentle cycle only; reshape and line dry; do not bleach"],
 ],
 "features":[
   ["Original Atelier Silhouette","Our in-house design team developed the quilted vest and wide-brim hat as a single coordinated set, not a cobbled-together costume. The proportions are tuned to the feline frame so the look reads as fashion, not dress-up."],
   ["Lightweight Quilted Warmth","A thin poly-cotton padding gives the vest its structured, luxe hand-feel without weighing the cat down. Your customers get a premium garment their pets will actually tolerate wearing."],
   ["Photo-Ready in Seconds","The molded wide-brim hat holds its shape and frames the face for instant social content. It is ideal for in-store displays and styled shoots where a clean, metallic look sells."],
   ["Comfort-First Inner Shirt","The white shirt uses a soft cotton poplin with a forgiving neck opening and a quiet back closure. No scratchy seams against the fur - just a clean base layer under the vest."],
   ["Wholesale-Ready Construction","Every set is finished to consistent B2B tolerances: matched trims, reinforced stitch lines, and a uniform size run. Order 200 and receive a shelf-ready, repeatable product."],
 ],
 "faqs":[
   ["How do I choose the right size for a cat?","Measure the cat's chest girth and weight, then match to our XS-L run (2-6.5 kg). When between sizes, size up for comfort and easier dressing."],
   ["Can I add my own brand logo?","Yes. On the 200-pc MOQ we weave or print your logo onto a sewn-in tag and can supply custom hangtags. Send your artwork with the order."],
   ["What is the lead time including a sample?","Sample ships in 5-7 days; bulk production runs 12-20 days after you approve the sample. Plan roughly 3-4 weeks from artwork sign-off to shipment."],
   ["How should the set be washed?","Hand wash cold or use a gentle machine cycle in a laundry bag. Reshape the hat and vest, then line dry flat - avoid bleach and tumble heat."],
   ["Is the hat secure on the cat's head?","The hat sits as a styled prop and is not strapped; most cats tolerate it briefly for photos. We recommend it for supervised wear and content shoots rather than all-day use."],
 ],
},
{
 "slug":"cat-white-victorian-gown","h1":"White Victorian Gown","unit":"/ pc",
 "price_low":"16.00","price_high":"22.00",
 "main":"white-victorian-gown-cat.webp","t1":"white-victorian-collar-cat.webp","t2":"silver-quilted-vest-cat.webp",
 "title":"White Victorian Gown for Cats | Original Designer Cat Clothing | Youna Global",
 "meta":"Wholesale original white Victorian gown for cats with lace hood & crystal buttons. Floor-length luxury cat dress. MOQ 200 pcs from $16. Factory-direct from Youna Global.",
 "short":"A floor-sweeping white Victorian gown with a lace hood and crystal-button front - a heritage-inspired statement piece from our original cat atelier. Designed for the luxury pet market where drama and detail sell.",
 "specs":[
   ["Material","Satin-finish polyester bodice with lace hood trim; resin crystal buttons; soft lining"],
   ["Size Range","XS (2-3 kg) - S (3-4 kg) - M (4-5 kg) - L (5-6.5 kg)"],
   ["Colors / Variants","Ivory White (as shown); custom dye available on MOQ"],
   ["MOQ","200 pcs per colorway"],
   ["Lead Time","12-20 days after sample approval; sample in 5-7 days"],
   ["Customization","Logo tag, custom color, custom button finish"],
   ["Packaging","Individual OPP bag with hangtag; protective carton for wholesale"],
   ["Care","Hand wash cold, line dry; steam lightly to refresh lace; do not wring"],
 ],
 "features":[
   ["Heritage Victorian Line","The gown's high neckline, laced hood, and buttoned front are drawn from 19th-century couture references re-proportioned for cats. It is a genuine design piece, not a themed onesie."],
   ["Hand-Set Crystal Buttons","Each resin crystal button is stitched for a secure, glinting closure down the front. The detail photographs beautifully and signals luxury at the shelf and in listings."],
   ["Floor-Length Drama","The long skirt drapes to the floor for portrait and event styling. Retailers use it for weddings, holidays, and premium photo packages where a white gown earns its keep."],
   ["Lined for Comfort","A soft inner lining keeps the satin off the coat and a hidden back closure makes dressing calm and quick. The hood is decorative and sits loose around the head."],
   ["Boutique Margin Builder","As an original Youna design, the gown is exclusive to your catalog - no mass-market duplicate on open commodity platforms. That exclusivity supports stronger retail pricing for your store or brand."],
 ],
 "faqs":[
   ["What cat sizes does the gown fit?","XS through L covers 2-6.5 kg. Because the gown is long, prioritize chest girth and back length; size up if your cat is between bands."],
   ["Is the lace hood comfortable for the cat?","The hood is an open, decorative frame that rests around the head without tightening. It is best for short, supervised wear and photography."],
   ["Can the gown be custom-colored or branded?","Yes - on the 200-pc MOQ we offer custom dye and a sewn logo tag. Discuss your palette and artwork with our team at order time."],
   ["How long is production including a sample?","Sample in 5-7 days, bulk in 12-20 days after approval. Most orders ship within a month of artwork confirmation."],
   ["How do I care for the lace and buttons?","Hand wash cold and line dry; reshape the lace while damp and steam on low if needed. Keep crystals away from harsh detergents."],
 ],
},
{
 "slug":"cat-grey-velvet-waistcoat","h1":"Grey Velvet Waistcoat","unit":"/ pc",
 "price_low":"12.00","price_high":"16.00",
 "main":"grey-velvet-waistcoat-cat.webp","t1":"black-gothic-dress-cat.webp","t2":"floral-garden-dress-cat.webp",
 "title":"Grey Velvet Waistcoat for Cats | Original Designer Cat Clothing | Youna Global",
 "meta":"Wholesale original grey velvet waistcoat for cats with faux-pearl necklace, bow & beret. Photo-ready gentleman cat outfit. MOQ 200 pcs from $12. Factory-direct from Youna Global.",
 "short":"A dark grey velvet waistcoat anchored by a faux-pearl necklace, an oversized bow, and a Parisian beret - our most photogenic gentleman look. An original Youna design that turns a calm cat into a cover shot.",
 "specs":[
   ["Material","Polyester velvet waistcoat; faux-pearl strand; grosgrain bow; molded beret"],
   ["Size Range","XS (2-3 kg) - S (3-4 kg) - M (4-5 kg) - L (5-6.5 kg)"],
   ["Colors / Variants","Dark Grey (as shown); custom velvet color on MOQ"],
   ["MOQ","200 pcs per colorway"],
   ["Lead Time","12-20 days after sample approval; sample in 5-7 days"],
   ["Customization","Logo tag, custom color, custom bow"],
   ["Packaging","Individual OPP bag with hangtag; master carton for wholesale"],
   ["Care","Spot clean or hand wash cold; lay flat to dry; do not tumble dry"],
 ],
 "features":[
   ["Rich Velvet Hand","The waistcoat uses a deep-pile polyester velvet that catches light like wool, giving a luxe, tactile read on camera. It is the kind of fabric that makes a listing feel expensive at a glance."],
   ["Styled Pearl & Bow","A faux-pearl necklace and an oversized grosgrain bow come pre-styled so the set looks finished out of the bag. Buyers get a shoot-ready product with zero assembly for the end customer."],
   ["Beret That Holds Shape","The molded beret keeps its tilt for consistent, charming photos. Like all our hats, it is a styled prop for supervised wear rather than a strapped accessory."],
   ["Calm, Comfortable Fit","The waistcoat closes at the back with quiet fastening and leaves the legs free, so most cats stand and move naturally. Velvet breathes well for short indoor sessions."],
   ["Exclusive Atelier SKU","Original to Youna's cat line, the waistcoat has no commodity-market twin. That protects your margin and gives your boutique or brand a distinctive hero piece."],
 ],
 "faqs":[
   ["Which cats fit the waistcoat?","XS-L suits 2-6.5 kg. Measure chest girth; the back closure gives a little adjustment, but size up if your cat is broad-chested."],
   ["Is the pearl necklace safe if a cat chews it?","The strand is decorative and not chew-proof. We classify the whole set as supervised, photo-and-event wear, not unattended daily use."],
   ["What customization is possible at MOQ?","At 200 pcs we add your logo tag, offer custom velvet colors, and can swap the bow style or color to match your brand."],
   ["How fast can I get stock?","Sample in 5-7 days, bulk in 12-20 days post-approval. Confirm artwork early to keep the full cycle near four weeks."],
   ["Can the velvet be machine washed?","Spot clean preferred; if needed, hand wash cold and lay flat to dry. Avoid tumble drying, which flattens the pile."],
 ],
},
{
 "slug":"cat-floral-garden-dress","h1":"Floral Garden Dress","unit":"/ pc",
 "price_low":"13.00","price_high":"17.00",
 "main":"floral-garden-dress-cat.webp","t1":"white-victorian-collar-cat.webp","t2":"grey-velvet-waistcoat-cat.webp",
 "title":"Floral Garden Dress for Cats | Original Designer Cat Clothing | Youna Global",
 "meta":"Wholesale original black-and-white floral garden dress for cats with sunhat. Fresh daytime cat outfit. MOQ 200 pcs from $13. Factory-direct original design from Youna Global.",
 "short":"A black-and-white floral dress crowned by a wide sunhat, composed for the garden and the feed alike - a fresh, feminine original from Youna's cat atelier. A versatile daytime SKU that pairs storytelling with strong shelf appeal.",
 "specs":[
   ["Material","Floral-print poly-cotton dress; straw-style sunhat; soft lining"],
   ["Size Range","XS (2-3 kg) - S (3-4 kg) - M (4-5 kg) - L (5-6.5 kg)"],
   ["Colors / Variants","Black/White Floral (as shown); custom print on MOQ"],
   ["MOQ","200 pcs per colorway"],
   ["Lead Time","12-20 days after sample approval; sample in 5-7 days"],
   ["Customization","Logo tag, custom print, custom hat trim"],
   ["Packaging","Individual OPP bag with hangtag; master carton for wholesale"],
   ["Care","Hand wash cold, line dry; iron lining on low; do not bleach"],
 ],
 "features":[
   ["Garden-Scene Original","The black-and-white floral motif and wide sunhat were composed together for an outdoor, editorial feel. It is a complete look, designed to read instantly as garden party in any listing."],
   ["Breathable Day Dress","The poly-cotton print is light and airy for warmer indoor or event wear. A soft lining and simple back closure keep dressing quick and the cat comfortable."],
   ["Hat That Frames the Face","The sunhat's brim shades and frames the face for charming, high-contrast photos. As with our other hats, it is a styled prop best used for supervised wear."],
   ["Print Consistency for Resellers","We hold the floral artwork to tight B2B tolerances so every batch matches. Your customers receive the same dress they saw online - protecting your reviews."],
   ["Story-Driven Merchandising","The garden narrative gives boutiques a built-in content angle: seasonal displays, spring promotions, and pet-influencer shoots. Exclusive to Youna, it stays off commodity marketplaces."],
 ],
 "faqs":[
   ["What sizes are available?","XS through L for cats 2-6.5 kg. Match chest girth and weight; size up between bands for an easier fit."],
   ["Is the floral print exclusive?","The artwork is an original Youna design and not listed on open commodity platforms, so your store keeps a differentiated SKU at the 200-pc MOQ."],
   ["Can I request a custom print or hat trim?","Yes. On MOQ we can run a custom floral or solid print and adjust the hat trim to your brand palette. Share references at order time."],
   ["What is the production timeline?","Sample in 5-7 days; bulk in 12-20 days after sample sign-off. Budget about three to four weeks from artwork approval to shipment."],
   ["How should the dress and hat be cleaned?","Hand wash cold and line dry; the hat keeps its shape better if wiped rather than submerged. Avoid bleach to protect the print."],
 ],
},
{
 "slug":"cat-black-gothic-dress","h1":"Black Gothic Dress","unit":"/ pc",
 "price_low":"15.00","price_high":"19.00",
 "main":"black-gothic-dress-cat.webp","t1":"white-victorian-gown-cat.webp","t2":"grey-velvet-waistcoat-cat.webp",
 "title":"Black Gothic Dress for Cats | Original Designer Cat Clothing | Youna Global",
 "meta":"Wholesale original black sheer gothic dress for cats with lace hat & pink bow. Editorial alternative cat outfit. MOQ 200 pcs from $15. Factory-direct from Youna Global.",
 "short":"A black sheer gothic dress with a lace hat and a single pink-bow accent - a moody, editorial original from Youna's cat atelier. Built for the alternative-leaning pet market where a strong point of view drives the sale.",
 "specs":[
   ["Material","Sheer mesh polyester overlay with solid lining; lace hat; grosgrain pink bow"],
   ["Size Range","XS (2-3 kg) - S (3-4 kg) - M (4-5 kg) - L (5-6.5 kg)"],
   ["Colors / Variants","Black + Pink Bow (as shown); custom bow/trim on MOQ"],
   ["MOQ","200 pcs per colorway"],
   ["Lead Time","12-20 days after sample approval; sample in 5-7 days"],
   ["Customization","Logo tag, custom bow color, custom trim"],
   ["Packaging","Individual OPP bag with hangtag; master carton for wholesale"],
   ["Care","Hand wash cold, delicate; line dry; do not wring the mesh"],
 ],
 "features":[
   ["Sheer Gothic Layer","The dress pairs a solid lining with a sheer mesh overlay for a layered, shadowed look that photographs with depth. It is a deliberate fashion statement, not a novelty costume."],
   ["Lace Hat & Pink Accent","A lace-trim hat and one crisp pink bow create the collection's signature contrast - dark with a single soft note. The combo is instantly recognizable in thumbnails and feeds."],
   ["Editorial Photo Potential","The sheer fabric and lace read as high-fashion on camera, giving resellers premium content with minimal styling. Ideal for alternative boutiques, photo studios, and themed seasonal drops."],
   ["Lined for Wearability","Under the mesh, a soft lining keeps the dress from sticking to fur and a back closure makes dressing calm. Legs stay free so the cat moves naturally during short sessions."],
   ["Differentiated Subculture SKU","As an original Youna design, the gothic dress targets a niche with little commodity competition. That focus supports higher retail pricing and loyal, repeat buyers."],
 ],
 "faqs":[
   ["What cat sizes does the gothic dress cover?","XS-L for 2-6.5 kg. Check chest girth and back length; the sheer overlay has some give, but size up between bands."],
   ["Is the sheer mesh fragile?","The mesh is a delicate fashion fabric, so we recommend hand washing and supervised wear. It is styled for events and photos rather than rough daily use."],
   ["Can I change the bow or hat trim color?","Yes - at the 200-pc MOQ we can recolor the bow and adjust trims to your brand. The classic black-plus-pink is also available as shown."],
   ["How long until I receive stock?","Sample in 5-7 days, bulk in 12-20 days after approval. Most orders land within roughly a month of artwork confirmation."],
   ["How do I wash the mesh and lace?","Hand wash cold on delicate, do not wring, and line dry away from heat. Store flat to keep the lace hat from creasing."],
 ],
},
{
 "slug":"cat-white-victorian-collar-dress","h1":"White Victorian Collar Dress","unit":"/ pc",
 "price_low":"15.00","price_high":"20.00",
 "main":"white-victorian-collar-cat.webp","t1":"floral-garden-dress-cat.webp","t2":"white-victorian-gown-cat.webp",
 "title":"White Victorian Collar Dress for Cats | Original Designer Cat Clothing | Youna Global",
 "meta":"Wholesale original white Victorian collar dress for cats with gold buttons & matching leash. Walk-ready luxury cat outfit. MOQ 200 pcs from $15. Factory-direct from Youna Global.",
 "short":"A white Victorian dress defined by a gold-button high collar and a matching leash - a refined, walk-ready original from Youna's cat atelier. The only look in the collection engineered for both the lens and the leash.",
 "specs":[
   ["Material","Satin-finish polyester dress; metal-look gold buttons; nylon matching leash"],
   ["Size Range","XS (2-3 kg) - S (3-4 kg) - M (4-5 kg) - L (5-6.5 kg)"],
   ["Colors / Variants","White + Gold (as shown); custom color/leash on MOQ"],
   ["MOQ","200 pcs per colorway"],
   ["Lead Time","12-20 days after sample approval; sample in 5-7 days"],
   ["Customization","Logo tag, custom color, custom leash branding"],
   ["Packaging","Individual OPP bag with hangtag; master carton for wholesale"],
   ["Care","Hand wash cold, line dry; wipe leash with damp cloth; do not tumble dry"],
 ],
 "features":[
   ["Signature Gold Collar","The high Victorian collar closes with metal-look gold buttons for a jewelry-like finish. It is the dress's hero detail - instantly premium in photos and on the shelf."],
   ["Matching Leash Included","Unlike our other sets, this dress ships with a coordinated leash for true walk-ready styling. Resellers can merchandise it as an outfit plus accessory, lifting average order value."],
   ["Victorian Craft Lines","Pintuck-style seams and a satin finish echo heritage tailoring, re-cut for the feline form. The result is a design piece that reads as couture, not a party onesie."],
   ["Comfortable for Short Walks","A soft lining and back closure keep the dress calm to wear; the leash attaches to your cat's own harness worn underneath. Best for supervised outings and content, not all-day wear."],
   ["Complete Outfit SKU","As an original Youna design with an included accessory, the collar dress is a self-contained hero product. Exclusive to your catalog, it strengthens both margin and brand story."],
 ],
 "faqs":[
   ["What sizes fit this dress?","XS through L for cats 2-6.5 kg. Prioritize chest girth; the collar has light adjustability but size up if between bands."],
   ["How does the leash work with the dress?","The leash is a styled match to the outfit and clips to your cat's separate harness worn underneath. We do not recommend it as the primary restraint for strong pullers."],
   ["Can the collar buttons or leash be branded?","At the 200-pc MOQ we add your logo tag and can brand or recolor the leash to match your line. Gold buttons are fixed as shown unless arranged otherwise."],
   ["What is the lead time with a sample?","Sample in 5-7 days; bulk in 12-20 days after approval. Plan roughly three to four weeks from artwork sign-off to shipment."],
   ["How do I care for the dress and leash?","Hand wash the dress cold and line dry; wipe the nylon leash with a damp cloth. Avoid tumble drying, which can dull the satin."],
 ],
},
]

NAV = '''<header class="navbar">
  <div class="container nav-inner">
    <a href="../index.html" class="logo">
      <img src="../assets/LOGO2.png" alt="Youna Global" class="logo-img" />
      <span class="logo-text">Youna <span class="logo-accent">Global</span></span>
    </a>
    <nav class="nav-links" id="navLinks">
      <a href="../index.html">Home</a>
      <a href="../services.html">Services</a>
      <a href="../products/consumer-electronics.html" class="active">Products</a>
      <a href="../about.html">About</a>
      <a href="../blog.html">Blog</a>
      <a href="../faq.html">FAQ</a>
      <a href="../contact.html">Contact</a>
    </nav>
    <a href="../contact.html" class="btn btn-primary nav-cta">Get Free Quote</a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>'''

FOOTER = '''<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-brand">
      <div class="logo"><img src="../assets/LOGO2.png" alt="Youna Global" class="logo-img" /><span class="logo-text">Youna <span class="logo-accent">Global</span></span></div>
      <p>Youna (Zhongshan) Commerce &amp; Trade Co., Ltd.<br />Professional China Sourcing Agent</p>
      <div class="footer-contacts">
        <a href="https://wa.me/8619898484442" target="_blank" style="display:flex;align-items:center;gap:6px;"><img src="../assets/WhatsApp%20LOGO.png" alt="WhatsApp" width="16" height="16" style="display:block;flex-shrink:0;"> WhatsApp: +86 198 9848 4442</a>
        <a href="mailto:longxin3639@gmail.com">longxin3639@gmail.com</a>
      </div>
      <div class="footer-social">
        <a href="https://www.youtube.com/@Karsa-2016" target="_blank" title="YouTube"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a>
        <a href="https://www.facebook.com/SourcingAgentKarsa/" target="_blank" title="Facebook"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
        <a href="https://www.instagram.com/karsa_sourcingagentchina/" target="_blank" title="Instagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 2.163c3.204 0 3.584.012 4.85.072 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
        <a href="https://www.tiktok.com/@karsachinasource" target="_blank" title="TikTok"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.27 6.27 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V8.69a8.27 8.27 0 004.84 1.55V6.79a4.85 4.85 0 01-1.07-.1z"/></svg></a>
      </div>
    </div>
    <div class="footer-links">
      <h4>Services</h4>
      <a href="../services.html#sourcing">Supplier Sourcing</a>
      <a href="../services.html#negotiation">Price Negotiation</a>
      <a href="../services.html#qc">Quality Control</a>
      <a href="../services.html#shipping">Shipping Agent</a>
      <a href="../services.html#branding">Custom Branding</a>
      <a href="../services.html#warehouse">Warehouse Storage</a>
    </div>
    <div class="footer-links">
      <h4>Products</h4>
      <a href="consumer-electronics.html">Consumer Electronics</a>
      <a href="apparel-accessories.html">Apparel &amp; Accessories</a>
      <a href="pet-supplies.html">Pet Supplies</a>
      <a href="automotive-supplies-tools.html">Automotive &amp; Tools</a>
      <a href="tiktok-trending.html">TikTok Trending</a>
      <a href="custom-oem-private-label.html">Custom OEM</a>
    </div>
    <div class="footer-links">
      <h4>Company</h4>
      <a href="../about.html">About Us</a>
      <a href="../blog.html">Blog</a>
      <a href="../faq.html">FAQ</a>
      <a href="../contact.html">Contact</a>
      <p style="color:#aaa;font-size:0.85rem;line-height:1.8;margin-top:12px;">
        No.9 Shangyuan Avenue,<br />
        Yuantang Road, Dongcheng<br />
        Subdistrict, Sihui City,<br />
        Zhaoqing, Guangdong, China
      </p>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 Youna (Zhongshan) Commerce &amp; Trade Co., Ltd. All rights reserved.</p>
  </div>
</footer>'''

def img(path): return IMG + "/" + path

for p in products:
    specs_html = "".join('<tr><th>{}</th><td>{}</td></tr>'.format(k,v) for k,v in p["specs"])
    feats = list(p["features"]) + [["Sized for the Feline Frame","Our XS-L run is mapped to cat weight (2-6.5 kg), not dog or human sizing, so the fit is right the first time and returns stay low."]]
    feats_html = "".join('<div class="pdp-feature"><div class="pdp-feature-icon"><i class="fas fa-gem"></i></div><h3>{}</h3><p>{}</p></div>'.format(t,d) for t,d in feats)
    faqs_html = "".join('<div class="pdp-faq-item"><h4>{}</h4><p>{}</p></div>'.format(q,a) for q,a in p["faqs"])
    who_html = "".join('<div class="pdp-feature"><div class="pdp-feature-icon"><i class="{}"></i></div><h3>{}</h3><p>{}</p></div>'.format(ic,t,d) for t,ic,d in WHO)
    wa = "https://wa.me/{}?text=Hi%20Karsa%2C%20I%27m%20interested%20in%20the%20{}%20cat%20outfit.%20Please%20send%20me%20a%20quote.".format(PHONE, p["h1"].replace(" ","%20"))

    # related: other 5 products + collection card
    others = [x for x in products if x["slug"] != p["slug"]]
    rel = ""
    for o in others:
        rel += '''      <a href="{slug}.html" class="catalog-card">
        <img src="{img}" alt="{h1}" class="catalog-card-img" loading="lazy" />
        <div class="catalog-card-body"><h3>{h1}</h3><div class="catalog-card-price">${lo} - ${hi} <span class="unit">{unit}</span></div><div class="catalog-card-moq">MOQ: 200 pcs</div></div>
      </a>
'''.format(slug=o["slug"], img=img(o["main"]), h1=o["h1"], lo=o["price_low"], hi=o["price_high"], unit=o["unit"])
    rel += '''      <a href="{blog}" class="catalog-card" style="border:2px solid var(--primary);">
        <img src="{bimg}" alt="Youna designer cat clothes collection" class="catalog-card-img" loading="lazy" />
        <div class="catalog-card-body"><h3>View the Full Collection</h3><div class="catalog-card-meta"><span><i class="fas fa-layer-group"></i> 6 original looks</span></div><div class="catalog-card-cta">Read the guide</div></div>
      </a>
'''.format(blog=BLOG, bimg=BLOG_IMG)

    ld = {
      "@context":"https://schema.org",
      "@type":"Product",
      "name": p["h1"] + " - Original Designer Cat Clothing",
      "description": p["short"],
      "brand": {"@type":"Brand","name":"Youna Global"},
      "offers": {
        "@type":"AggregateOffer",
        "priceCurrency":"USD",
        "lowPrice": p["price_low"],
        "highPrice": p["price_high"],
        "offerCount":"1",
        "availability":"https://schema.org/InStock"
      }
    }
    ld_json = json.dumps(ld, ensure_ascii=False, indent=2)

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{meta}" />
  <link rel="canonical" href="https://www.youna-global.com/products/{slug}.html" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{meta}" />
  <meta property="og:type" content="product" />
  <meta property="og:url" content="https://www.youna-global.com/products/{slug}.html" />
  <meta property="og:site_name" content="Youna Global" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" href="../assets/LOGO2.png" sizes="32x32" />
  <link rel="apple-touch-icon" href="../assets/LOGO2.png" />
  <link rel="stylesheet" href="../assets/style.css" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  assets/font-awesome/css/all.min.css
  <script type="application/ld+json">
  {ld}
  </script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-5NZQCPJRRX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-5NZQCPJRRX');
  </script>
</head>
<body>

{NAV}

<section class="section" style="padding-top:24px;padding-bottom:0;">
  <div class="container">
    <div class="breadcrumb">
      <a href="../index.html">Home</a>
      <span class="sep">/</span>
      <a href="../products/pet-supplies.html">Pet Supplies</a>
      <span class="sep">/</span>
      <span>{h1}</span>
    </div>
  </div>
</section>

<section class="section" style="padding-top:12px;">
  <div class="container">
    <div class="pdp-layout">
      <div class="pdp-gallery">
        <img src="{main}" alt="{h1}" class="pdp-main-img" id="mainImg" />
        <div class="pdp-thumbs">
          <img src="{main}" alt="{h1}" onclick="document.getElementById('mainImg').src=this.src" class="pdp-thumb active" />
          <img src="{t1}" alt="{h1} alternate view" onclick="document.getElementById('mainImg').src=this.src" class="pdp-thumb" />
          <img src="{t2}" alt="{h1} alternate view" onclick="document.getElementById('mainImg').src=this.src" class="pdp-thumb" />
        </div>
      </div>
      <div class="pdp-info">
        <h1>{h1}</h1>
        <div class="pdp-meta">
          <span><i class="fas fa-map-marker-alt"></i> Dongguan, China</span>
          <span><i class="fas fa-cube"></i> In Stock</span>
          <span><i class="fas fa-tags"></i> MOQ: 200 pcs</span>
        </div>
        <div class="pdp-price">${lo} - ${hi} <span class="unit">{unit}</span></div>
        <p class="pdp-short-desc">{short}</p>
        <table class="pdp-spec-table">
          {specs}
        </table>
        <div class="pdp-cta-group">
          <a href="{wa}" target="_blank" class="btn btn-primary"><i class="fab fa-whatsapp"></i> Get Quote on WhatsApp</a>
          <a href="../contact.html" class="btn btn-outline">Send Inquiry</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:#f8f9fa;">
  <div class="container">
    <h2 style="text-align:center;font-size:1.5rem;margin-bottom:32px;">How to Build Your Custom Cat Fashion Line</h2>
    <div class="pdp-features">
      <div class="pdp-feature"><div class="pdp-feature-icon"><i class="fas fa-palette"></i></div><h3>1. Choose Colorways &amp; Sizes</h3><p>Pick from our standard palettes or send PMS / reference colors for custom dye. Select 2-4 sizes across our XS-L cat run to cover most breeds.</p></div>
      <div class="pdp-feature"><div class="pdp-feature-icon"><i class="fas fa-pen-nib"></i></div><h3>2. Add Your Brand Logo</h3><p>We offer a sewn logo tag, custom hangtag, and printed branding. Send your AI or PDF artwork - our design team returns a free mockup within 24 hours.</p></div>
      <div class="pdp-feature"><div class="pdp-feature-icon"><i class="fas fa-box-open"></i></div><h3>3. Select Packaging</h3><p>Choose OPP bag with branded hangtag (default), backer card, or custom printed box for a premium unboxing. Layout design is free on 1,000+ pc orders.</p></div>
      <div class="pdp-feature"><div class="pdp-feature-icon"><i class="fas fa-check-circle"></i></div><h3>4. Approve Sample &amp; Ship</h3><p>We produce a physical sample in 5-7 days. Once approved, bulk runs 12-20 days. You get real-time photos and video updates throughout production.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="text-align:center;font-size:1.5rem;margin-bottom:32px;">Why Choose Our Designer Cat Clothing</h2>
    <div class="pdp-features">
      {feats}
    </div>
  </div>
</section>

<section class="section" style="background:#f8f9fa;">
  <div class="container">
    <h2 style="text-align:center;font-size:1.5rem;margin-bottom:32px;">Wholesale Cost &amp; Margin (Cat Apparel)</h2>
    <table class="pdp-spec-table" style="max-width:700px;margin:0 auto;">
      <tr><th>Item</th><th style="text-align:center;">Our Factory Price</th><th style="text-align:center;">Est. Retail</th><th style="text-align:center;">Your Margin</th></tr>
      <tr><td>{h1} (per unit)</td><td style="text-align:center;">${lo}-${hi}</td><td style="text-align:center;">$39-$79</td><td style="text-align:center;color:#1a73e8;font-weight:700;">~200-400%</td></tr>
      <tr><td>Shipping (sea, per unit, 500+ pcs)</td><td style="text-align:center;">~$0.30-$0.60</td><td style="text-align:center;">-</td><td style="text-align:center;">Negligible</td></tr>
    </table>
    <p style="text-align:center;color:#666;font-size:0.9rem;margin-top:16px;">{note}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="text-align:center;font-size:1.5rem;margin-bottom:32px;">Packaging &amp; What's Included</h2>
    <div style="max-width:700px;margin:0 auto;">
      <div style="background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:24px 28px;margin-bottom:20px;">
        <h3 style="font-size:1.1rem;margin-bottom:12px;color:#1a1a1a;"><i class="fas fa-box" style="color:var(--primary);margin-right:8px;"></i>Standard Package (Per Unit)</h3>
        <ul style="list-style:none;padding:0;margin:0;color:#444;line-height:2;">
          <li><i class="fas fa-check" style="color:#34a853;margin-right:8px;"></i>1x original Youna cat outfit as described</li>
          <li><i class="fas fa-check" style="color:#34a853;margin-right:8px;"></i>1x coordinated accessories (hat / bow / necklace / leash per design)</li>
          <li><i class="fas fa-check" style="color:#34a853;margin-right:8px;"></i>1x size-adjustment back closure</li>
          <li><i class="fas fa-check" style="color:#34a853;margin-right:8px;"></i>OPP bag + branded hangtag (default)</li>
        </ul>
      </div>
      <div style="background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:24px 28px;">
        <h3 style="font-size:1.1rem;margin-bottom:12px;color:#1a1a1a;"><i class="fas fa-palette" style="color:var(--primary);margin-right:8px;"></i>Customization Options</h3>
        <ul style="list-style:none;padding:0;margin:0;color:#444;line-height:2;">
          <li><i class="fas fa-check" style="color:#34a853;margin-right:8px;"></i><strong>Woven / printed logo tag</strong> - MOQ 200 pcs</li>
          <li><i class="fas fa-check" style="color:#34a853;margin-right:8px;"></i><strong>Custom dye / colorway</strong> - MOQ 200 pcs per color</li>
          <li><i class="fas fa-check" style="color:#34a853;margin-right:8px;"></i><strong>Custom trim &amp; buttons</strong> - bow / hat / leash recoloring</li>
          <li><i class="fas fa-check" style="color:#34a853;margin-right:8px;"></i><strong>Custom hangtag + box</strong> - MOQ 1,000 pcs</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:#f8f9fa;">
  <div class="container">
    <h2 style="text-align:center;font-size:1.5rem;margin-bottom:32px;">Who Should Buy This Product</h2>
    <div class="pdp-features">
      {who}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="text-align:center;font-size:1.5rem;margin-bottom:32px;">Frequently Asked Questions</h2>
    <div class="pdp-faq">
      {faqs}
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="container cta-inner">
    <div class="cta-text">
      <h2>Ready to Order {h1}?</h2>
      <p>Send us your quantity and customization requirements - we'll get back to you within 24 hours with a detailed quote.</p>
    </div>
    <div class="cta-actions">
      <a href="{wa}" target="_blank" class="btn btn-white btn-lg"><img src="../assets/WhatsApp%20LOGO.png" alt="WhatsApp" width="16" height="16" style="margin-right:6px;display:inline-block;vertical-align:middle;"> WhatsApp Us</a>
      <a href="../contact.html" class="btn btn-outline-white btn-lg">Send Inquiry</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="text-align:center;font-size:1.3rem;margin-bottom:24px;">More Designer Cat Looks</h2>
    <div class="catalog-grid">
      {rel}
    </div>
  </div>
</section>

{FOOTER}

<a href="https://wa.me/8619898484442" target="_blank" class="whatsapp-float" title="Chat on WhatsApp">
  <img src="../assets/WhatsApp%20LOGO.png" alt="WhatsApp" width="28" height="28" style="display:block;">
</a>

<script src="../assets/main.js"></script>
</body>
</html>
'''.format(
        title=p["title"], meta=p["meta"], slug=p["slug"], h1=p["h1"],
        main=img(p["main"]), t1=img(p["t1"]), t2=img(p["t2"]),
        lo=p["price_low"], hi=p["price_high"], unit=p["unit"], short=p["short"],
        specs=specs_html, feats=feats_html, faqs=faqs_html, who=who_html,
        wa=wa, rel=rel, NAV=NAV, FOOTER=FOOTER, note=PACKAGE_NOTE, ld=ld_json
    )

    fn = os.path.join(OUT, p["slug"] + ".html")
    with open(fn, "w", encoding="utf-8") as f:
        f.write(html)
    print("WROTE", fn, len(html), "bytes")

print("DONE", len(products), "product pages")
