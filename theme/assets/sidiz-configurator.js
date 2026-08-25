/* SIDIZ configurator — variant switching for the PDP head.

   Reads the variant JSON printed by the section, resolves the selected option
   combination, and updates the price, SKU, hero image, add-to-cart state and
   URL. Options that lead to no variant at all are disabled rather than left
   selectable, so the shopper cannot reach a dead combination. */

(function () {
  'use strict';

  function money(cents, format) {
    var value = (cents / 100).toFixed(2);
    var parts = value.split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    var amount = parts.join('.');
    return format ? format.replace(/\{\{\s*amount\s*\}\}/, amount) : '$' + amount;
  }

  function init(root) {
    if (root.dataset.sidizConfiguratorReady === 'true') return;
    root.dataset.sidizConfiguratorReady = 'true';

    var dataEl = root.querySelector('[data-sidiz-variants]');
    if (!dataEl) return;

    var variants;
    try {
      variants = JSON.parse(dataEl.textContent);
    } catch (err) {
      return;
    }
    if (!variants || !variants.length) return;

    var inputs = Array.prototype.slice.call(
      root.querySelectorAll('.product-variant__input')
    );
    if (!inputs.length) return;

    var priceEl = root.querySelector('[data-sidiz-price]');
    var skuEl = root.querySelector('[data-sidiz-sku]');
    var idEl = root.querySelector('[data-sidiz-variant-id]');
    var atc = root.querySelector('.add-to-cart');
    var atcLabel = root.querySelector('[data-sidiz-atc-label]');
    var images = Array.prototype.slice.call(root.querySelectorAll('.variant-image'));

    var moneyFormat =
      (window.Shopify && window.Shopify.moneyFormat) || '${{amount}}';

    function selection() {
      var chosen = [];
      inputs.forEach(function (input) {
        if (!input.checked) return;
        var pos = parseInt(input.dataset.optionPosition, 10);
        chosen[pos - 1] = input.value;
      });
      return chosen;
    }

    function matches(variant, chosen) {
      return chosen.every(function (value, i) {
        return value === undefined || variant.options[i] === value;
      });
    }

    function find(chosen) {
      for (var i = 0; i < variants.length; i++) {
        if (matches(variants[i], chosen)) return variants[i];
      }
      return null;
    }

    // Disable option values that cannot combine with the rest of the selection.
    function refreshAvailability(chosen) {
      inputs.forEach(function (input) {
        var pos = parseInt(input.dataset.optionPosition, 10);
        var probe = chosen.slice();
        probe[pos - 1] = input.value;
        input.disabled = !find(probe);
      });
    }

    function render(variant) {
      if (priceEl) {
        var html =
          '<div class="discount--details-top">' +
          (variant.compare_at_price && variant.compare_at_price > variant.price
            ? '<span class="product-discount--percent">' +
              Math.round(
                ((variant.compare_at_price - variant.price) /
                  variant.compare_at_price) *
                  100
              ) +
              '%</span>'
            : '') +
          '<span class="product-price--best">' +
          money(variant.price, moneyFormat) +
          '</span></div>' +
          (variant.compare_at_price && variant.compare_at_price > variant.price
            ? '<s class="product-price--original">' +
              money(variant.compare_at_price, moneyFormat) +
              '</s>'
            : '');
        priceEl.innerHTML = html;
      }

      if (skuEl) skuEl.textContent = variant.sku || '';
      if (idEl) idEl.value = variant.id;

      if (atc) {
        atc.disabled = !variant.available;
        if (atcLabel) {
          atcLabel.textContent = variant.available ? 'Add to cart' : 'Sold out';
        }
      }

      images.forEach(function (img) {
        img.classList.toggle(
          'is-hidden',
          String(img.dataset.variantId) !== String(variant.id)
        );
      });
      // If this variant has no image of its own, keep the first one showing.
      if (images.length && !images.some(function (i) { return !i.classList.contains('is-hidden'); })) {
        images[0].classList.remove('is-hidden');
      }

      root.querySelectorAll('[data-sidiz-option-value]').forEach(function (el) {
        var pos = parseInt(el.dataset.sidizOptionValue, 10);
        el.textContent = variant.options[pos - 1] || '';
      });

      if (window.history && window.history.replaceState) {
        var url = new URL(window.location.href);
        url.searchParams.set('variant', variant.id);
        window.history.replaceState({}, '', url.toString());
      }
    }

    function onChange() {
      var chosen = selection();
      refreshAvailability(chosen);

      var variant = find(chosen);
      if (!variant) {
        // Fall back to the first variant that honours the option just changed.
        variant = variants.find(function (v) {
          return v.available && matches(v, [chosen[0]]);
        });
      }
      if (variant) render(variant);
    }

    inputs.forEach(function (input) {
      input.addEventListener('change', onChange);
    });

    refreshAvailability(selection());
  }

  function boot(scope) {
    (scope || document)
      .querySelectorAll('[data-sidiz-configurator]')
      .forEach(init);
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
