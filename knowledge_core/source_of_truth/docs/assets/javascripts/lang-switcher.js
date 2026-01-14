(() => {
  const header = document.querySelector('.md-header__inner');
  if (!header || header.querySelector('.language-switcher')) {
    return;
  }

  const path = window.location.pathname;
  const markers = ['/ecosystem/', '/publications/', '/index.html'];
  let basePath = '/';

  for (const marker of markers) {
    if (path.includes(marker)) {
      basePath = `${path.split(marker)[0]}/`;
      break;
    }
  }

  if (basePath === '//') {
    basePath = '/';
  }

  const ruUrl = basePath;
  const enUrl = `${basePath}ecosystem/en/`;

  const container = document.createElement('div');
  container.className = 'language-switcher';
  container.innerHTML = `
    <details class="language-switcher__menu">
      <summary class="language-switcher__summary" aria-label="Переключить язык сайта">
        Language
      </summary>
      <div class="language-switcher__list">
        <a class="language-switcher__link" href="${ruUrl}">Русский</a>
        <a class="language-switcher__link" href="${enUrl}">English</a>
        <span class="language-switcher__hint">Другие языки — скоро</span>
      </div>
    </details>
  `;

  const search = header.querySelector('.md-search');
  if (search?.parentNode) {
    search.parentNode.insertBefore(container, search.nextSibling);
  } else {
    header.appendChild(container);
  }
})();
