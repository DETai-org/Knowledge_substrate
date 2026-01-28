(() => {
  const MOBILE_QUERY = "(max-width: 76.24em)";

  const isMobileViewport = () => window.matchMedia(MOBILE_QUERY).matches;

  const getDrawerToggle = () =>
    document.querySelector("input#__drawer") || document.querySelector('[data-md-toggle="drawer"]');

  const closeDrawer = () => {
    const drawerToggle = getDrawerToggle();
    if (!drawerToggle) {
      return;
    }

    drawerToggle.checked = false;

    if (typeof window.__md_set === "function") {
      window.__md_set("__drawer", false);
    }
  };

  const closeDrawerOnMobile = () => {
    if (!isMobileViewport()) {
      return;
    }

    closeDrawer();
  };

  let handlersBound = false;

  const bindHandlers = () => {
    if (handlersBound) {
      return;
    }

    handlersBound = true;

    document.addEventListener("click", (event) => {
      if (!isMobileViewport()) {
        return;
      }

      const target = event.target;
      if (!(target instanceof Element)) {
        return;
      }

      if (target.closest(".md-overlay")) {
        closeDrawer();
        return;
      }

      if (target.closest(".md-sidebar--primary a")) {
        closeDrawer();
      }
    });
  };

  const scheduleAfterThemeReady = () => {
    window.requestAnimationFrame(() => {
      window.requestAnimationFrame(() => {
        // После полной загрузки темы на мобильной ширине сбрасываем состояние drawer.
        closeDrawerOnMobile();
        bindHandlers();
      });
    });
  };

  const initialize = () => {
    scheduleAfterThemeReady();
  };

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initialize);
  } else {
    document.addEventListener("DOMContentLoaded", initialize);
  }
})();
