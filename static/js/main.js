/*
js/main.js

* Adds smooth scrolling for in-page anchors.
* Toggles mobile navigation when the hamburger is clicked.
* Populates the footer year dynamically.
  */

/* Ensure DOM is ready */
document.addEventListener('DOMContentLoaded', function () {
// Smooth scrolling for anchor links
// This improves UX on browsers that don't support `scroll-behavior: smooth` natively.
const navLinks = document.querySelectorAll('a[href^="#"]');
navLinks.forEach(link => {
link.addEventListener('click', function (e) {
const targetId = this.getAttribute('href').slice(1);
const targetEl = document.getElementById(targetId);
if (targetEl) {
e.preventDefault();
targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });

```
    // Close mobile nav if open
    const navList = document.getElementById('primary-menu');
    if (navList.classList.contains('open')) {
      navList.classList.remove('open');
      // update aria-expanded on toggle
      const toggle = document.querySelector('.nav-toggle');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    }
  }
});
```

});

// Mobile nav toggle logic
const navToggle = document.querySelector('.nav-toggle');
const navList = document.getElementById('primary-menu');
if (navToggle && navList) {
navToggle.addEventListener('click', function () {
const isOpen = navList.classList.toggle('open');
// Reflect state for screen readers
this.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
});
}

// Insert current year into footer
const yearEl = document.getElementById('year');
if (yearEl) {
yearEl.textContent = new Date().getFullYear();
}

// Optional: enhance form validation UX (simple)
const form = document.querySelector('.contact-form');
if (form) {
form.addEventListener('submit', function (e) {
// Let the browser perform its HTML5 validation; here we can add custom checks if desired.
if (!form.checkValidity()) {
e.preventDefault();
// Focus first invalid control for convenience
const firstInvalid = form.querySelector(':invalid');
if (firstInvalid) firstInvalid.focus();
}
});
}
});})
