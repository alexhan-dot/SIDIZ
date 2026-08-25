/* SIDIZ tabs — WAI-ARIA tab pattern for [data-sidiz-tabs].
   Panels are in the DOM already; this only toggles the hidden attribute and
   moves roving focus, so the content stays crawlable with JS disabled. */

(function () {
  'use strict';

  function init(root) {
    if (root.dataset.sidizTabsReady === 'true') return;
    root.dataset.sidizTabsReady = 'true';

    var tabs = Array.prototype.slice.call(root.querySelectorAll('[role="tab"]'));
    if (!tabs.length) return;

    function select(index, focus) {
      tabs.forEach(function (tab, i) {
        var selected = i === index;
        tab.setAttribute('aria-selected', selected ? 'true' : 'false');
        tab.tabIndex = selected ? 0 : -1;

        var panel = document.getElementById(tab.getAttribute('aria-controls'));
        if (panel) panel.hidden = !selected;
      });
      if (focus) tabs[index].focus();
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () {
        select(i, false);
      });

      tab.addEventListener('keydown', function (event) {
        var last = tabs.length - 1;
        var next = null;

        switch (event.key) {
          case 'ArrowRight':
          case 'ArrowDown':
            next = i === last ? 0 : i + 1;
            break;
          case 'ArrowLeft':
          case 'ArrowUp':
            next = i === 0 ? last : i - 1;
            break;
          case 'Home':
            next = 0;
            break;
          case 'End':
            next = last;
            break;
          default:
            return;
        }

        event.preventDefault();
        select(next, true);
      });
    });
  }

  function boot(scope) {
    (scope || document).querySelectorAll('[data-sidiz-tabs]').forEach(init);
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
