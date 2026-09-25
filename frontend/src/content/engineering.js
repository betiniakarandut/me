// Static engineering narrative: hero, impact, architecture, production
// engineering and principles. Data-backed records (projects, experience,
// skills) come from the API instead.

export const HERO = {
  name: "Betini Akarandut",
  title: "Backend & Cloud Engineer",
  lead: "I build production backend systems, cloud infrastructure and data-driven applications that operate under real-world constraints.",
  current: "Lead Backend/DevOps Engineer at TracTrac · Abuja, Nigeria",
  proof: [
    "Production APIs",
    "Distributed & event-driven systems",
    "Offline-first field workflows",
    "Cloud infrastructure & DevOps",
    "Payments",
    "Geospatial",
    "Applied AI",
  ],
  avatar: "https://github.com/betiniakarandut.png",
};

export const IMPACT = {
  metrics: [
    { value: "60k+", label: "users on TracTrac's platform, served by two production FastAPI backends I lead" },
    { value: "5,000+", label: "farmers onboarded on VITAL 2, where I was the sole backend engineer" },
    { value: "20+", label: "containerised applications operated on self-managed infrastructure" },
    { value: "3", label: "production platforms with backend ownership: TracTrac, SolarAfRiC, VITAL 2" },
  ],
  note: "ISSAM programme outcomes appear separately in the TracTrac case study and are not personal metrics.",
};

export const ARCHITECTURE = {
  diagnostics: {
    title: "SolarAfRiC: context-aware AI diagnostics",
    caption:
      "The model is one step in an operational workflow. Its structured output decides what the backend does next.",
    layers: [
      {
        label: "Input",
        nodes: [
          { name: "Customer report", detail: "text + photos" },
          { name: "Diagnostic conversation", detail: "multi-turn" },
        ],
      },
      {
        label: "Context assembly · FastAPI",
        nodes: [
          "Equipment specifications",
          "GPS location",
          "Nearby verified technicians",
          "LMS lessons",
          "Booking history",
        ],
      },
      {
        label: "Model",
        nodes: [{ name: "OpenAI GPT-4o-mini", detail: "vision input · structured JSON output" }],
      },
      {
        label: "Next action",
        nodes: ["Guided self-fix", "Further investigation", "Safety/severity escalation", "Technician booking"],
      },
    ],
  },
  bookingFlow: [
    { title: "Customer books a technician" },
    { title: "Payment captured and held", note: "Paystack, escrow-style" },
    { title: "7-state booking lifecycle" },
    { title: "Completion verified" },
    { title: "Technician payout wallet" },
    { title: "Withdrawal", note: "resolved bank account" },
  ],
  bookingNote: "A dispute workflow handles contested jobs. Technician communication and notifications use WebSockets and Firebase Cloud Messaging.",
  storageFlow: [
    { title: "Upload" },
    { title: "MIME sniffing", note: "content, not extension" },
    { title: "Cloudinary" },
    { title: "S3-compatible", note: "fallback" },
    { title: "Local storage", note: "last resort" },
  ],
  importFlow: [
    { title: "Bulk farmer upload" },
    { title: "Import with rollback", note: "all or nothing" },
    { title: "Audit trail" },
  ],
  voucherFlow: [{ title: "Voucher campaign" }, { title: "QR generation" }, { title: "Farmer onboarding" }],
};

export const PRODUCTION_ENGINEERING = [
  {
    title: "Reliability",
    items: [
      "Idempotent create/sync APIs and batch reconciliation for unreliable networks (TracTrac)",
      "Health checks and migration-gated deployments (TracTrac)",
      "Storage fallback across three providers (SolarAfRiC)",
      "Bulk import with rollback and audit trails (VITAL 2)",
    ],
  },
  {
    title: "Performance",
    items: [
      "Diagnosed request fan-out: SWR caching, page-1-only fetching, server-side summaries (TracTrac)",
      "Redis caching (TracTrac)",
      "Pagination API for a growing listing (MeetDevs)",
      "Response-time work on Django REST APIs (Join Momentum)",
    ],
  },
  {
    title: "Infrastructure",
    items: [
      "Docker and Docker Compose; self-managed VPS with Coolify and Traefik",
      "PgBouncer transaction pooling for PostgreSQL",
      "Render, Nginx load balancing, AWS EC2",
      "Capacity modelling and right-sizing",
    ],
  },
  {
    title: "Data",
    items: [
      "PostgreSQL and PostGIS as systems of record",
      "SQLAlchemy and Alembic: 29 migrations on SolarAfRiC, 39 on VITAL 2",
      "Decimal-precision financial reconciliation",
      "Audit trails and role-based access control",
    ],
  },
  {
    title: "Distributed systems",
    items: [
      "Kafka with the outbox pattern (TracTrac)",
      "Celery and Redis for asynchronous work (TracTrac, SUBSEL)",
      "WebSockets and Firebase Cloud Messaging (SolarAfRiC)",
      "Batched mass email within provider limits (VITAL 2)",
    ],
  },
];

export const THIS_SITE =
  "This site follows the same habits at small scale: FastAPI, PostgreSQL and Alembic, with migrations and an idempotent content sync run as a pre-deploy step and a database readiness check gating each release.";

export const PRINCIPLES = [
  {
    title: "Build for the actual environment",
    body: "Network, infrastructure and operational constraints are requirements, not edge cases.",
  },
  {
    title: "Design for failure",
    body: "Retries, synchronisation, validation and partial failure are designed in deliberately, not discovered in production.",
  },
  {
    title: "Measure before optimising",
    body: "Production behaviour, such as the 60+ request dashboard, decides where performance work goes.",
  },
  {
    title: "Keep systems understandable",
    body: "Architecture has to stay operable by the team that runs it; decisions get written down.",
  },
  {
    title: "Connect technology to outcomes",
    body: "A production system exists to support a real workflow, and it is judged by that workflow.",
  },
];
