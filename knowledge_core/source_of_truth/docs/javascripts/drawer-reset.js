(function () {
  const DRAWER_SELECTOR = '[data-md-toggle="drawer"]';
  const DESKTOP_QUERY = "(min-width: 76.25em)";
  let mediaListenerAttached = false;

  const isMobileViewport = () => !window.matchMedia(DESKTOP_QUERY).matches;

  const closeDrawer = () => {
    const drawerToggle = document.querySelector(DRAWER_SELECTOR);
    if (!drawerToggle) {
      return;
    }
    if (!isMobileViewport()) {
      return;
    }
    if (drawerToggle.checked) {
      drawerToggle.checked = false;
    }
    if (typeof window.__md_set === "function") {
      window.__md_set("__drawer", false);
    }
  };

  const deferUntilAfterTheme = (callback) => {
    if (typeof window.requestAnimationFrame === "function") {
      window.requestAnimationFrame(() => window.requestAnimationFrame(callback));
      return;
    }
    window.setTimeout(callback, 0);
  };

  const initialize = () => {
    deferUntilAfterTheme(closeDrawer);
    if (mediaListenerAttached) {
      return;
    }
    mediaListenerAttached = true;
    const media = window.matchMedia(DESKTOP_QUERY);
    if (typeof media.addEventListener === "function") {
      media.addEventListener("change", closeDrawer);
    } else if (typeof media.addListener === "function") {
      media.addListener(closeDrawer);
    }
  };

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initialize);
  } else {
    document.addEventListener("DOMContentLoaded", initialize);
  }
})();
