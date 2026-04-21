/* ==========================================================================
   Tree Removal Service — Main JavaScript
   Vanilla JS, no dependencies
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {

  /* ------------------------------------------------------------------------
     1. Mobile Menu Toggle
     ---------------------------------------------------------------------- */
  (function initMobileMenu() {
    const toggle = document.querySelector('[data-menu-toggle]');
    const menu   = document.getElementById('mobile-menu');
    if (!toggle || !menu) return;

    const hamburgerIcon = toggle.querySelector('[data-icon-hamburger]');
    const closeIcon     = toggle.querySelector('[data-icon-close]');

    function openMenu() {
      menu.classList.remove('hidden');
      // rAF so the browser paints the element before animating
      requestAnimationFrame(function () {
        menu.classList.add('open');
      });
      toggle.setAttribute('aria-expanded', 'true');
      document.body.classList.add('menu-open');
      if (hamburgerIcon) hamburgerIcon.classList.add('hidden');
      if (closeIcon)     closeIcon.classList.remove('hidden');
    }

    function closeMenu() {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('menu-open');
      if (hamburgerIcon) hamburgerIcon.classList.remove('hidden');
      if (closeIcon)     closeIcon.classList.add('hidden');
      // Wait for transition then hide
      setTimeout(function () {
        if (!menu.classList.contains('open')) {
          menu.classList.add('hidden');
        }
      }, 320);
    }

    toggle.addEventListener('click', function () {
      const isOpen = menu.classList.contains('open');
      isOpen ? closeMenu() : openMenu();
    });

    // Close on any nav link click
    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeMenu);
    });

    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) {
        closeMenu();
        toggle.focus();
      }
    });
  }());


  /* ------------------------------------------------------------------------
     2. FAQ Accordion
     ---------------------------------------------------------------------- */
  (function initFaq() {
    const toggles = document.querySelectorAll('[data-faq-toggle]');
    if (!toggles.length) return;

    toggles.forEach(function (btn) {
      btn.addEventListener('click', function () {
        const isExpanded = btn.getAttribute('aria-expanded') === 'true';
        const answer     = btn.nextElementSibling;

        // Close all others first
        toggles.forEach(function (other) {
          if (other !== btn) {
            other.setAttribute('aria-expanded', 'false');
            const otherAnswer = other.nextElementSibling;
            if (otherAnswer) otherAnswer.classList.remove('open');
          }
        });

        // Toggle current
        btn.setAttribute('aria-expanded', String(!isExpanded));
        if (answer) {
          answer.classList.toggle('open', !isExpanded);
        }
      });
    });
  }());


  /* ------------------------------------------------------------------------
     3. Gallery Lightbox
     ---------------------------------------------------------------------- */
  (function initLightbox() {
    const items = document.querySelectorAll('[data-lightbox]');
    if (!items.length) return;

    // Build lightbox DOM
    const lb = document.createElement('div');
    lb.id = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Image lightbox');
    lb.innerHTML = [
      '<button class="lightbox-prev" aria-label="Previous image">',
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>',
      '</button>',
      '<img src="" alt="" id="lightbox-img">',
      '<button class="lightbox-next" aria-label="Next image">',
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>',
      '</button>',
      '<button class="lightbox-close" aria-label="Close lightbox">',
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
      '</button>',
    ].join('');
    document.body.appendChild(lb);

    const lbImg   = lb.querySelector('#lightbox-img');
    const lbClose = lb.querySelector('.lightbox-close');
    const lbPrev  = lb.querySelector('.lightbox-prev');
    const lbNext  = lb.querySelector('.lightbox-next');
    let currentIndex = 0;
    let previousFocus = null;

    // Collect all lightbox items into an array
    const imageList = Array.from(items);

    function open(index) {
      currentIndex  = index;
      previousFocus = document.activeElement;
      const item    = imageList[index];
      const src     = item.dataset.lightboxSrc || item.querySelector('img').src;
      const alt     = item.dataset.lightboxAlt || item.querySelector('img').alt || 'Gallery image';
      lbImg.src     = src;
      lbImg.alt     = alt;
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
      lbClose.focus();
    }

    function close() {
      lb.classList.remove('open');
      document.body.style.overflow = '';
      if (previousFocus) previousFocus.focus();
    }

    function showPrev() {
      currentIndex = (currentIndex - 1 + imageList.length) % imageList.length;
      open(currentIndex);
    }

    function showNext() {
      currentIndex = (currentIndex + 1) % imageList.length;
      open(currentIndex);
    }

    // Attach click to each gallery item
    imageList.forEach(function (item, i) {
      item.addEventListener('click', function () { open(i); });
      // Keyboard: Enter/Space
      item.setAttribute('tabindex', '0');
      item.setAttribute('role', 'button');
      item.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          open(i);
        }
      });
    });

    lbClose.addEventListener('click', close);
    lbPrev.addEventListener('click', showPrev);
    lbNext.addEventListener('click', showNext);

    // Close on overlay click (not image click)
    lb.addEventListener('click', function (e) {
      if (e.target === lb) close();
    });

    // Keyboard navigation
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape')     close();
      if (e.key === 'ArrowLeft')  showPrev();
      if (e.key === 'ArrowRight') showNext();
    });

    // Focus trap inside lightbox
    lb.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab') return;
      const focusable = lb.querySelectorAll('button');
      const first     = focusable[0];
      const last      = focusable[focusable.length - 1];
      if (e.shiftKey) {
        if (document.activeElement === first) { e.preventDefault(); last.focus(); }
      } else {
        if (document.activeElement === last)  { e.preventDefault(); first.focus(); }
      }
    });
  }());


  /* ------------------------------------------------------------------------
     4. Count-up on Scroll
     ---------------------------------------------------------------------- */
  (function initCountUp() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function animateCount(el) {
      const target   = parseInt(el.dataset.count, 10);
      const suffix   = el.dataset.countSuffix || '';
      const prefix   = el.dataset.countPrefix || '';
      const duration = 1800; // ms
      const start    = performance.now();

      if (prefersReduced) {
        el.textContent = prefix + target.toLocaleString() + suffix;
        return;
      }

      function step(now) {
        const elapsed  = now - start;
        const progress = Math.min(elapsed / duration, 1);
        // Ease out cubic
        const eased    = 1 - Math.pow(1 - progress, 3);
        const value    = Math.round(eased * target);
        el.textContent = prefix + value.toLocaleString() + suffix;
        if (progress < 1) requestAnimationFrame(step);
      }

      requestAnimationFrame(step);
    }

    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCount(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    counters.forEach(function (el) {
      observer.observe(el);
    });
  }());


  /* ------------------------------------------------------------------------
     5. Form Validation
     ---------------------------------------------------------------------- */
  (function initFormValidation() {
    const forms = document.querySelectorAll('form[data-validate]');
    if (!forms.length) return;

    const emailRe = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
    // Min 7 digits; allows digits, spaces, +, -, (, )
    const phoneRe = /^[\d\s+\-()\u00A0]{7,}$/;

    function getError(input) {
      const val  = input.value.trim();
      const type = input.type;

      if (input.required && !val) return 'This field is required.';
      if (!val) return null; // optional and empty — fine

      if (type === 'email' && !emailRe.test(val)) {
        return 'Please enter a valid email address.';
      }
      if (type === 'tel' && !phoneRe.test(val)) {
        return 'Please enter a valid phone number (at least 7 digits).';
      }
      return null;
    }

    function showError(input, msg) {
      const group = input.closest('.form-group') || input.parentElement;
      group.classList.add('field-error');

      let errEl = group.querySelector('.error-msg');
      if (!errEl) {
        errEl = document.createElement('span');
        errEl.className   = 'error-msg';
        errEl.setAttribute('aria-live', 'polite');
        group.appendChild(errEl);
      }
      errEl.textContent = msg;
      input.setAttribute('aria-invalid', 'true');
      input.setAttribute('aria-describedby', errEl.id || (errEl.id = 'err-' + Math.random().toString(36).slice(2)));
    }

    function clearError(input) {
      const group = input.closest('.form-group') || input.parentElement;
      group.classList.remove('field-error');
      const errEl = group.querySelector('.error-msg');
      if (errEl) errEl.textContent = '';
      input.removeAttribute('aria-invalid');
    }

    forms.forEach(function (form) {
      // Live validation on blur
      form.querySelectorAll('input, select, textarea').forEach(function (input) {
        input.addEventListener('blur', function () {
          const err = getError(input);
          err ? showError(input, err) : clearError(input);
        });

        input.addEventListener('input', function () {
          if (input.getAttribute('aria-invalid') === 'true') {
            const err = getError(input);
            err ? showError(input, err) : clearError(input);
          }
        });
      });

      form.addEventListener('submit', function (e) {
        e.preventDefault();

        // Honeypot check
        const honeypot = form.querySelector('[name="_gotcha"]');
        if (honeypot && honeypot.value) return; // silently abort

        let firstError = null;
        let valid      = true;

        form.querySelectorAll('input, select, textarea').forEach(function (input) {
          // Skip hidden honeypot
          if (input.name === '_gotcha') return;
          const err = getError(input);
          if (err) {
            showError(input, err);
            valid = false;
            if (!firstError) firstError = input;
          } else {
            clearError(input);
          }
        });

        if (!valid) {
          firstError.focus();
          return;
        }

        // Submit via fetch (Formspree / any POST endpoint)
        const action = form.getAttribute('action');
        const data   = new FormData(form);

        fetch(action, {
          method:  'POST',
          headers: { 'Accept': 'application/json' },
          body:    data,
        })
          .then(function (res) {
            if (!res.ok) throw new Error('Server error ' + res.status);
            return res.json();
          })
          .then(function () {
            form.style.display = 'none';
            const success = form.parentElement.querySelector('.form-success');
            if (success) success.classList.remove('hidden');
          })
          .catch(function () {
            // Surface a generic error without hiding the form
            let errBanner = form.querySelector('.form-submit-error');
            if (!errBanner) {
              errBanner           = document.createElement('p');
              errBanner.className = 'error-msg form-submit-error';
              errBanner.setAttribute('aria-live', 'polite');
              errBanner.style.marginTop = '1rem';
              form.appendChild(errBanner);
            }
            errBanner.textContent = 'Something went wrong — please try again or call us directly.';
          });
      });
    });
  }());


  /* ------------------------------------------------------------------------
     6. Active Nav Link (highlight current page)
     ---------------------------------------------------------------------- */
  (function initActiveNav() {
    const path     = window.location.pathname;
    // Extract filename (e.g. "about.html") or "index.html" for root
    const filename = path.split('/').pop() || 'index.html';

    document.querySelectorAll('.nav-link, .mobile-nav-link').forEach(function (link) {
      const href      = link.getAttribute('href') || '';
      const linkFile  = href.split('/').pop().split('?')[0];

      if (linkFile === filename || (filename === '' && linkFile === 'index.html')) {
        link.setAttribute('aria-current', 'page');
      }
    });
  }());


  /* ------------------------------------------------------------------------
     7. Header Shrink on Scroll
     ---------------------------------------------------------------------- */
  (function initHeaderShrink() {
    const header = document.querySelector('.site-header');
    if (!header) return;

    let ticking = false;

    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          if (window.scrollY > 60) {
            header.classList.add('scrolled');
          } else {
            header.classList.remove('scrolled');
          }
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }());

}); // end DOMContentLoaded
