import { escapeHtml } from "../utils/format";

export function renderSection({ id, eyebrow, title, intro = "", body, className = "" }) {
  const headingId = `${id}-title`;
  return `
    <section id="${id}" class="card section-panel ${className}" aria-labelledby="${headingId}">
      ${eyebrow ? `<p class="section-eyebrow">${escapeHtml(eyebrow)}</p>` : ""}
      <h2 id="${headingId}">${escapeHtml(title)}</h2>
      ${intro ? `<p class="section-intro">${escapeHtml(intro)}</p>` : ""}
      ${body}
    </section>
  `;
}

/** Placeholder for a section filled in by an API call; see app/bootstrap.js. */
export function renderSlot(name, lines = 3) {
  const skeleton = Array.from({ length: lines }, () => `<span class="skeleton-line"></span>`).join("");
  return `<div class="slot" data-slot="${name}" aria-busy="true"><div class="skeleton" aria-hidden="true">${skeleton}</div><span class="visually-hidden">Loading…</span></div>`;
}

export function renderEmptyState(message) {
  return `<p class="muted empty-state">${escapeHtml(message)}</p>`;
}

export function renderChips(items, className = "chips") {
  return `<div class="${className}">${items.map((item) => `<span>${escapeHtml(item)}</span>`).join("")}</div>`;
}

export function renderMetrics(metrics, className = "metrics-grid") {
  return `
    <div class="${className}">
      ${metrics
        .map(
          (metric) => `
            <div class="metric">
              <p class="metric-value">${escapeHtml(metric.value)}</p>
              <p class="metric-label">${escapeHtml(metric.label)}</p>
            </div>
          `
        )
        .join("")}
    </div>
  `;
}

/** Linear process: horizontal on wide screens, vertical on narrow ones. */
export function renderFlow(steps, { label = "" } = {}) {
  return `
    <ol class="flow" ${label ? `aria-label="${escapeHtml(label)}"` : ""}>
      ${steps
        .map((step) => {
          const title = typeof step === "string" ? step : step.title;
          const note = typeof step === "string" ? "" : step.note || "";
          return `
            <li class="flow-step">
              <span class="flow-step-title">${escapeHtml(title)}</span>
              ${note ? `<span class="flow-step-note">${escapeHtml(note)}</span>` : ""}
            </li>
          `;
        })
        .join("")}
    </ol>
  `;
}

/** Layered architecture diagram: each layer is a labelled row of components. */
export function renderDiagram({ title, layers, caption = "" }) {
  return `
    <figure class="diagram">
      ${title ? `<figcaption class="diagram-title">${escapeHtml(title)}</figcaption>` : ""}
      <div class="diagram-layers">
        ${layers
          .map(
            (layer) => `
              <div class="diagram-layer">
                <p class="diagram-layer-label">${escapeHtml(layer.label)}</p>
                <ul class="diagram-nodes">
                  ${layer.nodes
                    .map((node) => {
                      const name = typeof node === "string" ? node : node.name;
                      const detail = typeof node === "string" ? "" : node.detail || "";
                      return `<li class="diagram-node">${escapeHtml(name)}${
                        detail ? `<span class="diagram-node-detail">${escapeHtml(detail)}</span>` : ""
                      }</li>`;
                    })
                    .join("")}
                </ul>
              </div>
            `
          )
          .join("")}
      </div>
      ${caption ? `<p class="diagram-caption">${escapeHtml(caption)}</p>` : ""}
    </figure>
  `;
}

/** Labelled steps (Observation / Investigation / ... or Challenge / Approach / ...). */
export function renderSteps(steps) {
  return `
    <dl class="steps">
      ${steps
        .map(
          (step) => `
            <div class="step">
              <dt class="step-label">${escapeHtml(step.label)}</dt>
              <dd>${
                Array.isArray(step.body)
                  ? `<ul>${step.body.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>`
                  : `<p>${escapeHtml(step.body)}</p>`
              }</dd>
            </div>
          `
        )
        .join("")}
    </dl>
  `;
}

export function renderList(items, className = "bullet-list") {
  return `<ul class="${className}">${items.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>`;
}
