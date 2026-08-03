import { escapeHtml } from "../utils/format";

function renderFlowRow(steps) {
  return `
    <div class="flow-row">
      ${steps
        .map((step, index) => {
          const arrow = index === 0 ? "" : `<span class="flow-arrow" aria-hidden="true">&rarr;</span>`;
          return `${arrow}<span class="flow-step">${escapeHtml(step)}</span>`;
        })
        .join("")}
    </div>
  `;
}

export function renderHighlightsSection() {
  const highlights = [
    {
      tag: "PS",
      title: "Production Systems",
      body: "Operate production backends serving 100,000+ registered users on TracTrac's platform, plus 5,000+ farmers onboarded through VITAL 2.",
    },
    {
      tag: "OF",
      title: "Offline-First Systems",
      body: "Designed synchronization and reconciliation architecture for field operations across low-connectivity rural environments at TracTrac and VITAL 2.",
    },
    {
      tag: "DS",
      title: "Distributed Systems",
      body: "Built Kafka and outbox-pattern event flows, Redis caching, and real-time WebSocket communication across production backends.",
    },
    {
      tag: "CD",
      title: "Cloud & DevOps",
      body: "Containerized and deployed production services with Docker across VPS, Render, and Coolify, with migration-gated deployments and health checks.",
    },
    {
      tag: "$",
      title: "Payment Systems",
      body: "Built Paystack payment reconciliation at TracTrac and an escrow-style payment lifecycle with payout wallets and dispute workflows at SolarAfRiC.",
    },
    {
      tag: "AI",
      title: "Applied AI",
      body: "Engineered a context-aware diagnostic system combining vision input, structured LLM outputs, and equipment, location, and technician context.",
    },
    {
      tag: "PE",
      title: "Performance Engineering",
      body: "Diagnosed a production dashboard generating 60+ backend requests per load and redesigned its data-loading architecture.",
    },
  ];

  return `
    <section id="highlights" class="card section-panel">
      <span class="section-eyebrow">Technical Highlights</span>
      <h2>Where I add the most value</h2>
      <div class="highlights-grid">
        ${highlights
          .map(
            (item) => `
              <article class="highlight-card">
                <div class="highlight-icon" aria-hidden="true">${escapeHtml(item.tag)}</div>
                <h3>${escapeHtml(item.title)}</h3>
                <p>${escapeHtml(item.body)}</p>
              </article>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderStatsStrip() {
  const stats = [
    { value: "100K+", label: "Registered users managed (TracTrac)" },
    { value: "5K+", label: "Farmers onboarded (VITAL 2)" },
    { value: "5", label: "Production platforms across 4 companies" },
  ];

  return `
    <section class="card section-panel">
      <div class="stats-strip">
        ${stats
          .map(
            (stat) => `
              <div class="stat-item">
                <div class="stat-value">${escapeHtml(stat.value)}</div>
                <div class="stat-label">${escapeHtml(stat.label)}</div>
              </div>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderArchitectureSection() {
  const diagrams = [
    {
      title: "TracTrac Offline Synchronization",
      steps: [
        "Field Agent",
        "Offline Local Data",
        "Sync API",
        "Core Backend",
        "PostgreSQL / Redis",
        "Kafka / Outbox",
        "Admin & Operations",
      ],
    },
    {
      title: "SolarAfRiC AI Diagnostics",
      steps: [
        "User Report",
        "Diagnostic API",
        "Context Assembly (Equipment, Location, Technician, LMS)",
        "Vision + LLM",
        "Structured Diagnosis",
        "Self-Fix / Technician Escalation",
      ],
    },
    {
      title: "Production Infrastructure",
      steps: [
        "Client",
        "API",
        "Redis / Kafka",
        "PostgreSQL",
        "External Services (Paystack, Firebase, CommCare)",
      ],
    },
  ];

  return `
    <section id="architecture" class="card section-panel">
      <span class="section-eyebrow">Architecture</span>
      <h2>How the systems are put together</h2>
      <p class="section-intro">Conceptual, not exhaustive — the shape of how data and requests actually move.</p>
      <div class="architecture-grid">
        ${diagrams
          .map(
            (diagram) => `
              <div class="architecture-diagram">
                <h3>${escapeHtml(diagram.title)}</h3>
                ${renderFlowRow(diagram.steps)}
              </div>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderProductionEngineeringSection() {
  const items = [
    {
      title: "Containerization",
      body: "Docker-based deployment for consistent behavior between development and production environments.",
    },
    {
      title: "Deployment Targets",
      body: "Services deployed and maintained across self-managed VPS infrastructure, Render, and Coolify.",
    },
    {
      title: "Connection Pooling",
      body: "PgBouncer in transaction-pooling mode in front of PostgreSQL to keep connections stable under load.",
    },
    {
      title: "Migration-Gated Deployments",
      body: "Deployments gated on schema migrations and health checks, so a rollout doesn't outrun the database it depends on.",
    },
    {
      title: "Scalability Analysis",
      body: "Modeled platform behavior from 10 to 500+ concurrent users to plan capacity ahead of growth.",
    },
  ];

  return `
    <section id="production-engineering" class="card section-panel">
      <span class="section-eyebrow">Production Engineering</span>
      <h2>What happens after the code is written</h2>
      <p class="section-intro">
        I don't just build the backend — I own what happens when it reaches production.
      </p>
      <div class="experience-grid">
        ${items
          .map(
            (item) => `
              <article class="experience-card">
                <h3>${escapeHtml(item.title)}</h3>
                <p>${escapeHtml(item.body)}</p>
              </article>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderPerformanceCaseStudySection() {
  const steps = [
    { label: "Problem", text: "One TracTrac dashboard screen was generating 60+ backend requests on load." },
    {
      label: "Investigation",
      text: "Traced the request fan-out to inefficient, per-widget client-side data loading rather than a single page-scoped fetch.",
    },
    {
      label: "Engineering response",
      text: "Redesigned the loading architecture around page-scoped data fetching and server-computed summary endpoints instead of client-side fan-out, and documented the decision as an architectural record (ADR).",
    },
    {
      label: "Outcome",
      text: "Reduced the dashboard's request volume and left a documented reference point so future dashboard screens don't regress into the same pattern.",
    },
  ];

  return `
    <section class="card section-panel">
      <span class="section-eyebrow">Performance Case Study</span>
      <h2>The 60-request dashboard</h2>
      <div class="case-study-steps">
        ${steps
          .map(
            (step) => `
              <div class="case-study-step">
                <p class="case-study-step-label">${escapeHtml(step.label)}</p>
                <p>${escapeHtml(step.text)}</p>
              </div>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderPhilosophySection() {
  const principles = [
    {
      title: "Reliability",
      body: "Design for the failure modes that actually happen — network partitions, retries, partial writes — not just the happy path.",
    },
    {
      title: "Data Consistency",
      body: "Treat data consistency as a first-class concern, using patterns like the outbox pattern to keep events and state in sync.",
    },
    {
      title: "Observability",
      body: "Instrument systems so problems are diagnosable, not just detectable — the dashboard investigation started with looking at what was actually being requested.",
    },
    {
      title: "Performance",
      body: "Profile before optimizing, and prefer architectural fixes — caching, connection pooling, better queries — over throwing more infrastructure at a problem.",
    },
    {
      title: "Operational Ownership",
      body: "Own the deployment path, not just the code — migrations, health checks, and rollout strategy are part of the engineering, not an afterthought.",
    },
  ];

  return `
    <section id="how-i-engineer" class="card section-panel">
      <span class="section-eyebrow">How I Engineer</span>
      <h2>The way I think about systems</h2>
      <div class="philosophy-grid">
        ${principles
          .map(
            (item) => `
              <article class="philosophy-item">
                <h3>${escapeHtml(item.title)}</h3>
                <p>${escapeHtml(item.body)}</p>
              </article>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

const SKILL_GROUP_ORDER = [
  "Backend",
  "Data",
  "Distributed Systems",
  "Cloud & Infrastructure",
  "DevOps",
  "Integrations",
  "Frontend",
];

export function renderSkillsSection(skills) {
  if (!skills.length) {
    return `
      <section id="stack" class="card section-panel">
        <span class="section-eyebrow">Technical Stack</span>
        <h2>Capabilities</h2>
        ${renderEmptyStateFallback()}
      </section>
    `;
  }

  const grouped = new Map();
  skills.forEach((skill) => {
    const category = skill.category || "Other";
    if (!grouped.has(category)) grouped.set(category, []);
    grouped.get(category).push(skill);
  });

  const orderedCategories = [
    ...SKILL_GROUP_ORDER.filter((category) => grouped.has(category)),
    ...[...grouped.keys()].filter((category) => !SKILL_GROUP_ORDER.includes(category)),
  ];

  const groupsMarkup = orderedCategories
    .map((category) => {
      const isSupporting = category === "Frontend";
      const chips = grouped
        .get(category)
        .map((skill) => `<span>${escapeHtml(skill.name)}</span>`)
        .join("");

      return `
        <div class="skill-group${isSupporting ? " is-supporting" : ""}">
          <p class="skill-group-title">${escapeHtml(category)}</p>
          <div class="chips">${chips}</div>
        </div>
      `;
    })
    .join("");

  return `
    <section id="stack" class="card section-panel">
      <span class="section-eyebrow">Technical Stack</span>
      <h2>Capabilities, grouped by what they do</h2>
      <div class="skills-groups">${groupsMarkup}</div>
    </section>
  `;
}

function renderEmptyStateFallback() {
  return `<p class="muted empty-state">Skill data is currently unavailable.</p>`;
}
