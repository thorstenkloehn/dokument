/*
 * Zensical rendert Mermaid-Diagramme in einen `attachShadow({mode:"closed"})`
 * hinein (siehe assets/javascripts/bundle.*.min.js). Ein closed Shadow Root
 * blockiert grundsätzlich jede externe CSS-Regel und jeden Zugriff via
 * `element.shadowRoot` – deshalb schrumpft die SVG auf schmalen Viewports
 * (Smartphones) auf Containerbreite, ohne dass sich das per extra.css
 * korrigieren ließe.
 *
 * Fix: `Element.prototype.attachShadow` wird abgefangen und erzwingt
 * `mode: "open"`, bevor Zensicals Bundle jemals einen Shadow Root anlegt.
 * Ein MutationObserver reicht anschließend in den (jetzt offenen) Shadow
 * Root hinein und hebt das erzwungene `width: 100%` der SVG auf, sodass
 * das Diagramm nie unter eine lesbare Mindestbreite schrumpft – der
 * Host-Div bekommt dafür über extra.css eine eigene Scrollleiste.
 */
(function () {
  "use strict";

  var nativeAttachShadow = Element.prototype.attachShadow;
  Element.prototype.attachShadow = function (init) {
    return nativeAttachShadow.call(this, Object.assign({}, init, { mode: "open" }));
  };

  var MIN_WIDTH_PX = 600;

  function fixSvg(svg) {
    if (!svg || svg.dataset.mermaidMobileFix === "done") return;
    svg.dataset.mermaidMobileFix = "done";
    svg.style.maxWidth = "none";
    svg.style.width = "auto";
    svg.style.minWidth = MIN_WIDTH_PX + "px";
  }

  function scanForMermaidHosts() {
    document.querySelectorAll(".mermaid").forEach(function (host) {
      if (host.shadowRoot) {
        fixSvg(host.shadowRoot.querySelector("svg"));
      }
    });
  }

  var observer = new MutationObserver(scanForMermaidHosts);
  observer.observe(document.documentElement, { childList: true, subtree: true });

  // Erstlauf, falls Diagramme schon vor dem Observer-Start gerendert wurden.
  scanForMermaidHosts();
})();
