(function () {
  const SUPPORTED_LANGS = ["en", "fi", "ru", "de", "cn"];
  const STORAGE_KEY = "detai_docs_preferred_locale";

  function getCurrentLanguage(pathname) {
    const langMatch = pathname.match(/\/(ru|en|de|fi|cn)\//i);
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

    if (/\/(ru|en|de|fi|cn)\//i.test(pathname)) {
      return pathname.replace(/\/(ru|en|de|fi|cn)\//i, `/${targetLang}/`) + search + hash;
    }

    const trimmed = pathname.replace(/\/+$/, "");
    return `${trimmed}/${targetLang}/${search}${hash}`.replace(/\/+/g, "/");
  }

  function buildLanguageRoot(targetLang) {
    const { pathname, search, hash } = window.location;
    const match = pathname.match(/^(.*)\/(ru|en|de|fi|cn)\//i);
    const root = `${match ? match[1] : ""}/${targetLang}/`.replace(/\/+/g, "/");
    return root + search + hash;
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

  function hasLocalizedEquivalent(pathname) {
    const match = pathname.match(/\/(ru|en|de|fi|cn)(\/.*)?$/i);
    const languagePath = match ? (match[2] || "/") : "/";
    return languagePath === "/" || languagePath === "/ecosystem/";
  }

  function updateLanguageLinks() {
    const currentLang = getCurrentLanguage(window.location.pathname);
    const targetByLabel = {
      English: "en",
      "Русский": "ru",
      Deutsch: "de",
      Suomi: "fi",
      中文: "cn",
    };

    const menuLinks = document.querySelectorAll(
      ".md-tabs__link, .md-nav__link, .md-select__link[data-locale]"
    );

    menuLinks.forEach((link) => {
      const targetLang = link.dataset.locale || targetByLabel[normalizeText(link)];
      if (!targetLang || targetLang === currentLang) {
        if (targetLang === currentLang) {
          link.setAttribute("aria-current", "true");
        }
        return;
      }

      const localizedUrl = buildLocalizedUrl(targetLang);
      const fallbackUrl = buildLanguageRoot(targetLang);

      link.setAttribute("href", localizedUrl);
      link.setAttribute("target", "_self");

      if (link.dataset.detaiLocalePersistence !== "true") {
        link.dataset.detaiLocalePersistence = "true";
        link.addEventListener("click", async (event) => {
          event.preventDefault();
          persistPreferredLocale(targetLang);

          if (hasLocalizedEquivalent(window.location.pathname)) {
            window.location.assign(localizedUrl);
            return;
          }

          try {
            const response = await window.fetch(localizedUrl, { method: "HEAD" });
            window.location.assign(response.ok ? localizedUrl : fallbackUrl);
          } catch (_error) {
            window.location.assign(fallbackUrl);
          }
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
