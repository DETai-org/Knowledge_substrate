(function () {
  const SUPPORTED_LANGS = ["en", "fi", "ru", "de", "zh"];
  const STORAGE_KEY = "detai_docs_preferred_locale";

  function getCurrentLanguage(pathname) {
    const langMatch = pathname.match(/\/(ru|en|de|fi|zh)\//i);
    if (langMatch) {
      return langMatch[1].toLowerCase();
    }
    return null;
  }

  function buildLocalizedUrl(targetLang) {
    const { pathname, search, hash } = window.location;

    if (!SUPPORTED_LANGS.includes(targetLang)) {
      return pathname + search + hash;
    }

    if (/\/(ru|en|de|fi|zh)\//i.test(pathname)) {
      return pathname.replace(/\/(ru|en|de|fi|zh)\//i, `/${targetLang}/`) + search + hash;
    }

    const trimmed = pathname.replace(/\/+$/, "");
    return `${trimmed}/${targetLang}/${search}${hash}`.replace(/\/+/g, "/");
  }

  function persistPreferredLocale(targetLang) {
    try {
      window.localStorage.setItem(STORAGE_KEY, targetLang);
    } catch (_error) {
      // Persistence is progressive enhancement; navigation must still work.
    }
  }

  function normalizeText(element) {
    return element.textContent.replace(/\s+/g, " ").trim();
  }

  function updateLanguageLinks() {
    const currentLang = getCurrentLanguage(window.location.pathname);
    const targetByLabel = {
      English: "en",
      "Русский": "ru",
      Deutsch: "de",
      Suomi: "fi",
      中文: "zh",
    };

    const menuLinks = document.querySelectorAll(
      ".md-tabs__link, .md-nav__link, .md-select__link[data-locale]"
    );

    menuLinks.forEach((link) => {
      const targetLang = link.dataset.locale || targetByLabel[normalizeText(link)];
      if (!targetLang) {
        return;
      }

      const localizedUrl = buildLocalizedUrl(targetLang);
      link.setAttribute("href", localizedUrl);
      link.setAttribute("target", "_self");

      if (targetLang === currentLang) {
        link.setAttribute("aria-current", "true");
      } else {
        link.removeAttribute("aria-current");
      }

      if (link.dataset.detaiLocalePersistence !== "true") {
        link.dataset.detaiLocalePersistence = "true";
        link.addEventListener("click", () => {
          persistPreferredLocale(targetLang);
        });
      }
    });
  }

  if (typeof document$ !== "undefined" && document$ && typeof document$.subscribe === "function") {
    document$.subscribe(updateLanguageLinks);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", updateLanguageLinks);
  } else {
    updateLanguageLinks();
  }
})();
