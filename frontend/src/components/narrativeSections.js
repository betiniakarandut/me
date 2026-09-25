// Sections rendered from static content modules. They paint immediately and
// never depend on the API, so the core story survives a backend outage.
import { ARCHITECTURE, HERO, IMPACT, PRINCIPLES, PRODUCTION_ENGINEERING, THIS_SITE } from "../content/engineering";
import { LEADERSHIP_INTRO, LEADERSHIP_ITEMS, LEARNING_EVENT, PITCH_CHALLENGE } from "../content/leadership";
import { RESUME_URL } from "../content/links";
import { TRACTRAC } from "../content/tractrac";
import { escapeHtml } from "../utils/format";
import {
  renderChips,
  renderDiagram,
  renderFlow,
  renderList,
  renderMetrics,
  renderSection,
  renderSteps,
} from "./ui";

const HERO_MOTIF = `
  <svg class="hero-motif" viewBox="0 0 220 200" aria-hidden="true" focusable="false">
    <circle cx="40" cy="40" r="14"></circle>
    <circle cx="150" cy="30" r="10"></circle>
    <circle cx="185" cy="110" r="16"></circle>
    <circle cx="90" cy="150" r="12"></circle>
    <circle cx="30" cy="140" r="9"></circle>
    <path d="M40 40 L150 30" />
    <path d="M150 30 L185 110" />
    <path d="M40 40 L90 150" />
    <path d="M90 150 L185 110" />
    <path d="M30 140 L90 150" />
  </svg>
`;

export function renderHeroSection() {
  return `
    <section id="home" class="hero card" aria-labelledby="home-title">
      ${HERO_MOTIF}
      <div class="hero-grid">
        <div class="hero-copy">
          <p class="kicker">${escapeHtml(HERO.title)}</p>
          <h1 id="home-title">${escapeHtml(HERO.name)}</h1>
          <p class="lead">${escapeHtml(HERO.lead)}</p>
          <ul class="hero-proof" aria-label="Areas of work">
            ${HERO.proof.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}
          </ul>
          <div class="hero-actions">
            <a class="button button-primary" href="#systems">Explore Systems</a>
            <a class="button button-secondary" href="${RESUME_URL}" target="_blank" rel="noopener">Download Resume</a>
          </div>
          <p class="hero-current">${escapeHtml(HERO.current)}</p>
        </div>
        <img class="hero-avatar" src="${escapeHtml(HERO.avatar)}" alt="Portrait of ${escapeHtml(HERO.name)}" width="160" height="160" />
      </div>
    </section>
  `;
}

export function renderImpactSection() {
  return renderSection({
    id: "impact",
    eyebrow: "Engineering Impact",
    title: "Production scale, stated plainly",
    body: `${renderMetrics(IMPACT.metrics)}<p class="fine-print">${escapeHtml(IMPACT.note)}</p>`,
  });
}

function renderSubsection(id, title, body) {
  return `
    <div class="subsection" ${id ? `id="${id}"` : ""}>
      <h3>${escapeHtml(title)}</h3>
      ${body}
    </div>
  `;
}

export function renderTracTracCaseStudy() {
  const t = TRACTRAC;
  const context = `
    <dl class="context-grid">
      ${t.context
        .map(
          (item) => `
            <div>
              <dt>${escapeHtml(item.label)}</dt>
              <dd>${escapeHtml(item.value)}</dd>
            </div>
          `
        )
        .join("")}
    </dl>
  `;

  const body = `
    <p class="prose-lead">${escapeHtml(t.intro)}</p>
    ${context}
    ${renderSubsection("", "The engineering problem", renderList(t.constraints))}
    ${renderSubsection("tractrac-architecture", "Platform architecture", renderDiagram(t.architecture))}
    ${renderSubsection(
      "tractrac-offline",
      "Offline-first field workflow",
      `
        ${renderFlow(t.offline.flow, { label: "Offline-first synchronisation flow" })}
        <div class="two-col">
          <div>
            <p class="label">What the design guarantees</p>
            ${renderList(t.offline.guarantees)}
          </div>
          <div>
            <p class="label">Trade-off</p>
            <p class="muted">${escapeHtml(t.offline.tradeoff)}</p>
            <p class="label">Outcome</p>
            <p class="muted">${escapeHtml(t.offline.outcome)}</p>
          </div>
        </div>
      `
    )}
    <div class="two-col">
      ${renderSubsection("", "Field intelligence: GPS & geospatial", renderList(t.geospatial))}
      ${renderSubsection("", "Payments & reconciliation", renderList(t.payments))}
    </div>
    ${renderSubsection(
      "tractrac-incident",
      "Production incident: one screen, 60+ requests",
      renderSteps(t.incident)
    )}
    ${renderSubsection("", "Infrastructure I operate", renderList(t.infrastructure))}
    ${renderSubsection(
      "",
      "From technology to outcomes",
      `<p class="muted">${escapeHtml(t.dataStory)}</p>${renderFlow(t.outcomesChain, { label: "Technology to outcomes" })}`
    )}
    ${renderSubsection(
      "tractrac-programme",
      "Programme context: ISSAM",
      `
        <p class="muted">${escapeHtml(t.programme.intro)}</p>
        <p class="label">Recorded on the platform</p>
        ${renderMetrics(t.programme.platform, "metrics-grid metrics-compact")}
        <p class="label">Programme outcomes</p>
        ${renderMetrics(t.programme.programme, "metrics-grid metrics-compact")}
        <p class="fine-print">${escapeHtml(t.programme.inclusion)}</p>
        <p class="fine-print">${escapeHtml(t.programme.ecosystem)}</p>
      `
    )}
    <div class="subsection">
      <p class="label">Technologies</p>
      ${renderChips(t.stack, "project-tech")}
    </div>
  `;

  return renderSection({
    id: "tractrac",
    eyebrow: "Case Study · TracTrac",
    title: "Backend infrastructure for agricultural mechanisation in the field",
    body,
    className: "case-study",
  });
}

export function renderArchitectureSection() {
  const a = ARCHITECTURE;
  const body = `
    <div class="architecture-grid">
      ${renderDiagram(a.diagnostics)}
      <div class="diagram">
        <p class="diagram-title">SolarAfRiC: booking and payment lifecycle</p>
        ${renderFlow(a.bookingFlow, { label: "Booking and payment lifecycle" })}
        <p class="diagram-caption">${escapeHtml(a.bookingNote)}</p>
      </div>
      <div class="two-col">
        <div class="diagram">
          <p class="diagram-title">SolarAfRiC: resilient file storage</p>
          ${renderFlow(a.storageFlow, { label: "Storage fallback chain" })}
        </div>
        <div class="diagram">
          <p class="diagram-title">VITAL 2: bulk data and campaigns</p>
          ${renderFlow(a.importFlow, { label: "Bulk import flow" })}
          ${renderFlow(a.voucherFlow, { label: "Voucher campaign flow" })}
        </div>
      </div>
    </div>
  `;
  return renderSection({
    id: "architecture",
    eyebrow: "Architecture",
    title: "How the other systems are put together",
    intro: "Conceptual diagrams of real components. Each shows only what that system actually uses.",
    body,
  });
}

export function renderProductionEngineeringSection() {
  const body = `
    <div class="capability-grid">
      ${PRODUCTION_ENGINEERING.map(
        (group) => `
          <article class="capability">
            <h3>${escapeHtml(group.title)}</h3>
            ${renderList(group.items)}
          </article>
        `
      ).join("")}
    </div>
    <p class="fine-print">${escapeHtml(THIS_SITE)}</p>
  `;
  return renderSection({
    id: "engineering",
    eyebrow: "Production Engineering",
    title: "What happens after the code is written",
    body,
  });
}

export function renderLeadershipSection() {
  const le = LEARNING_EVENT;
  const pc = PITCH_CHALLENGE;
  const body = `
    <div class="leadership-grid">
      ${LEADERSHIP_ITEMS.map(
        (item) => `
          <article class="leadership-card">
            <p class="card-kind">${escapeHtml(item.kind)}</p>
            <h3>${escapeHtml(item.title)}</h3>
            <p class="muted">${escapeHtml(item.body)}</p>
            ${item.link ? `<a class="text-link" href="${item.link.href}">${escapeHtml(item.link.label)} →</a>` : ""}
          </article>
        `
      ).join("")}
    </div>

    <article class="feature-card" id="pitch-challenge">
      <p class="card-kind">${escapeHtml(pc.kind)}</p>
      <h3>${escapeHtml(pc.title)}</h3>
      <p class="feature-role">${escapeHtml(pc.role)}</p>
      <p class="muted">${escapeHtml(pc.summary)} ${escapeHtml(pc.context)}</p>
      <blockquote class="pull-quote">
        <p><span class="label">Theme</span>${escapeHtml(pc.theme)}</p>
        <p><span class="label">Challenge question</span>${escapeHtml(pc.question)}</p>
      </blockquote>
      <div class="two-col">
        <div>
          <p class="label">Who could apply</p>
          ${renderList(pc.eligibility)}
        </div>
        <div>
          <p class="label">What I led</p>
          ${renderList(pc.scope)}
        </div>
      </div>
      <p class="label">Delivery process</p>
      ${renderFlow(pc.process, { label: "Pitch challenge delivery process" })}
      <p class="label">Prize structure</p>
      ${renderMetrics(pc.prizes, "metrics-grid metrics-compact")}
      <p class="fine-print">${escapeHtml(pc.prizeNote)}</p>
    </article>

    <article class="feature-card" id="learning-event">
      <p class="card-kind">${escapeHtml(le.kind)}</p>
      <h3>${escapeHtml(le.title)}</h3>
      <p class="muted">${escapeHtml(le.body)}</p>
      <p class="label">Narrative structure</p>
      ${renderFlow(le.structure, { label: "Explainer narrative structure" })}
      <div class="two-col">
        <div>
          <p class="label">What it explains</p>
          ${renderList(le.covered)}
        </div>
        <div>
          <p class="label">Format</p>
          <p class="muted">${escapeHtml(le.format)}</p>
        </div>
      </div>
    </article>
  `;
  return renderSection({
    id: "leadership",
    eyebrow: "Technical Leadership",
    title: "Ownership beyond the code",
    intro: LEADERSHIP_INTRO,
    body,
  });
}

export function renderPrinciplesSection() {
  const body = `
    <ol class="principles">
      ${PRINCIPLES.map(
        (item) => `
          <li>
            <h3>${escapeHtml(item.title)}</h3>
            <p>${escapeHtml(item.body)}</p>
          </li>
        `
      ).join("")}
    </ol>
  `;
  return renderSection({ id: "how-i-engineer", eyebrow: "How I Engineer", title: "Working principles", body });
}
