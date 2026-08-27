(function () {
  const STORAGE_KEY = "detai_docs_preferred_locale";
  const chooser = document.querySelector(".language-choice");
  const links = Array.from(document.querySelectorAll(".language-choice__link"));

  links.forEach((link) => {
    link.addEventListener("click", () => {
      try {
        window.localStorage.setItem(STORAGE_KEY, link.dataset.locale);
      } catch (_error) {
        // Persistence is progressive enhancement; the link must still navigate.
      }
    });
  });

  if (!chooser || links.length === 0) {
    return;
  }

  document.documentElement.classList.add("detai-language-choice-active");
  links[0].focus({ preventScroll: true });

  chooser.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      event.preventDefault();
      return;
    }

    if (event.key !== "Tab") {
      return;
    }

    const firstLink = links[0];
    const lastLink = links[links.length - 1];

    if (event.shiftKey && document.activeElement === firstLink) {
      event.preventDefault();
      lastLink.focus();
    } else if (!event.shiftKey && document.activeElement === lastLink) {
      event.preventDefault();
      firstLink.focus();
    }
  });
})();
