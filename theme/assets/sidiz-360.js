/* SIDIZ 360 viewer.

   Opens the .modal-360 matching the currently selected colour, lazily loading
   the rotation frames only once the viewer is actually opened. Uses Swiper when
   it is present (as the KR theme does) and falls back to scroll-snap plus the
   prev/next controls when it is not, so the viewer still works either way. */

(function () {
  'use strict';

  function currentColour(root) {
    var checked = root.querySelector(
      '.product-variant--wrapper .product-variant__input:checked[data-option-position="2"]'
    );
    if (checked) return checked.value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    return null;
  }

  function loadFrames(modal) {
    modal.querySelectorAll('img[data-src]').forEach(function (img) {
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
    });
  }

  function init(root) {
    if (root.dataset.sidiz360Ready === 'true') return;
    root.dataset.sidiz360Ready = 'true';

    var trigger = root.querySelector('[data-sidiz-360]');
    var modals = Array.prototype.slice.call(root.querySelectorAll('[data-sidiz-360-modal]'));
    if (!trigger || !modals.length) return;

    var swipers = new WeakMap();
    var lastFocus = null;

    function pick() {
      var colour = currentColour(root);
      return (
        modals.filter(function (m) {
          return m.dataset.colour === colour;
        })[0] || modals[0]
      );
    }

    function close(modal) {
      modal.classList.add('hidden');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    }

    function open() {
      var modal = pick();
      loadFrames(modal);
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
      lastFocus = document.activeElement;

      var closeBtn = modal.querySelector('[data-sidiz-360-close]');
      if (closeBtn) closeBtn.focus();

      if (typeof window.Swiper === 'function' && !swipers.has(modal)) {
        swipers.set(
          modal,
          new window.Swiper(modal.querySelector('.modal-360--swiper'), {
            slidesPerView: 'auto',
            centeredSlides: true,
            spaceBetween: 8,
            loop: true,
            navigation: {
              prevEl: modal.querySelector('.navigation-prev'),
              nextEl: modal.querySelector('.navigation-next'),
            },
          })
        );
      }
    }

    trigger.addEventListener('click', open);
    trigger.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        open();
      }
    });

    modals.forEach(function (modal) {
      var closeBtn = modal.querySelector('[data-sidiz-360-close]');
      if (closeBtn) {
        closeBtn.addEventListener('click', function () {
          close(modal);
        });
        closeBtn.addEventListener('keydown', function (event) {
          if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            close(modal);
          }
        });
      }

      // Fallback paging when Swiper is unavailable.
      var track = modal.querySelector('.swiper-wrapper');
      ['prev', 'next'].forEach(function (dir) {
        var btn = modal.querySelector('.navigation-' + dir);
        if (!btn || !track) return;
        btn.addEventListener('click', function () {
          if (typeof window.Swiper === 'function') return;
          var slide = track.querySelector('.swiper-slide');
          var step = slide ? slide.offsetWidth + 8 : track.clientWidth;
          track.scrollBy({ left: dir === 'next' ? step : -step, behavior: 'smooth' });
        });
      });
    });

    document.addEventListener('keydown', function (event) {
      if (event.key !== 'Escape') return;
      modals.forEach(function (modal) {
        if (!modal.classList.contains('hidden')) close(modal);
      });
    });
  }

  function boot(scope) {
    (scope || document).querySelectorAll('[data-sidiz-configurator]').forEach(init);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      boot();
    });
  } else {
    boot();
  }

  document.addEventListener('shopify:section:load', function (event) {
    boot(event.target);
  });
})();
