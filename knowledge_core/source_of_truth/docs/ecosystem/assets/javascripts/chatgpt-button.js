(function () {
  const BUTTON_ID = "chatgpt-open-button";
  const CHATGPT_URL = "https://chatgpt.com/";
  const TOAST_VISIBLE_MS = 1200;

  const DEFAULT_PROMPT_TEMPLATES = {
    ru: "Прочитай <CURRENT_PAGE_URL> и отвечай на вопросы о содержимом.",
    en: "Read <CURRENT_PAGE_URL> and answer questions about the content.",
  };

  const getLanguageFromUrl = () => {
    const path = window.location.pathname.toLowerCase();
    if (path.includes("/ru/")) {
      return "ru";
    }
    if (path.includes("/en/")) {
      return "en";
    }
    return "";
  };

  const getPageLanguage = () => {
    const urlLanguage = getLanguageFromUrl();
    if (urlLanguage) {
      document.documentElement.lang = urlLanguage;
      return urlLanguage;
    }

    const langAttribute = document.documentElement.lang?.trim();
    if (langAttribute) {
      return langAttribute.split("-")[0].toLowerCase();
    }

    return "en";
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

  const getFeedbackMessages = () => {
    const language = getPageLanguage();
    if (language === "ru") {
      return {
        success: "Скопировано!",
        failure: "Ошибка копирования",
        toast: "Скопировано ✅",
      };
    }
    return {
      success: "Copied!",
      failure: "Copy failed",
      toast: "Copied ✅",
    };
  };

  const buildChatGptUrl = (prompt) => `${CHATGPT_URL}?prompt=${encodeURIComponent(prompt)}`;

  const removeToast = () => {
    const existingToast = document.querySelector(".chatgpt-toast");
    if (existingToast) {
      existingToast.remove();
    }
  };

  const showToast = (message) => {
    removeToast();

    const toast = document.createElement("div");
    toast.className = "chatgpt-toast";
    toast.textContent = message;
    document.body.appendChild(toast);

    window.setTimeout(() => {
      if (toast.parentNode) {
        toast.remove();
      }
    }, TOAST_VISIBLE_MS);
  };

  const setFeedback = (button, message, delay, toastMessage) => {
    if (!button.dataset.chatgptLabel) {
      button.dataset.chatgptLabel = button.textContent.trim() || "Open in ChatGPT";
    }
    button.textContent = message;

    if (toastMessage) {
      showToast(toastMessage);
    }

    window.setTimeout(() => {
      button.textContent = button.dataset.chatgptLabel;
    }, delay);
  };

  const updateButtonHref = (button) => {
    const prompt = buildPrompt(window.location.href);
    button.href = buildChatGptUrl(prompt);
  };

  const ensureButton = () => {
    const button = document.getElementById(BUTTON_ID);
    if (!button) {
      return;
    }

    updateButtonHref(button);

    if (!button.dataset.chatgptLabel) {
      button.dataset.chatgptLabel = button.textContent.trim() || "Open in ChatGPT";
    }

    if (button.dataset.chatgptBound === "true") {
      return;
    }

    button.dataset.chatgptBound = "true";

    ["mouseenter", "focus", "contextmenu"].forEach((eventName) => {
      button.addEventListener(eventName, () => updateButtonHref(button));
    });

    button.addEventListener("click", async (event) => {
      event.preventDefault();
      const prompt = buildPrompt(window.location.href);
      const chatGptUrl = buildChatGptUrl(prompt);
      button.href = chatGptUrl;
      const feedback = getFeedbackMessages();

      let copied = false;
      try {
        await copyPrompt(prompt);
        copied = true;
        setFeedback(button, feedback.success, 1000, feedback.toast);
      } catch (error) {
        console.warn("Не удалось скопировать prompt в буфер обмена.", error);
        setFeedback(button, feedback.failure, 1200);
      }

      window.open(chatGptUrl, "_blank", "noopener");

      if (!copied) {
        try {
          await copyPrompt(prompt);
          setFeedback(button, feedback.success, 1000, feedback.toast);
        } catch (secondError) {
          console.warn("Повторная попытка копирования prompt завершилась неудачей.", secondError);
        }
      }
    });
  };

  const initialize = () => {
    ensureButton();

    const button = document.getElementById(BUTTON_ID);
    if (button && button.dataset.chatgptBound !== "true") {
      console.warn("ChatGPT button handler was not bound. Href fallback remains active.");
      updateButtonHref(button);
    }
  };

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initialize);
  } else {
    document.addEventListener("DOMContentLoaded", initialize);
  }
})();
