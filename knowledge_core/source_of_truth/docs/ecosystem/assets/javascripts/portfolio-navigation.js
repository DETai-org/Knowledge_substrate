/* Resolve menu targets so echelon badges also survive relative self-links (./). */
(function () {
  "use strict";

  var echelons = {
    "francis-galton": "E1",
    "psykhe-ai": "E1",
    "website": "E2",
    "psychology-in-quotes": "E2",
    "storytelling": "E2",
    "telegram": "E2",
    "infrastructure-foundation": "E3"
  };

  function decorate() {
    document.querySelectorAll(".md-nav--primary a[href]").forEach(function (link) {
      var path = new URL(link.getAttribute("href"), document.baseURI).pathname;
      var match = path.match(/\/technology\/platform\/([^/]+)\/$/);
      var echelon = match && echelons[match[1]];
      if (echelon) link.dataset.detaiEchelon = echelon;
      else delete link.dataset.detaiEchelon;
    });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(decorate);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", decorate);
  } else {
    decorate();
  }
})();
