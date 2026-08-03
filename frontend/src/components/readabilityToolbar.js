import { READABILITY_STORAGE_KEY } from "../config";

export function renderReadabilityToolbar() {
  return `
    <section class="toolbar">
      <div class="toggle-wrap">
        <button id="readability-toggle" class="radio-toggle" type="button" aria-label="Toggle readability mode">
          <span class="radio-icon" aria-hidden="true"></span>
          <span class="radio-text">Toggle me</span>
        </button>
      </div>
    </section>
  `;
}

function applyReadabilityMode(mode) {
  const isHighContrast = mode === "high-contrast";
  document.body.classList.toggle("high-contrast", isHighContrast);
  localStorage.setItem(READABILITY_STORAGE_KEY, mode);

  const button = document.querySelector("#readability-toggle");
  if (!button) return;
  button.classList.toggle("is-on", isHighContrast);
  button.setAttribute("aria-pressed", String(isHighContrast));
}

export function setupReadabilityToggle() {
  const button = document.querySelector("#readability-toggle");
  if (!button) return;

  const savedMode = localStorage.getItem(READABILITY_STORAGE_KEY) || "normal";
  applyReadabilityMode(savedMode);

  button.addEventListener("click", () => {
    const currentMode = document.body.classList.contains("high-contrast") ? "high-contrast" : "normal";
    const nextMode = currentMode === "normal" ? "high-contrast" : "normal";
    applyReadabilityMode(nextMode);
  });
}
