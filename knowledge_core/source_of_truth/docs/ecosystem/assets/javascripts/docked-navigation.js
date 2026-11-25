(function () {
  var storageKey = "detai:knowledge-substrate:sidebar-width:v1";
  var compactStorageKey = "detai:knowledge-substrate:compact-sidebar-ratio:v1";
  var compactViewport = window.matchMedia("(max-width: 47.999em), (max-width: 76.234375em) and (pointer: coarse)");
  var desiredWidth = 260;
  var compactRatio = 1 / 3;
  var collapseThreshold = 56;
  var currentGrid;
  var sidebar;
  var rootTitle;
  var split;
  var gutter;
  var resizeFrame;

  try {
    var stored = Number(window.localStorage.getItem(storageKey));
    if (Number.isFinite(stored) && stored >= 120) desiredWidth = stored;
    var compactStored = window.localStorage.getItem(compactStorageKey);
    if (compactStored !== null && Number(compactStored) >= 0 && Number(compactStored) <= 1) {
      compactRatio = Number(compactStored);
    }
  } catch (_error) { /* Keep a working panel when storage is unavailable. */ }

  function limits() {
    var width = currentGrid.getBoundingClientRect().width;
    var compact = compactViewport.matches;
    var min = compact ? 0 : 180;
    var gutterWidth = compact ? 18 : 8;
    var contentMin = compact ? width / 3 : Math.min(280, width / 2);
    return {
      width: width,
      min: min,
      max: Math.max(min, Math.min(640, Math.floor(width - contentMin - gutterWidth))),
      gutterWidth: gutterWidth,
      contentMin: contentMin
    };
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

  function saveWidth(width) {
    var compact = compactViewport.matches;
    if (compact) compactRatio = width < collapseThreshold ? 0 : width / limits().width;
    else desiredWidth = width;
    try {
      window.localStorage.setItem(compact ? compactStorageKey : storageKey, String(compact ? compactRatio : desiredWidth));
    } catch (_error) { /* Optional persistence. */ }
  }

  function layout() {
    if (!currentGrid || !currentGrid.isConnected) return;
    if (split) {
      split.destroy();
      split = null;
    }
    var header = document.querySelector(".md-header");
    var headerHeight = header ? header.getBoundingClientRect().height : 48;
    document.documentElement.style.setProperty("--detai-header-height", headerHeight + "px");
    var compact = compactViewport.matches;
    var range = limits();
    var preferredWidth = compact ? Math.round(compactRatio * range.width) : desiredWidth;
    var width = Math.max(range.min, Math.min(range.max, preferredWidth));
    var collapsed = compact && width === 0;
    var toggle = document.querySelector(".detai-nav-toggle");
    document.documentElement.classList.toggle("detai-nav-compact", compact);
    document.documentElement.classList.remove("detai-nav-resizing");
    sidebar.hidden = collapsed;
    gutter.hidden = collapsed;
    if (toggle) toggle.setAttribute("aria-expanded", String(!collapsed));
    var toc = window.matchMedia("(min-width: 90em)").matches ? " 200px" : "";
    currentGrid.style.gridTemplateColumns = width + "px " + (collapsed ? 0 : range.gutterWidth) + "px 1fr" + toc;
    if (!collapsed && typeof window.Split === "function") {
      split = window.Split({
        columnGutters: [{ track: 1, element: gutter }],
        columnMinSizes: { 0: range.min, 2: range.contentMin },
        columnMaxSizes: { 0: range.max },
        snapOffset: 0,
        onDrag: updateAria,
        onDragStart: function () { document.documentElement.classList.add("detai-nav-resizing"); },
        onDragEnd: function () {
          document.documentElement.classList.remove("detai-nav-resizing");
          saveWidth(actualWidth());
          if (compact && compactRatio === 0) layout();
          else updateAria();
        }
      });
    }
    updateAria();
  }

  function undock() {
    if (!currentGrid) return;
    if (split) {
      split.destroy();
      split = null;
    }
    currentGrid.style.removeProperty("grid-template-columns");
    gutter.remove();
    if (rootTitle) rootTitle.setAttribute("for", "__drawer");
    currentGrid = null;
    sidebar = null;
    gutter = null;
    rootTitle = null;
    document.documentElement.classList.remove("detai-docked-nav", "detai-nav-compact", "detai-nav-resizing");
  }

  function bind() {
    var primary = document.querySelector(".md-sidebar--primary");
    var grid = primary && primary.parentElement;
    if (grid && grid === currentGrid && primary === sidebar) return;
    if (!primary || primary.hidden) {
      undock();
      return;
    }
    undock();
    var drawer = document.getElementById("__drawer");
    if (drawer && drawer.checked) drawer.click();
    currentGrid = grid;
    sidebar = primary;
    sidebar.id = "detai-navigation";
    document.documentElement.classList.add("detai-docked-nav");
    rootTitle = sidebar.querySelector('.md-nav--primary > .md-nav__title[for="__drawer"]');
    if (rootTitle) rootTitle.removeAttribute("for");
    gutter = document.createElement("div");
    gutter.className = "detai-nav-gutter";
    gutter.tabIndex = 0;
    gutter.setAttribute("role", "separator");
    gutter.setAttribute("aria-label", "Ширина навигации");
    gutter.setAttribute("aria-orientation", "vertical");
    gutter.setAttribute("aria-controls", sidebar.id);
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
      saveWidth(Math.max(range.min, Math.min(range.max, width)));
      layout();
      if (gutter.hidden) document.querySelector(".detai-nav-toggle")?.focus();
    });
    layout();
  }

  function requestLayout() {
    window.cancelAnimationFrame(resizeFrame);
    resizeFrame = window.requestAnimationFrame(layout);
  }

  window.addEventListener("resize", requestLayout);
  compactViewport.addEventListener("change", requestLayout);

  document.addEventListener("click", function (event) {
    if (!currentGrid || !compactViewport.matches || !event.target.closest(".detai-nav-toggle")) return;
    saveWidth(compactRatio === 0 ? limits().width / 3 : 0);
    layout();
  });

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(function () { window.requestAnimationFrame(bind); });
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bind);
  } else { bind(); }
})();
