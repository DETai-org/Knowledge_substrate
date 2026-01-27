(function () {
  const BUTTON_CLASS = "chatgpt-action";
  const BUTTON_ID = "chatgpt-open-button";
  const CHATGPT_URL = "https://chatgpt.com/";
  const TOAST_CLASS = "chatgpt-toast";
  const TOAST_DURATION_MS = 1600;

  const isDesktopViewport = () => window.matchMedia("(min-width: 1024px)").matches;

  const DEFAULT_PROMPT_TEMPLATES = {
    ru: "Прочитай <CURRENT_PAGE_URL> и отвечай на вопросы о содержимом.",
    en: "Read <CURRENT_PAGE_URL> and answer questions about the content.",
  };

  const getPageLanguage = () => {
    const langAttribute = document.documentElement.lang?.trim();
    if (langAttribute) {
      return langAttribute.split("-")[0].toLowerCase();
    }
    document.documentElement.lang = "ru";
    return "ru";
  };

  const getPromptTemplates = () => {
    if (window.chatgptPromptTemplate && typeof window.chatgptPromptTemplate === "object") {
      return window.chatgptPromptTemplate;
    }
    if (typeof window.chatgptPromptTemplate === "string" && window.chatgptPromptTemplate.trim()) {
      return { en: window.chatgptPromptTemplate };
    }
    return DEFAULT_PROMPT_TEMPLATES;
  };

  const getPromptTemplate = () => {
    const templates = getPromptTemplates();
    const language = getPageLanguage();
    return templates[language] || templates.en || DEFAULT_PROMPT_TEMPLATES.en;
  };

  const buildPrompt = (url) => {
    const template = getPromptTemplate();
    return template.replace(/<CURRENT_PAGE_URL>|\{\{\s*url\s*\}\}/g, url);
  };

  const copyPrompt = async (prompt) => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(prompt);
      return;
    }

    const textarea = document.createElement("textarea");
    textarea.value = prompt;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "absolute";
    textarea.style.left = "-9999px";
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
  };

  const getToast = () => document.querySelector(`.${TOAST_CLASS}`);

  const createToast = () => {
    const toast = document.createElement("div");
    toast.className = TOAST_CLASS;
    toast.setAttribute("role", "status");
    toast.setAttribute("aria-live", "polite");
    document.body.appendChild(toast);
    return toast;
  };

  const getToastMessages = () => {
    const language = getPageLanguage();
    if (language === "ru") {
      return {
        success: "Промпт скопирован — вставь в ChatGPT (Ctrl+V)",
        failure: "Не удалось скопировать — скопируй вручную",
      };
    }
    return {
      success: "Prompt copied — paste in ChatGPT (Ctrl+V)",
      failure: "Couldn’t copy — please copy manually",
    };
  };

  const showToast = (message) => {
    if (!isDesktopViewport()) {
      return;
    }
    const toast = getToast() || createToast();
    toast.textContent = message;
    toast.classList.add("is-visible");
    window.setTimeout(() => {
      toast.classList.remove("is-visible");
    }, TOAST_DURATION_MS);
  };

  const buildChatGptUrl = (prompt) => `${CHATGPT_URL}?prompt=${encodeURIComponent(prompt)}`;

  const ensureButton = () => {
    if (!isDesktopViewport()) {
      const existing = document.getElementById(BUTTON_ID);
      if (existing) {
        existing.remove();
      }
      const toast = getToast();
      if (toast) {
        toast.remove();
      }
      return;
    }

    const content = document.querySelector(".md-content__inner");
    if (!content) {
      return;
    }

    const existing = document.getElementById(BUTTON_ID);
    if (existing) {
      existing.remove();
    }

    const wrapper = document.createElement("div");
    wrapper.className = BUTTON_CLASS;
    wrapper.id = BUTTON_ID;

    const button = document.createElement("a");
    button.className = "md-button";
    button.textContent = "Open in ChatGPT";
    button.href = CHATGPT_URL;
    button.target = "_blank";
    button.rel = "noopener";

    let feedbackTimeout;

    const setFeedback = (message, delay) => {
      if (feedbackTimeout) {
        clearTimeout(feedbackTimeout);
      }
      button.textContent = message;
      feedbackTimeout = window.setTimeout(() => {
        button.textContent = "Open in ChatGPT";
      }, delay);
    };

    const refreshButtonHref = () => {
      const prompt = buildPrompt(window.location.href);
      button.href = buildChatGptUrl(prompt);
    };

    ["mouseenter", "focus", "contextmenu"].forEach((eventName) => {
      button.addEventListener(eventName, refreshButtonHref);
    });

    button.addEventListener("click", async (event) => {
      event.preventDefault();
      const url = window.location.href;
      const prompt = buildPrompt(url);
      const chatGptUrl = buildChatGptUrl(prompt);
      button.href = chatGptUrl;

      const toastMessages = getToastMessages();

      try {
        await copyPrompt(prompt);
        setFeedback("Copied!", 1000);
        showToast(toastMessages.success);
      } catch (error) {
        console.warn("Не удалось скопировать prompt в буфер обмена.", error);
        setFeedback("Copy failed", 1200);
        showToast(toastMessages.failure);
      }

      window.open(chatGptUrl, "_blank", "noopener");
    });

    wrapper.appendChild(button);

    const actionsContainer = document.querySelector(".md-content__button");
    if (actionsContainer) {
      actionsContainer.prepend(wrapper);
    } else {
      content.prepend(wrapper);
    }
  };

  const initialize = () => {
    ensureButton();
  };

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initialize);
  } else {
    document.addEventListener("DOMContentLoaded", initialize);
  }
})();
