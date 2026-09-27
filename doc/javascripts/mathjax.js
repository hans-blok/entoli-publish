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
  svg: {
    fontCache: "none"
  },
  startup: {
    typeset: false,
    ready() {
      MathJax.startup.defaultReady();
      // Wait for startup, then render once per Material page event.
      // Keep our queue separate from MathJax's own startup promise.
      MathJax.startup.promise.then(() => {
        let pending = Promise.resolve();
        document$.subscribe(() => {
          pending = pending.then(() => {
            MathJax.typesetClear();
            MathJax.texReset();
            return MathJax.typesetPromise();
          }).catch(error => console.error("MathJax typesetting failed", error));
        });
      });
    }
  }
};
