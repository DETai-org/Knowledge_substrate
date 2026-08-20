mermaid.initialize({
  startOnLoad: false,
  securityLevel: "strict",
});

let mermaidDiagramIndex = 0;

document$.subscribe(async () => {
  const sources = document.querySelectorAll("pre.mermaid-source");

  for (const source of sources) {
    const diagramId = `mermaid-diagram-${mermaidDiagramIndex++}`;
    const { svg } = await mermaid.render(diagramId, source.textContent);
    const diagram = document.createElement("div");
    diagram.className = "mermaid-diagram";
    diagram.innerHTML = svg;
    source.replaceWith(diagram);
  }
});
