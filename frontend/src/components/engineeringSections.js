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
      body: "Operate production backends serving 60,000+ registered users on TracTrac's platform, plus 5,000+ farmers onboarded through VITAL 2.",
    },
    {
      tag: "OF",
      title: "Offline-First Systems",
      body: "Led an offline-first system for low-connectivity field operations at TracTrac, replacing a paid third-party data-collection tool.",
    },
    {
      tag: "DS",
      title: "Distributed Systems",
      body: "Built Kafka and outbox-pattern event flows, Redis caching, and real-time WebSocket communication across production backends.",
    },
    {
      tag: "CD",
      title: "Cloud & DevOps",
      body: "Migrated infrastructure to a self-managed Contabo VPS and Coolify, running 20+ containerized applications with capacity modelling and right-sizing.",
    },
    {
      tag: "$",
      title: "Payment Systems",
      body: "Implemented concurrency-safe financial reconciliation using precise decimal arithmetic, with Paystack payment processing at TracTrac.",
    },
    {
      tag: "AI",
      title: "Applied AI",
      body: "Engineered a context-aware diagnostic system combining vision input, structured LLM outputs, and equipment, location, and technician context.",
    },
    {
      tag: "PE",
      title: "Performance Engineering",
      body: "Diagnosed a production dashboard issue under load, driven by request fan-out, through measurement rather than assumptions.",
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
    { value: "60K+", label: "Registered users on TracTrac's platform" },
    { value: "5K+", label: "Farmers onboarded (VITAL 2)" },
    { value: "20+", label: "Containerized production applications managed" },
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
        "Reverse Proxy",
        "API",
        "Redis / Kafka",
        "PostgreSQL",
        "External Services (Paystack, Firebase)",
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
      title: "Infrastructure Migration",
      body: "Migrated from managed hosting to a self-managed Contabo VPS with Coolify orchestration and a Traefik reverse proxy, running 20+ containerized applications.",
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
      title: "Capacity Modelling",
      body: "Modeled platform behavior across concurrent-user ranges and right-sized infrastructure accordingly, reducing costs without sacrificing headroom.",
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

export function renderTracTracCaseStudiesSection() {
  const caseStudies = [
    {
      title: "Offline-First Field Operations",
      challenge:
        "Field agents and farmers request tractors and labour-saving devices from areas with unreliable or no connectivity — the system has to tolerate delayed synchronization, retries, duplicate requests, and eventual consistency rather than assuming an always-on connection.",
      approach:
        "Led the design and implementation of an offline-first system for these requests, replacing a paid third-party data-collection tool the platform previously relied on.",
      outcome:
        "Expanded digital access for remote farming communities who couldn't reliably reach the platform's core APIs directly.",
    },
    {
      title: "Diagnosing a Production Dashboard Under Load",
      challenge:
        "An administrative dashboard began failing intermittently under load, generating 60+ backend requests per page load — a classic request fan-out problem, but the root cause wasn't obvious from the symptoms alone.",
      approach:
        "Investigated systematically rather than guessing: database performance, caching behavior, locking, pagination, and aggregate-query behavior were all examined before deciding on a fix.",
      outcome:
        "Redesigned the dashboard around page-scoped fetching and server-computed, cached summaries — while preserving the existing response contract — and documented the decision as an ADR to prevent regression.",
    },
    {
      title: "Infrastructure Migration to Self-Managed Hosting",
      challenge:
        "Moving from managed hosting toward infrastructure the team fully controls, without sacrificing reliability during the transition.",
      approach:
        "Provisioned and migrated services to a self-managed Contabo VPS with Coolify for container orchestration and a Traefik reverse proxy, running 20+ containerized applications with PgBouncer managing database connections.",
      outcome:
        "Full operational ownership of the deployment path — capacity modelling and right-sizing now directly inform infrastructure costs instead of a managed provider's pricing tiers.",
    },
    {
      title: "Payment & Financial Reconciliation",
      challenge:
        "Financial calculations in a payments system can't tolerate floating-point rounding errors — reconciliation has to be exact, and concurrent writes can't corrupt balances.",
      approach:
        "Implemented concurrency-safe financial reconciliation using precise decimal arithmetic, integrated with Paystack for payment processing.",
      outcome:
        "Reliable payment reconciliation as part of TracTrac's core operational systems.",
    },
    {
      title: "Geospatial Farm Measurement",
      challenge:
        "Determining farm area from GPS coordinates captured in the field, where signal noise and inconsistent walking paths make raw coordinates unreliable.",
      approach:
        "Built GPS-based farm measurement using geospatial calculations against a PostgreSQL/PostGIS data layer.",
      outcome:
        "A working measurement workflow integrated into the platform's booking and service-delivery flow.",
    },
  ];

  return `
    <section id="case-studies" class="card section-panel">
      <span class="section-eyebrow">TracTrac Case Studies</span>
      <h2>Engineering problems, not a technology list</h2>
      <p class="section-intro">
        TracTrac is a production system operating in a real agricultural environment, not a demo. These are
        the engineering problems behind it.
      </p>
      <div class="case-study-grid">
        ${caseStudies
          .map(
            (study) => `
              <article class="case-study-card">
                <h3>${escapeHtml(study.title)}</h3>
                <div class="case-study-steps">
                  <div class="case-study-step">
                    <p class="case-study-step-label">Challenge</p>
                    <p>${escapeHtml(study.challenge)}</p>
                  </div>
                  <div class="case-study-step">
                    <p class="case-study-step-label">Approach</p>
                    <p>${escapeHtml(study.approach)}</p>
                  </div>
                  <div class="case-study-step">
                    <p class="case-study-step-label">Outcome</p>
                    <p>${escapeHtml(study.outcome)}</p>
                  </div>
                </div>
              </article>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderDataSystemsSection() {
  return `
    <section id="data-systems" class="card section-panel">
      <span class="section-eyebrow">Data & Decision Systems</span>
      <h2>Where this is heading</h2>
      <div class="prose">
        <p class="muted">
          The backend systems I operate already generate and move a substantial amount of operational
          data — farmers, mechanization requests, tractor activity, geographic locations, payments,
          service delivery, and field events. At TracTrac, I built reporting infrastructure that reconciles
          platform and field data into monitoring on hectares mechanized, farmers reached, revenue,
          cooperatives, and service delivery — the operational picture a program needs to make decisions.
        </p>
        <p class="muted">
          That's the natural bridge from backend engineering to data science: I already build the systems
          that generate and operationalize this data. Advanced training in data science and decision
          analytics is how I'd go further — turning that data into forecasting, optimization, and better
          operational decisions, rather than just moving it reliably from one system to another.
        </p>
        <p class="muted">
          To be clear about where I am today: this is a direction I'm building toward, not a claim of
          current machine learning research or production ML deployment. My production work right now is
          backend and data infrastructure engineering — the foundation that kind of work depends on.
        </p>
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
      body: "Instrument systems so problems are diagnosable, not just detectable — measurement before assumptions.",
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
  "Geospatial",
  "Payments",
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
