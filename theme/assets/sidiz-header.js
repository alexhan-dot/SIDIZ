/* SIDIZ header contrast.

   The header is fixed over the page and only its text changes colour — white
   over dark sections, black over light ones. Nothing else about it inverts.

   mix-blend-mode: difference was the wrong tool: it works per channel, so a
   coloured backdrop gives coloured text (a green "SPECIAL OFFERS" over a red
   chair) rather than the clean black or white this design wants.

   Instead each section declares what sits behind the header via
   data-header-scheme="dark|light". Whichever declaring section is crossing the
   header band decides the scheme, so the switch happens exactly as a dark
   section slides under the bar. Sections that declare nothing count as light,
   which is the common case. */

(function () {
  'use strict';

  var HEADER_BAND = 72; // px of page the bar actually covers

  function init(header) {
    if (header.dataset.sidizHeaderReady === 'true') return;
    header.dataset.sidizHeaderReady = 'true';

    var sections = Array.prototype.slice.call(
      document.querySelectorAll('[data-header-scheme]')
    );

    function apply(scheme) {
      header.classList.toggle('header--on-dark', scheme === 'dark');
      header.classList.toggle('header--on-light', scheme !== 'dark');
    }

    function currentScheme() {
      // The declaring section whose box covers the header band wins. Reading
      // rects on scroll is cheap enough here — there are only a handful.
      for (var i = 0; i < sections.length; i++) {
        var rect = sections[i].getBoundingClientRect();
        if (rect.top <= HEADER_BAND && rect.bottom >= HEADER_BAND) {
          return sections[i].dataset.headerScheme;
        }
      }
      return 'light';
    }

    var ticking = false;
    function onScroll() {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        apply(currentScheme());
        header.classList.toggle('header--scrolled', window.scrollY > 8);
        ticking = false;
      });
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    onScroll();
  }

  function boot() {
    var header = document.querySelector('[data-sidiz-header]');
    if (header) init(header);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  document.addEventListener('shopify:section:load', boot);
})();
