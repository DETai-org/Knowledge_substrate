(function () {
  var storageKey = "detai:knowledge-substrate:nav-state:v1";
  var memoryState = window.__detaiNavStateMemory || {};
  window.__detaiNavStateMemory = memoryState;

  function loadState() {
    try {
      if (window.sessionStorage) {
        return JSON.parse(window.sessionStorage.getItem(storageKey) || "{}");
      }
    } catch (_error) {
      // Fall through to the in-memory state.
    }

    return memoryState;
  }

  function saveState(state) {
    memoryState = state;
    window.__detaiNavStateMemory = memoryState;

    try {
      if (window.sessionStorage) {
        window.sessionStorage.setItem(storageKey, JSON.stringify(state));
      }
    } catch (_error) {
      // Ignore storage failures so navigation keeps working in restricted modes.
    }
  }

  function normalize(text) {
    return (text || "").trim().replace(/\s+/g, " ");
  }

  function itemTitle(item) {
    var link = item && item.querySelector(":scope > .md-nav__link");
    var ellipsis = link && link.querySelector(".md-ellipsis");
    return normalize(ellipsis ? ellipsis.textContent : link && link.textContent);
  }

  function stateKey(input) {
    var item = input.closest(".md-nav__item");
    var parts = [];

    while (item) {
      var title = itemTitle(item);
      if (title) {
        parts.unshift(title);
      }

      item = item.parentElement && item.parentElement.closest(".md-nav__item");
    }

    return parts.join(" / ") || input.id;
  }

  function toggles() {
    return Array.prototype.slice.call(
      document.querySelectorAll(".md-sidebar--primary input.md-nav__toggle")
    );
  }

  function restore() {
    var state = loadState();

    toggles().forEach(function (input) {
      var key = stateKey(input);

      if (Object.prototype.hasOwnProperty.call(state, key)) {
        input.checked = Boolean(state[key]);
      }
    });
  }

  function bind() {
    restore();

    toggles().forEach(function (input) {
      if (input.dataset.detaiNavStateBound === "true") {
        return;
      }

      input.dataset.detaiNavStateBound = "true";
      input.addEventListener("change", function () {
        var state = loadState();
        state[stateKey(input)] = input.checked;
        saveState(state);
      });
    });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(function () {
      window.requestAnimationFrame(bind);
    });
  } else {
    document.addEventListener("DOMContentLoaded", bind);
  }
})();
