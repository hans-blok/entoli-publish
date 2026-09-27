window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  startup: {
    ready() {
      MathJax.startup.defaultReady();
      // Material's instant navigation replaces the page without reloading JS.
      document$.subscribe(() => {
        MathJax.startup.promise = MathJax.startup.promise.then(() => {
          MathJax.typesetClear();
          MathJax.texReset();
          return MathJax.typesetPromise();
        }).catch(error => console.error("MathJax typesetting failed", error));
      });
    }
  }
};
