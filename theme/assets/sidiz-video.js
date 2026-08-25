/* SIDIZ lazy video.

   The T90 page carries ~14 autoplaying background videos. Letting them all
   fetch on load competes for bandwidth, so the video the visitor is actually
   looking at arrives late and stalls — which reads as poor quality even though
   the file is fine.

   This defers every video until it is near the viewport, then attaches its
   source and plays it; videos that scroll away are paused so they stop
   consuming bandwidth and battery. The poster carries the frame until then, so
   nothing looks empty.

   Markup contract: <video data-sidiz-video preload="none" poster="…">
                      <source data-src="…" type="video/mp4">
                    </video>
   A video marked data-eager loads immediately — use it for the hero only. */

(function () {
  'use strict';

  var ROOT_MARGIN = '400px 0px';
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function attach(video) {
    if (video.dataset.sidizLoaded === 'true') return;
    video.dataset.sidizLoaded = 'true';

    video.querySelectorAll('source[data-src]').forEach(function (source) {
      source.src = source.dataset.src;
      source.removeAttribute('data-src');
    });
    video.load();
  }

  function play(video) {
    attach(video);
    if (reduceMotion) return;
    var attempt = video.play();
    // Autoplay can still be refused (low power mode, data saver); the poster
    // stays visible, so there is nothing to recover from.
    if (attempt && typeof attempt.catch === 'function') attempt.catch(function () {});
  }

  function init(video) {
    if (video.dataset.sidizVideoReady === 'true') return;
    video.dataset.sidizVideoReady = 'true';

    if (video.dataset.eager === 'true') {
      play(video);
      return;
    }

    if (!('IntersectionObserver' in window)) {
      play(video);
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            play(entry.target);
          } else if (entry.target.dataset.sidizLoaded === 'true') {
            entry.target.pause();
          }
        });
      },
      { rootMargin: ROOT_MARGIN, threshold: 0.01 }
    );

    observer.observe(video);
  }

  function boot(scope) {
    (scope || document).querySelectorAll('video[data-sidiz-video]').forEach(init);
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

  // Stop everything while the tab is hidden.
  document.addEventListener('visibilitychange', function () {
    if (!document.hidden) return;
    document.querySelectorAll('video[data-sidiz-video]').forEach(function (video) {
      video.pause();
    });
  });
})();
