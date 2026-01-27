(function () {
  const BUTTON_CLASS = "chatgpt-action";
  const BUTTON_ID = "chatgpt-open-button";
  const CHATGPT_URL = "https://chat.openai.com/";

  const getPromptTemplate = () => {
    if (typeof window.chatgptPromptTemplate === "string" && window.chatgptPromptTemplate.trim()) {
      return window.chatgptPromptTemplate;
    }
    return "Read <CURRENT_PAGE_URL> and answer questions about the content.";
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

  const ensureButton = () => {
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

    button.addEventListener("click", async (event) => {
      event.preventDefault();
      const url = window.location.href;
      const prompt = buildPrompt(url);

      try {
        await copyPrompt(prompt);
        setFeedback("Copied!", 1000);
      } catch (error) {
        console.warn("Не удалось скопировать prompt в буфер обмена.", error);
        setFeedback("Copy failed", 1200);
      }

      window.open(CHATGPT_URL, "_blank", "noopener");
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
