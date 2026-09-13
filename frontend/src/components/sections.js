import { escapeHtml, formatEventDate, renderParagraphs } from "../utils/format";

function renderEmptyState(message) {
  return `<p class="muted empty-state">${escapeHtml(message)}</p>`;
}

function resolveAvatarUrl(profile) {
  const fallback = "https://github.com/betiniakarandut.png";
  const githubUrl = profile?.github_url;
  if (!githubUrl) return fallback;

  try {
    const url = new URL(githubUrl);
    const parts = url.pathname.split("/").filter(Boolean);
    const username = parts[0];
    if (!username) return fallback;
    return `https://github.com/${username}.png`;
  } catch {
    return fallback;
  }
}

const HERO_MOTIF = `
  <svg class="hero-motif" viewBox="0 0 220 200" aria-hidden="true">
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

export function renderHeroSection(profile, skills) {
  if (!profile) {
    return `
      <section class="hero card section-panel">
        <h1>Portfolio Data Unavailable</h1>
        ${renderEmptyState("The backend profile endpoint is currently unavailable.")}
      </section>
    `;
  }

  const skillMarkup = skills.length
    ? skills
        .slice(0, 8)
        .map((skill) => `<span>${escapeHtml(skill.name)}</span>`)
        .join("")
    : `<span>Backend Engineering</span>`;
  const avatarUrl = resolveAvatarUrl(profile);

  return `
    <section class="hero-stage section-panel">
      <div class="hero-avatar-wrap" aria-hidden="true">
        <img class="hero-avatar" src="${escapeHtml(avatarUrl)}" alt="${escapeHtml(profile.name)} profile image" />
      </div>
      <section class="hero card">
        ${HERO_MOTIF}
        <p class="kicker">${escapeHtml(profile.title)}</p>
        <h1>${escapeHtml(profile.name)}</h1>
        <p class="lead">${escapeHtml(profile.tagline)}</p>
        <div class="chips">${skillMarkup}</div>
      </section>
    </section>
  `;
}

export function renderJourneySection(journey) {
  return `
    <section class="card section-panel">
      <span class="section-eyebrow">Timeline</span>
      <h2>Journey</h2>
      <div class="timeline">
        ${
          journey.length
            ? journey
                .map(
                  (item) => `
                    <article class="timeline-item">
                      <p class="event-date">${escapeHtml(formatEventDate(item.event_date))}</p>
                      <h3>${escapeHtml(item.title)}</h3>
                      <p>${escapeHtml(item.description)}</p>
                    </article>
                  `
                )
                .join("")
            : renderEmptyState("No journey records found.")
        }
      </div>
    </section>
  `;
}

export function renderScholarshipsSection(scholarships) {
  return `
    <section class="card section-panel">
      <span class="section-eyebrow">Certifications</span>
      <h2>Certifications & Achievements</h2>
      ${
        scholarships.length
          ? `<ul>${scholarships
              .map((s) => `<li>${escapeHtml(s.name)} — ${escapeHtml(s.issuer)} (${escapeHtml(s.year)})</li>`)
              .join("")}</ul>`
          : renderEmptyState("No certifications found.")
      }
    </section>
  `;
}

export function renderExperienceSection(experience) {
  return `
    <section class="card section-panel">
      <span class="section-eyebrow">Experience</span>
      <h2>Work Experience</h2>
      <p class="background-note">
        Earlier background: Chemical Engineering &rarr; AWS ML Foundations (Udacity) and Zero To Mastery
        Academy web development &rarr; an early backend internship at Scoplex Technologies, plus research
        work with Extern and community contribution with United People Global.
      </p>
      <div class="experience-grid">
        ${
          experience.length
            ? experience
                .map(
                  (item) => `
                    <article class="experience-card">
                      <h3>${escapeHtml(item.company)}</h3>
                      <p class="role">${escapeHtml(item.role)}</p>
                      <p>${escapeHtml(item.summary)}</p>
                    </article>
                  `
                )
                .join("")
            : renderEmptyState("No experience records found.")
        }
      </div>
    </section>
  `;
}

function renderProjectMetaBlock(label, text) {
  if (!text) return "";
  return `
    <div>
      <p class="project-meta-label">${escapeHtml(label)}</p>
      <p class="project-meta-text">${escapeHtml(text)}</p>
    </div>
  `;
}

export function renderProjectsSection(projects) {
  return `
    <section id="systems" class="card section-panel">
      <span class="section-eyebrow">Selected Systems</span>
      <h2>What I've engineered</h2>
      <p class="section-intro">
        Production systems, not tutorials — each one solved a real operational constraint.
      </p>
      <div class="projects-grid">
        ${
          projects.length
            ? projects
                .map((project, index) => {
                  const techChips = project.tech_stack
                    .split(",")
                    .map((item) => item.trim())
                    .filter(Boolean)
                    .map((item) => `<span>${escapeHtml(item)}</span>`)
                    .join("");

                  return `
                    <article class="project-card${index < 2 ? " project-card-featured" : ""}">
                      <h3>${escapeHtml(project.title)}</h3>
                      <p class="project-summary">${escapeHtml(project.summary)}</p>
                      <div class="project-meta">
                        ${renderProjectMetaBlock("Engineering challenge", project.challenge)}
                        ${renderProjectMetaBlock("What I engineered", project.engineered)}
                        ${renderProjectMetaBlock("Impact", project.impact)}
                        <div>
                          <p class="project-meta-label">Technology</p>
                          <div class="project-tech">${techChips}</div>
                        </div>
                      </div>
                    </article>
                  `;
                })
                .join("")
            : renderEmptyState("No featured projects found.")
        }
      </div>
    </section>
  `;
}

export function renderArticlesSection(articles) {
  return `
    <section class="card section-panel">
      <span class="section-eyebrow">Writing</span>
      <h2>Writing</h2>
      <div class="experience-grid">
        ${
          articles.length
            ? articles
                .map(
                  (article) => `
                    <article class="experience-card">
                      <h3>${escapeHtml(article.title)}</h3>
                      <p>${escapeHtml(article.excerpt)}</p>
                      <a class="article-link" href="${escapeHtml(article.url)}" target="_blank" rel="noreferrer">${escapeHtml(article.source)}</a>
                    </article>
                  `
                )
                .join("")
            : renderEmptyState("No articles found.")
        }
      </div>
    </section>
  `;
}

export function renderGithubSection(repositories) {
  return `
    <section class="card section-panel">
      <span class="section-eyebrow">Open Source</span>
      <h2>Recent GitHub Repositories</h2>
      <div class="experience-grid">
        ${
          repositories.length
            ? repositories
                .map(
                  (repo) => `
                    <article class="experience-card">
                      <h3>${escapeHtml(repo.name)}</h3>
                      <p>${escapeHtml(repo.description || "No description provided.")}</p>
                      <p class="role">${escapeHtml(repo.language)} - ⭐ ${escapeHtml(repo.stargazers_count)}</p>
                      <a class="article-link" href="${escapeHtml(repo.html_url)}" target="_blank" rel="noreferrer">Open Repository</a>
                    </article>
                  `
                )
                .join("")
            : renderEmptyState("No repositories found.")
        }
      </div>
    </section>
  `;
}

export function renderTopAlert(errors) {
  if (!errors.length) return "";
  return `
    <section class="card alert-card section-panel">
      <p class="alert-text">
        Some sections could not load from the backend: ${escapeHtml(errors.join(", "))}.
      </p>
    </section>
  `;
}

export function renderNavbar(profile) {
  const brand = profile?.name || "Betini Akarandut";
  const github = profile?.github_url || "https://github.com/betiniakarandut";
  const linkedin = profile?.linkedin_url || "https://www.linkedin.com/in/betiniakarandut/";
  const hashnode = profile?.hashnode_url || "https://hashnode.com/@betiniakarandut";
  const twitter = "https://x.com/betiniakarandut";
  const youtube = "https://www.youtube.com/@betiniakarandut";
  const coderlegion = "https://coderlegion.com/user/Betini+Akarandut";

  return `
    <aside class="side-nav card">
      <div class="nav-wrap">
        <a href="#home" class="brand-link">${escapeHtml(brand)}</a>
        <nav class="site-nav" aria-label="Main navigation">
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="#highlights">Highlights</a>
          <a href="#systems">Systems</a>
          <a href="#architecture">Architecture</a>
          <a href="#journey-experience">Experience</a>
          <a href="#stack">Stack</a>
          <a href="#contact">Contact</a>
        </nav>
        <div class="network-icons" aria-label="Network links">
          <a class="network-icon" href="${escapeHtml(linkedin)}" target="_blank" rel="noreferrer" aria-label="LinkedIn">in</a>
          <a class="network-icon" href="${escapeHtml(github)}" target="_blank" rel="noreferrer" aria-label="GitHub">gh</a>
          <a class="network-icon" href="${escapeHtml(hashnode)}" target="_blank" rel="noreferrer" aria-label="Hashnode">hn</a>
          <a class="network-icon" href="${escapeHtml(coderlegion)}" target="_blank" rel="noreferrer" aria-label="CoderLegion">cl</a>
          <a class="network-icon" href="${escapeHtml(twitter)}" target="_blank" rel="noreferrer" aria-label="Twitter">x</a>
          <a class="network-icon" href="${escapeHtml(youtube)}" target="_blank" rel="noreferrer" aria-label="YouTube">yt</a>
        </div>
      </div>
    </aside>
  `;
}

export function renderAboutSection(profile) {
  if (!profile) {
    return `
      <section id="about" class="card">
        <h2>About</h2>
        ${renderEmptyState("Profile info is currently unavailable.")}
      </section>
    `;
  }

  return `
    <section id="about" class="card section-panel">
      <span class="section-eyebrow">About</span>
      <h2>How I got here</h2>
      <div class="prose">${renderParagraphs(profile.bio)}</div>
    </section>
  `;
}

export function renderChallengesSection() {
  return `
    <section id="challenges" class="card section-panel">
      <span class="section-eyebrow">Challenges</span>
      <h2>Challenges</h2>
      <div class="experience-grid">
        <article class="experience-card">
          <h3>Career Transition</h3>
          <p>Moved from Chemical Engineering into software engineering while balancing academics and internships.</p>
        </article>
        <article class="experience-card">
          <h3>Production Readiness</h3>
          <p>Built confidence in shipping backend services with testing, observability, and iterative improvements.</p>
        </article>
        <article class="experience-card">
          <h3>Scale and Reliability</h3>
          <p>Navigated real-world constraints across API design, async jobs, and integrations in fast-moving teams.</p>
        </article>
      </div>
    </section>
  `;
}

export function renderPersonalLifeSection() {
  return `
    <section id="personal-life" class="card section-panel">
      <span class="section-eyebrow">Beyond Engineering</span>
      <h2>Personal Life/Encounters</h2>
      <p class="muted">
        Beyond code, I value resilience, discipline, and growth. My encounters across mentorship, teamwork,
        and self-driven learning have shaped how I solve problems and support people.
      </p>
      <p class="muted">
        I enjoy sharing lessons from engineering projects, cloud experiments, and practical insights that help
        upcoming developers build with confidence.
      </p>
    </section>
  `;
}

export function renderCtaSection(profile) {
  const email = profile?.email ? `mailto:${profile.email}` : "#contact";
  return `
    <section id="cta" class="card cta-card section-panel">
      <h2>Let's build something that has to hold up in production</h2>
      <p class="muted">Open to backend, cloud, and platform engineering opportunities.</p>
      <div class="cta-actions">
        <a class="cta-radio-btn cta-radio-btn-primary" href="#contact">
          <span class="cta-radio-icon" aria-hidden="true"></span>
          <span>Send a Message</span>
        </a>
        <a class="cta-radio-btn cta-radio-btn-secondary" href="${escapeHtml(email)}">
          <span class="cta-radio-icon" aria-hidden="true"></span>
          <span>Email Me</span>
        </a>
      </div>
    </section>
  `;
}

export function renderSiteFooter(profile) {
  const github = profile?.github_url || "https://github.com/betiniakarandut";
  const linkedin = profile?.linkedin_url || "https://www.linkedin.com/in/betiniakarandut/";
  const hashnode = profile?.hashnode_url || "https://hashnode.com/@betiniakarandut";
  const twitter = "https://x.com/betiniakarandut";
  const youtube = "https://www.youtube.com/@betiniakarandut";
  const coderlegion = "https://coderlegion.com/user/Betini+Akarandut";

  return `
    <footer class="site-footer card section-panel">
      <p class="muted footer-copy">Connect and follow my work</p>
      <div class="footer-actions">
        <a href="${escapeHtml(hashnode)}" target="_blank" rel="noreferrer">Hashnode</a>
        <a href="${escapeHtml(github)}" target="_blank" rel="noreferrer">GitHub</a>
        <a href="${escapeHtml(linkedin)}" target="_blank" rel="noreferrer">LinkedIn</a>
        <a href="${escapeHtml(coderlegion)}" target="_blank" rel="noreferrer">CoderLegion</a>
        <a href="${escapeHtml(twitter)}" target="_blank" rel="noreferrer">Twitter</a>
        <a href="${escapeHtml(youtube)}" target="_blank" rel="noreferrer">YouTube</a>
      </div>
    </footer>
  `;
}
