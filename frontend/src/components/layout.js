import { EMAIL, NAV_LINKS, RESUME_URL, SOCIAL_LINKS } from "../content/links";
import { escapeHtml } from "../utils/format";
import {
  ICON_CODERLEGION,
  ICON_GITHUB,
  ICON_HASHNODE,
  ICON_LINKEDIN,
  ICON_X,
  ICON_YOUTUBE,
} from "./icons";
import { renderReadabilityToggle } from "./readabilityToolbar";

const ICONS = {
  linkedin: ICON_LINKEDIN,
  github: ICON_GITHUB,
  hashnode: ICON_HASHNODE,
  coderlegion: ICON_CODERLEGION,
  x: ICON_X,
  youtube: ICON_YOUTUBE,
};

export function renderNavbar() {
  return `
    <header class="side-nav card">
      <div class="nav-wrap">
        <a href="#home" class="brand-link">
          Betini Akarandut
          <span class="brand-role">Backend & Cloud Engineer</span>
        </a>
        <nav class="site-nav" aria-label="Main navigation">
          ${NAV_LINKS.map((link) => `<a href="${link.href}">${escapeHtml(link.label)}</a>`).join("")}
        </nav>
        <div class="nav-extras">
          <div class="network-icons" aria-label="Profiles">
            ${SOCIAL_LINKS.map(
              (link) =>
                `<a class="network-icon" href="${escapeHtml(link.url)}" target="_blank" rel="noopener noreferrer" aria-label="${escapeHtml(link.label)}">${ICONS[link.key]}</a>`
            ).join("")}
          </div>
          ${renderReadabilityToggle()}
        </div>
      </div>
    </header>
  `;
}

export function renderStatusBanner() {
  return `<div id="status-banner" class="status-banner" role="status" aria-live="polite" hidden></div>`;
}

export function renderSiteFooter() {
  return `
    <footer class="site-footer">
      <p class="footer-copy">© ${new Date().getFullYear()} Betini Akarandut · Backend & Cloud Engineer · Abuja, Nigeria</p>
      <div class="footer-actions">
        <a href="mailto:${EMAIL}">Email</a>
        <a href="${RESUME_URL}" target="_blank" rel="noopener">Resume (PDF)</a>
        ${SOCIAL_LINKS.map(
          (link) =>
            `<a href="${escapeHtml(link.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(link.label)}</a>`
        ).join("")}
      </div>
    </footer>
  `;
}
