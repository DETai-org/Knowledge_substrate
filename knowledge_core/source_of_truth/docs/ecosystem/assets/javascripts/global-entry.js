(function () {
  const STORAGE_KEY = "detai_docs_preferred_locale";
  const chooser = document.querySelector(".language-choice");
  const backdrop = document.querySelector(".language-choice-backdrop");
  const openButton = document.querySelector("[data-language-choice-open]");
  const closeButton = document.querySelector("[data-language-choice-close]");
  const links = Array.from(document.querySelectorAll(".language-choice__link"));
  const supportedLocales = new Set(links.map((link) => link.dataset.locale));

  function readPreferredLocale() {
    try {
      const locale = window.localStorage.getItem(STORAGE_KEY);
      return supportedLocales.has(locale) ? locale : null;
    } catch (_error) {
      return null;
    }
  }

  function showChooser() {
    if (!chooser) {
      return;
    }

    chooser.setAttribute("aria-hidden", "false");
    document.documentElement.classList.add("detai-language-choice-active");
  }

  function hideChooser() {
    if (!chooser) {
      return;
    }

    chooser.setAttribute("aria-hidden", "true");
    document.documentElement.classList.remove("detai-language-choice-active");
    openButton?.focus({ preventScroll: true });
  }

  links.forEach((link) => {
    link.addEventListener("click", () => {
      try {
        window.localStorage.setItem(STORAGE_KEY, link.dataset.locale);
      } catch (_error) {
        // Persistence is progressive enhancement; the link must still navigate.
      }
    });
  });

  if (!chooser || !backdrop || links.length === 0) {
    return;
  }

  if (readPreferredLocale()) {
    hideChooser();
  } else {
    showChooser();
  }

  openButton?.addEventListener("click", showChooser);
  closeButton?.addEventListener("click", hideChooser);

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      hideChooser();
      return;
    }
  });
})();
