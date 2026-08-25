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

    // Disable option values that cannot combine with the selection made so far.
    //
    // Only the options BEFORE this one constrain it. Constraining by the later
    // options too would disable most of the first option — picking a material
    // would be blocked because the currently selected colour is not offered in
    // it, when in reality choosing that material simply moves you to a
    // different colour.
    function refreshAvailability(chosen) {
      inputs.forEach(function (input) {
        var pos = parseInt(input.dataset.optionPosition, 10);
        var probe = chosen.slice(0, pos - 1);
        probe[pos - 1] = input.value;
        var ok = !!find(probe);
        // `disabled` is a class in the KR sheet, not just the attribute: inside
        // .product-variants--hide-unavailable it hides the value entirely,
        // which is how kr.sidiz.com behaves — choosing a leather leaves only
        // the leather colours on screen.
        input.classList.toggle('disabled', !ok);
        input.disabled = !ok;
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

    function syncInputs(variant) {
      inputs.forEach(function (input) {
        var pos = parseInt(input.dataset.optionPosition, 10);
        input.checked = variant.options[pos - 1] === input.value;
      });
    }

    function onChange(event) {
      var chosen = selection();
      var variant = find(chosen);

      if (!variant) {
        // The combination does not exist — usually because the shopper changed
        // an early option and the later ones no longer apply. Honour the option
        // they just touched and everything before it, then let the rest follow.
        var changedPos = event && event.target
          ? parseInt(event.target.dataset.optionPosition, 10)
          : 1;
        var prefix = chosen.slice(0, changedPos);
        variant =
          variants.filter(function (candidate) {
            return candidate.available && matches(candidate, prefix);
          })[0] ||
          variants.filter(function (candidate) {
            return matches(candidate, prefix);
          })[0];
        if (variant) syncInputs(variant);
      }

      refreshAvailability(selection());
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
