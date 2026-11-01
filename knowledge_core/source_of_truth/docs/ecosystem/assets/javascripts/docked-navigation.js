(function () {
  var storageKey = "detai:knowledge-substrate:sidebar-width:v1";
  var desiredWidth = 260;
  var currentGrid;
  var split;
  var gutter;
  var resizeFrame;

  try {
    var stored = Number(window.localStorage.getItem(storageKey));
    if (Number.isFinite(stored) && stored >= 120) desiredWidth = stored;
  } catch (_error) { /* Keep a working panel when storage is unavailable. */ }

  function limits() {
    var width = currentGrid.getBoundingClientRect().width;
    var min = width < 600 ? 120 : 180;
    var contentMin = Math.min(280, width / 2);
    return { min: min, max: Math.max(min, Math.min(640, width - contentMin - 8)) };
  }

  function actualWidth() {
    return parseFloat(window.getComputedStyle(currentGrid).gridTemplateColumns);
  }

  function updateAria() {
    var range = limits();
    gutter.setAttribute("aria-valuemin", Math.round(range.min));
    gutter.setAttribute("aria-valuemax", Math.round(range.max));
    gutter.setAttribute("aria-valuenow", Math.round(actualWidth()));
  }

  function saveWidth() {
    desiredWidth = actualWidth();
    try { window.localStorage.setItem(storageKey, String(desiredWidth)); } catch (_error) { /* Optional persistence. */ }
    updateAria();
  }

  function layout() {
    if (!currentGrid || !currentGrid.isConnected) return;
    if (split) split.destroy(true);
    var header = document.querySelector(".md-header");
    var headerHeight = header ? header.getBoundingClientRect().height : 48;
    document.documentElement.style.setProperty("--detai-header-height", headerHeight + "px");
    var range = limits();
    var width = Math.max(range.min, Math.min(range.max, desiredWidth));
    var toc = window.matchMedia("(min-width: 90em)").matches ? " 200px" : "";
    currentGrid.style.gridTemplateColumns = width + "px 8px 1fr" + toc;
    if (typeof window.Split === "function") {
      split = window.Split({
        columnGutters: [{ track: 1, element: gutter }],
        columnMinSizes: { 0: range.min, 2: Math.min(280, currentGrid.clientWidth / 2) },
        columnMaxSizes: { 0: range.max },
        snapOffset: 0,
        onDrag: updateAria,
        onDragStart: function () { document.documentElement.classList.add("detai-nav-resizing"); },
        onDragEnd: function () {
          document.documentElement.classList.remove("detai-nav-resizing");
          saveWidth();
        }
      });
    }
    updateAria();
  }

  function bind() {
    var sidebar = document.querySelector(".md-sidebar--primary");
    var grid = sidebar && sidebar.parentElement;
    if (!sidebar || sidebar.hidden) {
      document.documentElement.classList.remove("detai-docked-nav");
      return;
    }
    if (grid === currentGrid) return;
    if (split) split.destroy(true);
    currentGrid = grid;
    document.documentElement.classList.add("detai-docked-nav");
    var rootTitle = sidebar.querySelector(".md-nav--primary > .md-nav__title");
    if (rootTitle) rootTitle.removeAttribute("for");
    gutter = document.createElement("div");
    gutter.className = "detai-nav-gutter";
    gutter.tabIndex = 0;
    gutter.setAttribute("role", "separator");
    gutter.setAttribute("aria-label", "Ширина навигации");
    gutter.setAttribute("aria-orientation", "vertical");
    grid.insertBefore(gutter, sidebar.nextSibling);
    // Split Grid prevents the native mousedown focus, so retain keyboard access explicitly.
    gutter.addEventListener("mousedown", function () { gutter.focus({ preventScroll: true }); });
    gutter.addEventListener("keydown", function (event) {
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
      event.preventDefault();
      var range = limits();
      var width = actualWidth();
      if (event.key === "Home") width = range.min;
      else if (event.key === "End") width = range.max;
      else width += (event.key === "ArrowRight" ? 1 : -1) * (event.shiftKey ? 40 : 16);
      desiredWidth = Math.max(range.min, Math.min(range.max, width));
      layout();
      saveWidth();
    });
    layout();
  }

  window.addEventListener("resize", function () {
    window.cancelAnimationFrame(resizeFrame);
    resizeFrame = window.requestAnimationFrame(layout);
  });

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(function () { window.requestAnimationFrame(bind); });
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bind);
  } else { bind(); }
})();
