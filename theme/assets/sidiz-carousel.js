/* SIDIZ carousel — drives [data-sidiz-carousel] banners.
   Scroll-snap does the moving; this only syncs dots and handles autoplay. */

(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function init(root) {
    if (root.dataset.sidizCarouselReady === 'true') return;
    root.dataset.sidizCarouselReady = 'true';

    var track = root.querySelector('.sidiz-banner__track');
    var dots = Array.prototype.slice.call(root.querySelectorAll('.sidiz-banner__dot'));
    var slides = Array.prototype.slice.call(root.querySelectorAll('.sidiz-banner__slide'));
    if (!track || slides.length < 2) return;

    var current = 0;
    var timer = null;

    function select(index) {
      current = index;
      dots.forEach(function (dot, i) {
        if (i === index) {
          dot.setAttribute('aria-selected', 'true');
        } else {
          dot.removeAttribute('aria-selected');
        }
      });
    }

    function goTo(index, smooth) {
      var target = slides[index];
      if (!target) return;
      track.scrollTo({
        left: target.offsetLeft,
        behavior: smooth && !reduceMotion ? 'smooth' : 'auto',
      });
      select(index);
    }

    dots.forEach(function (dot) {
      dot.addEventListener('click', function () {
        stop();
        goTo(parseInt(dot.dataset.index, 10), true);
        start();
      });
    });

    // Keep the dots honest when the user swipes.
    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) select(slides.indexOf(entry.target));
          });
        },
        { root: track, threshold: 0.6 }
      );
      slides.forEach(function (slide) {
        observer.observe(slide);
      });
    }

    function start() {
      if (root.dataset.autoplay !== 'true' || reduceMotion) return;
      var interval = parseInt(root.dataset.interval, 10) || 6000;
      timer = window.setInterval(function () {
        goTo((current + 1) % slides.length, true);
      }, interval);
    }

    function stop() {
      if (timer) window.clearInterval(timer);
      timer = null;
    }

    root.addEventListener('mouseenter', stop);
    root.addEventListener('mouseleave', start);
    root.addEventListener('focusin', stop);

    document.addEventListener('visibilitychange', function () {
      if (document.hidden) {
        stop();
      } else {
        start();
      }
    });

    start();
  }

  function boot(scope) {
    (scope || document).querySelectorAll('[data-sidiz-carousel]').forEach(init);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      boot();
    });
  } else {
    boot();
  }

  // Theme editor re-renders sections without a page load.
  document.addEventListener('shopify:section:load', function (event) {
    boot(event.target);
  });
})();
