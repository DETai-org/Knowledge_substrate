(function () {
  const DRAWER_SELECTOR = '[data-md-toggle="drawer"]';
  const DESKTOP_QUERY = "(min-width: 76.25em)";

  const isMobileViewport = () => !window.matchMedia(DESKTOP_QUERY).matches;

  const closeDrawer = () => {
    const drawerToggle = document.querySelector(DRAWER_SELECTOR);
    if (!drawerToggle) {
      return;
    }
    if (isMobileViewport() && drawerToggle.checked) {
      drawerToggle.checked = false;
      if (typeof window.__md_set === "function") {
        window.__md_set("__drawer", false);
      }
    }
  };

  const initialize = () => {
    closeDrawer();
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
