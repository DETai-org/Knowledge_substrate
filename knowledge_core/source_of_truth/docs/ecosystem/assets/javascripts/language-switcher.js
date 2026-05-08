(function () {
  const SUPPORTED_LANGS = ["ru", "en", "de", "fi", "cn"];

  function getCurrentLanguage(pathname) {
    const langMatch = pathname.match(/\/(ru|en|de|fi|cn)\//i);
    if (langMatch) {
      return langMatch[1].toLowerCase();
    }
    return "ru";
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
      中文: "cn",
    };

    const menuLinks = document.querySelectorAll(
      ".md-tabs__link, .md-nav__link"
    );

    menuLinks.forEach((link) => {
      const targetLang = targetByLabel[normalizeText(link)];
      if (!targetLang || targetLang === currentLang) {
        return;
      }

      link.setAttribute("href", buildLocalizedUrl(targetLang));
    });
  }

  document.addEventListener("DOMContentLoaded", updateLanguageLinks);
})();
