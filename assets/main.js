// Youna Global - Main JS

// Mobile nav toggle
(function() {
  'use strict';
  
  document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');
    
    if (navToggle && navLinks) {
      navToggle.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        navLinks.classList.toggle('open');
        console.log('Menu toggled:', navLinks.classList.contains('open'));
      });
      
      // Close menu when clicking on links
      navLinks.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', function() {
          navLinks.classList.remove('open');
        });
      });
      
      // Close menu when clicking outside
      document.addEventListener('click', function(e) {
        if (navLinks.classList.contains('open') && 
            !navLinks.contains(e.target) && 
            !navToggle.contains(e.target)) {
          navLinks.classList.remove('open');
        }
      });
    }
  });
})();

// Contact form handler
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    // Allow form to submit normally
  });
}

// Success modal
document.addEventListener('DOMContentLoaded', function() {
  if (window.location.search.includes('success=true')) {
    const successModal = document.getElementById('successModal');
    if (successModal) {
      successModal.style.display = 'flex';
      window.history.replaceState({}, document.title, window.location.pathname);
      setTimeout(function() {
        successModal.style.display = 'none';
      }, 5000);
    }
  }
});

// Trust Carousel
document.addEventListener('DOMContentLoaded', function() {
  const trustCarousel = document.querySelector('.trust-carousel');
  if (!trustCarousel) return;

  const trustTrack = trustCarousel.querySelector('.trust-track');
  if (!trustTrack) return;
  
  // Pause on hover
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
  
  // Responsive animation speed
  function adjustSpeed() {
    const width = window.innerWidth;
    let speed = '30s';
    
    if (width <= 640) {
      speed = '20s';
    } else if (width <= 900) {
      speed = '25s';
    }
    
    trustTrack.style.animationDuration = speed;
  }
  
  adjustSpeed();
  window.addEventListener('resize', adjustSpeed);
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Navbar scroll effect
const navbar = document.querySelector('.navbar');
if (navbar) {
  window.addEventListener('scroll', function() {
    navbar.style.boxShadow = window.scrollY > 10 ? '0 2px 20px rgba(0,0,0,0.08)' : 'none';
  });
}

// Animate elements on scroll
const observer = new IntersectionObserver(function(entries) {
  entries.forEach(function(entry) {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.service-card, .why-card, .testimonial-card, .step, .value-card, .country-item').forEach(function(el) {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});
