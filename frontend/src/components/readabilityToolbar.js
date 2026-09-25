import { READABILITY_STORAGE_KEY } from "../config";

export function renderReadabilityToggle() {
  return `
    <button id="readability-toggle" class="radio-toggle" type="button" aria-pressed="false">
      <span class="radio-icon" aria-hidden="true"></span>
      <span class="radio-text">High contrast</span>
    </button>
  `;
}

function readSavedMode() {
  try {
    return localStorage.getItem(READABILITY_STORAGE_KEY) || "normal";
  } catch {
    return "normal";
  }
}

function applyReadabilityMode(mode) {
  const isHighContrast = mode === "high-contrast";
  document.body.classList.toggle("high-contrast", isHighContrast);
  try {
    localStorage.setItem(READABILITY_STORAGE_KEY, mode);
  } catch {
    // Storage unavailable (private mode, blocked site data): the toggle still works for this visit.
  }

  const button = document.querySelector("#readability-toggle");
  if (!button) return;
  button.classList.toggle("is-on", isHighContrast);
  button.setAttribute("aria-pressed", String(isHighContrast));
}

export function setupReadabilityToggle() {
  const button = document.querySelector("#readability-toggle");
  if (!button) return;

  applyReadabilityMode(readSavedMode());

  button.addEventListener("click", () => {
    const nextMode = document.body.classList.contains("high-contrast") ? "normal" : "high-contrast";
    applyReadabilityMode(nextMode);
  });
}
