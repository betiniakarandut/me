import {
  fetchArticles,
  fetchCredentials,
  fetchExperience,
  fetchGithubRepos,
  fetchJourney,
  fetchProfile,
  fetchProjects,
  fetchSkills,
} from "../api/portfolioService";
import { setupContactForm } from "../components/contactForm";
import {
  renderArticles,
  renderBio,
  renderCredentials,
  renderExperience,
  renderGithub,
  renderJourney,
  renderProjects,
  renderSkills,
} from "../components/dataSections";
import { setupReadabilityToggle } from "../components/readabilityToolbar";
import { renderHomePage } from "./renderHomePage";

// Slot -> (request, renderer, label). Listed roughly in page priority; all
// requests start together and each slot renders as soon as its own data lands.
const SLOTS = [
  { name: "projects", load: fetchProjects, render: renderProjects, label: "projects" },
  { name: "experience", load: fetchExperience, render: renderExperience, label: "experience" },
  { name: "skills", load: fetchSkills, render: renderSkills, label: "skills" },
  { name: "articles", load: fetchArticles, render: renderArticles, label: "articles" },
  { name: "profile", load: fetchProfile, render: renderBio, label: "profile" },
  { name: "journey", load: fetchJourney, render: renderJourney, label: "journey" },
  { name: "credentials", load: fetchCredentials, render: renderCredentials, label: "certifications" },
];

// Optional, third-party-backed content: loaded only when scrolled near.
const LAZY_SLOTS = [{ name: "github", load: fetchGithubRepos, render: renderGithub, label: null }];

const failed = new Set();

function updateStatusBanner() {
  const banner = document.querySelector("#status-banner");
  if (!banner) return;
  if (!failed.size) {
    banner.hidden = true;
    return;
  }
  banner.hidden = false;
  banner.textContent = `Some live sections couldn't load (${[...failed].join(", ")}). Everything else on this page is unaffected.`;
}

function renderUnavailable(label) {
  return `<p class="muted empty-state">This section couldn't load${label ? ` its ${label}` : ""} right now. Please refresh in a moment.</p>`;
}

async function fillSlot({ name, load, render, label }) {
  const slot = document.querySelector(`[data-slot="${name}"]`);
  if (!slot) return;
  try {
    const data = await load();
    slot.innerHTML = render(data);
  } catch {
    if (label === null) {
      slot.innerHTML = render([]);
    } else {
      slot.innerHTML = renderUnavailable(label);
      failed.add(label);
      updateStatusBanner();
    }
  } finally {
    slot.removeAttribute("aria-busy");
  }
}

function observeLazySlots() {
  LAZY_SLOTS.forEach((config) => {
    const slot = document.querySelector(`[data-slot="${config.name}"]`);
    if (!slot) return;
    if (!("IntersectionObserver" in window)) {
      fillSlot(config);
      return;
    }
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries.some((entry) => entry.isIntersecting)) {
          observer.disconnect();
          fillSlot(config);
        }
      },
      { rootMargin: "600px 0px" }
    );
    observer.observe(slot);
  });
}

export function bootstrapApp(container) {
  renderHomePage(container);
  setupReadabilityToggle();
  setupContactForm();

  // A URL hash targets a section that only now exists in the DOM.
  if (window.location.hash) {
    document.querySelector(window.location.hash)?.scrollIntoView();
  }

  SLOTS.forEach((config) => fillSlot(config));
  observeLazySlots();
}
