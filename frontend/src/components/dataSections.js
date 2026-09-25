// Sections backed by API data. Each exports a shell (rendered immediately with
// loading slots) and fill functions that render one API response into a slot.
import { formatDateRange, formatEventDate, escapeHtml, renderParagraphs } from "../utils/format";
import { renderChips, renderEmptyState, renderSection, renderSlot } from "./ui";

const CASE_STUDY_LINKS = {
  "tractrac-platform": { href: "#tractrac", label: "Read the TracTrac case study" },
  "solarafric-platform": { href: "#architecture", label: "See the SolarAfRiC architecture" },
};

const SKILL_GROUP_ORDER = [
  "Backend",
  "Data",
  "Distributed Systems",
  "Cloud & DevOps",
  "Payments",
  "Geospatial",
  "Applied AI",
  "Integrations",
  "Frontend",
];
const SUPPORTING_SKILL_GROUPS = new Set(["Frontend"]);

const CREDENTIAL_GROUPS = [
  { key: "certification", title: "Certifications" },
  { key: "scholarship", title: "Scholarships" },
  { key: "award", title: "Awards" },
];

function splitTech(techStack) {
  return String(techStack || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function renderMeta(label, text) {
  if (!text) return "";
  return `
    <div>
      <p class="project-meta-label">${escapeHtml(label)}</p>
      <p class="project-meta-text">${escapeHtml(text)}</p>
    </div>
  `;
}

function renderExternalLinks(project) {
  const links = [];
  if (project.repo_url) links.push(`<a class="text-link" href="${escapeHtml(project.repo_url)}" target="_blank" rel="noopener noreferrer">Repository</a>`);
  if (project.live_url) links.push(`<a class="text-link" href="${escapeHtml(project.live_url)}" target="_blank" rel="noopener noreferrer">Live</a>`);
  return links.join("");
}

// ── Selected systems ────────────────────────────────────────────
export function renderSystemsShell() {
  return renderSection({
    id: "systems",
    eyebrow: "Selected Systems",
    title: "Production systems I've engineered",
    intro: "Each one solved a real operational constraint. TracTrac and SolarAfRiC carry the deepest architecture work.",
    body: renderSlot("projects", 6),
  });
}

export function renderProjects(projects) {
  const featured = projects.filter((project) => project.featured);
  const other = projects.filter((project) => !project.featured);
  if (!featured.length && !other.length) return renderEmptyState("No projects found.");

  const featuredMarkup = featured
    .map((project, index) => {
      const caseStudy = CASE_STUDY_LINKS[project.slug];
      return `
        <article class="project-card${index < 2 ? " project-card-featured" : ""}">
          <h3>${escapeHtml(project.title)}</h3>
          <p class="project-summary">${escapeHtml(project.summary)}</p>
          ${project.facts?.length ? renderChips(project.facts, "fact-row") : ""}
          <div class="project-meta">
            ${renderMeta("Engineering challenge", project.challenge)}
            ${renderMeta("What I engineered", project.engineered)}
            ${renderMeta("Impact", project.impact)}
          </div>
          <div>
            <p class="project-meta-label">Technology</p>
            ${renderChips(splitTech(project.tech_stack), "project-tech")}
          </div>
          <div class="card-links">
            ${caseStudy ? `<a class="text-link" href="${caseStudy.href}">${escapeHtml(caseStudy.label)} →</a>` : ""}
            ${renderExternalLinks(project)}
          </div>
        </article>
      `;
    })
    .join("");

  const otherMarkup = other.length
    ? `
      <details class="other-work">
        <summary>Earlier and smaller projects (${other.length})</summary>
        <ul class="other-work-list">
          ${other
            .map(
              (project) => `
                <li>
                  <p class="other-work-title">${escapeHtml(project.title)}</p>
                  <p class="muted">${escapeHtml(project.summary)}</p>
                  <p class="other-work-tech">${escapeHtml(project.tech_stack)}</p>
                  <div class="card-links">${renderExternalLinks(project)}</div>
                </li>
              `
            )
            .join("")}
        </ul>
      </details>
    `
    : "";

  return `<div class="projects-grid">${featuredMarkup}</div>${otherMarkup}`;
}

// ── Experience ──────────────────────────────────────────────────
export function renderExperienceShell() {
  return renderSection({
    id: "experience",
    eyebrow: "Experience",
    title: "Where I've done the work",
    body: `
      ${renderSlot("experience", 8)}
      <p class="background-note">
        Earlier: Chemical Engineering → AWS ML Foundations (Udacity) and Zero To Mastery web development →
        a backend internship at Scoplex Technologies, research work with Extern, and community
        contribution with United People Global.
      </p>
    `,
  });
}

// Roles shown expanded; older ones collapse under "Earlier roles".
const EXPANDED_ROLES = 4;

export function renderExperience(experience) {
  if (!experience.length) return renderEmptyState("No experience records found.");
  const recent = experience.slice(0, EXPANDED_ROLES);
  const earlier = experience.slice(EXPANDED_ROLES);
  return `
    ${renderExperienceList(recent)}
    ${
      earlier.length
        ? `<details class="other-work earlier-roles">
            <summary>Earlier roles (${earlier.length}): ${escapeHtml(earlier.map((item) => item.company).join(", "))}</summary>
            ${renderExperienceList(earlier)}
          </details>`
        : ""
    }
  `;
}

function renderExperienceList(items) {
  return `
    <ol class="experience-list">
      ${items
        .map(
          (item) => `
            <li class="experience-item">
              <div class="experience-head">
                <div>
                  <h3>${escapeHtml(item.role)}</h3>
                  <p class="experience-company">${escapeHtml(item.company)}</p>
                </div>
                <p class="experience-when">
                  <span>${escapeHtml(formatDateRange(item.start_date, item.end_date, item.is_current))}</span>
                  <span>${escapeHtml(item.location)}</span>
                </p>
              </div>
              <p class="muted">${escapeHtml(item.summary)}</p>
              ${
                item.highlights?.length
                  ? `<ul class="bullet-list">${item.highlights.map((h) => `<li>${escapeHtml(h)}</li>`).join("")}</ul>`
                  : ""
              }
            </li>
          `
        )
        .join("")}
    </ol>
  `;
}

// ── Technical stack ─────────────────────────────────────────────
export function renderStackShell() {
  return renderSection({
    id: "stack",
    eyebrow: "Technical Stack",
    title: "Capabilities, grouped by what they do",
    body: renderSlot("skills", 4),
  });
}

export function renderSkills(skills) {
  if (!skills.length) return renderEmptyState("Skill data is currently unavailable.");
  const grouped = new Map();
  skills.forEach((skill) => {
    const category = skill.category || "Other";
    if (!grouped.has(category)) grouped.set(category, []);
    grouped.get(category).push(skill.name);
  });
  const ordered = [
    ...SKILL_GROUP_ORDER.filter((category) => grouped.has(category)),
    ...[...grouped.keys()].filter((category) => !SKILL_GROUP_ORDER.includes(category)),
  ];
  return `
    <div class="skills-groups">
      ${ordered
        .map(
          (category) => `
            <div class="skill-group${SUPPORTING_SKILL_GROUPS.has(category) ? " is-supporting" : ""}">
              <h3 class="skill-group-title">${escapeHtml(category)}</h3>
              ${renderChips(grouped.get(category))}
            </div>
          `
        )
        .join("")}
    </div>
  `;
}

// ── Writing & GitHub ────────────────────────────────────────────
export function renderWritingShell() {
  return renderSection({
    id: "writing",
    eyebrow: "Writing & Open Source",
    title: "Writing on production systems and engineering decisions",
    body: `
      ${renderSlot("articles", 4)}
      <div class="subsection" id="github">
        <h3>Recent GitHub repositories</h3>
        <div class="slot" data-slot="github" data-lazy="true" aria-busy="true">
          <p class="muted empty-state">Repositories load when you scroll here.</p>
        </div>
      </div>
    `,
  });
}

export function renderArticles(articles) {
  if (!articles.length) return renderEmptyState("No articles found.");
  return `
    <ul class="article-list">
      ${articles
        .map(
          (article) => `
            <li class="article-item">
              <p class="article-date">${escapeHtml(formatEventDate(article.published_at))} · ${escapeHtml(article.source)}</p>
              <h3><a href="${escapeHtml(article.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(article.title)}</a></h3>
              <p class="muted">${escapeHtml(article.excerpt)}</p>
            </li>
          `
        )
        .join("")}
    </ul>
  `;
}

export function renderGithub(repositories) {
  if (!repositories.length) {
    return renderEmptyState("GitHub is unavailable right now. See github.com/betiniakarandut.");
  }
  return `
    <ul class="repo-list">
      ${repositories
        .map(
          (repo) => `
            <li class="repo-item">
              <a href="${escapeHtml(repo.html_url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(repo.name)}</a>
              <p class="muted">${escapeHtml(repo.description || "No description provided.")}</p>
              <p class="repo-meta">${escapeHtml(repo.language)} · ★ ${escapeHtml(repo.stargazers_count)}</p>
            </li>
          `
        )
        .join("")}
    </ul>
  `;
}

// ── About ───────────────────────────────────────────────────────
export function renderAboutShell() {
  return renderSection({
    id: "about",
    eyebrow: "About",
    title: "How I got here",
    body: `
      <div class="about-grid">
        <div class="prose">
          ${renderSlot("profile", 5)}
          <p class="fine-print">Outside work: volunteer with the Clean Sweep Community in Abuja: community cleanups and advocating for practical waste-bin solutions.</p>
        </div>
        <div>
          <h3 class="about-subtitle">Path</h3>
          ${renderSlot("journey", 6)}
        </div>
      </div>
    `,
  });
}

export function renderBio(profile) {
  if (!profile?.bio) return renderEmptyState("Profile information is currently unavailable.");
  return renderParagraphs(profile.bio);
}

export function renderJourney(journey) {
  if (!journey.length) return renderEmptyState("No journey records found.");
  return `
    <ol class="timeline">
      ${journey
        .map(
          (item) => `
            <li class="timeline-item">
              <p class="event-date">${escapeHtml(formatEventDate(item.event_date))}</p>
              <p class="timeline-title">${escapeHtml(item.title)}</p>
              <p class="timeline-text">${escapeHtml(item.description)}</p>
            </li>
          `
        )
        .join("")}
    </ol>
  `;
}

// ── Certifications & awards ─────────────────────────────────────
export function renderCredentialsShell() {
  return renderSection({
    id: "credentials",
    eyebrow: "Credentials",
    title: "Certifications & Awards",
    body: renderSlot("credentials", 3),
  });
}

export function renderCredentials(items) {
  if (!items.length) return renderEmptyState("No certifications found.");
  const groups = CREDENTIAL_GROUPS.map((group) => ({
    ...group,
    items: items.filter((item) => (item.category || "certification") === group.key),
  })).filter((group) => group.items.length);
  return `
    <div class="credential-groups">
      ${groups
        .map(
          (group) => `
            <div>
              <h3 class="skill-group-title">${escapeHtml(group.title)}</h3>
              <ul class="credential-list">
                ${group.items
                  .map(
                    (item) => `
                      <li>
                        <span class="credential-name">${escapeHtml(item.name)}</span>
                        <span class="credential-meta">${escapeHtml(item.issuer)} · ${escapeHtml(item.year)}</span>
                      </li>
                    `
                  )
                  .join("")}
              </ul>
            </div>
          `
        )
        .join("")}
    </div>
  `;
}
