/* SIDIZ sticky nav — highlights the section currently in view and reveals the
   bar only once the visitor has scrolled past the buy box. */

(function () {
  'use strict';

  function init(nav) {
    if (nav.dataset.sidizStickyNavReady === 'true') return;
    nav.dataset.sidizStickyNavReady = 'true';

    var links = Array.prototype.slice.call(nav.querySelectorAll('[data-sidiz-anchor]'));
    var targets = links
      .map(function (link) {
        return document.getElementById(link.dataset.sidizAnchor);
      })
      .filter(Boolean);

    // Reveal the bar once the PDP head has scrolled out of view.
    var head = document.getElementById('sidiz-pdp-head');
    if (head && 'IntersectionObserver' in window) {
      new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            nav.classList.toggle('is-visible', !entry.isIntersecting);
          });
        },
        { rootMargin: '-120px 0px 0px 0px' }
      ).observe(head);
    } else {
      nav.classList.add('is-visible');
    }

    if (!targets.length || !('IntersectionObserver' in window)) return;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          links.forEach(function (link) {
            link.classList.toggle(
              'is-current',
              link.dataset.sidizAnchor === entry.target.id
            );
          });
        });
      },
      { rootMargin: '-45% 0px -45% 0px' }
    );

    targets.forEach(function (target) {
      observer.observe(target);
    });
  }

  function boot(scope) {
    (scope || document).querySelectorAll('[data-sidiz-sticky-nav]').forEach(init);
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
