// TracTrac deep case study. Personal responsibilities come from the experience
// record; ISSAM figures are programme/platform outcomes and are labelled as such.

export const TRACTRAC = {
  intro:
    "TracTrac Plus is TracTrac's proprietary on-demand farm mechanisation platform. It carries farmer onboarding, land mapping, soil testing, demand logging, job assignment, job tracking, job closure and payment recording, connecting farmers, mechanisation service providers (MSPs), field agents and operations teams. I lead its backend and infrastructure engineering.",

  context: [
    { label: "Role", value: "Lead Backend/DevOps Engineer · Feb 2025 – present" },
    { label: "Scale", value: "60k+ users on two production FastAPI backends with shared infrastructure" },
    { label: "Environment", value: "Rural and underserved areas where connectivity cannot be assumed" },
  ],

  constraints: [
    "Field agents capture work where the network drops out, but every record still has to reach the backend exactly once.",
    "Farmers, MSPs, field agents and operations teams all touch the same job as it moves from request to closure.",
    "Bookings, hire workflows and payments move money, so they have to reconcile.",
    "Field activity has to become data that operations and programme partners can rely on.",
  ],

  architecture: {
    title: "TracTrac platform (conceptual)",
    caption:
      "Components used on TracTrac. Not every request touches every layer; the exact topology is simplified.",
    layers: [
      {
        label: "Clients",
        nodes: [
          { name: "Field agent workflows", detail: "offline-capable" },
          { name: "Admin dashboard", detail: "Next.js · Redux" },
          { name: "CommCare integration" },
        ],
      },
      { label: "API", nodes: [{ name: "Two FastAPI backends", detail: "shared infrastructure" }] },
      {
        label: "Data & messaging",
        nodes: [
          { name: "PostgreSQL + PostGIS", detail: "via PgBouncer" },
          { name: "Redis", detail: "caching" },
          { name: "Kafka", detail: "outbox event flows" },
        ],
      },
      {
        label: "Processing",
        nodes: [{ name: "Celery workers" }, { name: "WebSockets", detail: "live updates" }],
      },
      {
        label: "Operational services",
        nodes: [
          "Booking & hire",
          "GPS vehicle tracking",
          "Farm measurement",
          "Payments & reconciliation",
          "Reporting & Excel exports",
        ],
      },
    ],
  },

  offline: {
    flow: [
      { title: "Field agent", note: "captures requests on site" },
      { title: "Offline workflow", note: "no connectivity required" },
      { title: "Synchronisation", note: "when a connection returns" },
      { title: "Idempotent create/sync APIs", note: "FastAPI" },
      { title: "Batch reconciliation", note: "against server state" },
      { title: "PostgreSQL", note: "system of record" },
      { title: "Operations & reporting" },
    ],
    guarantees: [
      "Replays are safe: a request resent after a dropped connection does not create a duplicate record.",
      "Batches are reconciled against what the server already holds instead of being trusted blindly.",
      "Validation stays on the server, so offline capture cannot bypass business rules.",
    ],
    tradeoff:
      "The backend accepts eventual consistency: field records can arrive long after they were captured. In exchange, field work never stops for a network.",
    outcome:
      "I led this workflow for tractor and labour-saving-device requests. It replaced a paid third-party data-collection tool and extended the platform to communities without reliable connectivity.",
  },

  geospatial: [
    "Farm measurement from GPS coordinates captured in the field: polygon area via the Shoelace formula, distances via the Haversine formula.",
    "Live GPS vehicle tracking.",
    "Location-aware workflows for land mapping, job assignment and service delivery, on a PostgreSQL/PostGIS data layer.",
  ],

  payments: [
    "Booking and hire workflows that carry a job from request through assignment to closure.",
    "Wallet and payment reconciliation with Paystack, using decimal-precision, concurrency-safe calculations.",
    "Transaction state that feeds operational and programme reporting.",
  ],

  incident: [
    {
      label: "Observation",
      body: "An administrative dashboard began failing intermittently under load. A single screen was generating 60+ backend requests.",
    },
    {
      label: "Investigation",
      body: "Traced the request pattern and examined database performance, caching, locking, pagination and aggregate-query behaviour before choosing a fix. The cause was request fan-out and redundant data retrieval.",
    },
    {
      label: "Response",
      body: [
        "SWR caching on the client, so repeated views reuse data instead of refetching it.",
        "Page-1-only fetching where the screen only displays the first page.",
        "Server-side summary endpoints that compute and cache aggregates once.",
        "The existing response contract preserved, and the decision recorded as an architecture decision record (ADR).",
      ],
    },
    {
      label: "Result",
      body: "The screen now asks the backend for what it shows instead of assembling it from dozens of calls, and the ADR explains why so the pattern does not creep back.",
    },
  ],

  infrastructure: [
    "Docker containers on a self-managed Contabo VPS, orchestrated with Coolify behind a Traefik reverse proxy: 20+ containerised applications.",
    "PgBouncer in transaction-pooling mode in front of PostgreSQL, keeping connection counts bounded as workers scale.",
    "Redis and Kafka as shared infrastructure for both backends.",
    "Staging environment, health checks and migration-gated deployments.",
    "Capacity modelling and right-sizing to control infrastructure cost.",
  ],

  outcomesChain: [
    { title: "Technology", note: "backends, offline workflows, GPS" },
    { title: "Operational workflow", note: "onboarding → demand → job → payment" },
    { title: "Field adoption", note: "MSPs and field agents trained on the platform" },
    { title: "Programme data", note: "requests, fulfilment, hectares, payments" },
    { title: "Decision-making", note: "monthly and quarterly technical reporting" },
    { title: "Mechanisation outcomes", note: "services delivered to smallholder farmers" },
  ],

  dataStory:
    "The backend's job is to turn distributed field activity (registrations, land mapping, service demand, job assignment and fulfilment, payments, equipment use, location) into structured operational data. I built the reporting that reconciles platform and field data for programme monitoring and donor documentation.",

  programme: {
    intro:
      "ISSAM is a TracTrac and Mastercard Foundation partnership. The figures below are programme and platform outcomes recorded within ISSAM. They are the work of many teams, partners, MSPs and farmers, not my individual achievements. They describe the environment the backend serves.",
    platform: [
      { value: "146,170", label: "farmers registered or onboarded onto TracTrac Plus" },
      { value: "8,577", label: "service requests" },
      { value: "91.8%", label: "fulfilment rate (7,872 fulfilled)" },
      { value: "4,740", label: "unique farmers serviced" },
      { value: "8,719.88 ha", label: "hectares worked" },
    ],
    programme: [
      { value: "25,000+", label: "young people mobilised and screened" },
      { value: "18", label: "training cohorts" },
      { value: "5,012", label: "certified mechanisation service providers" },
      { value: "2,987", label: "graduates actively earning as MSPs" },
      { value: "566", label: "cooperatives formed" },
      { value: "3,396", label: "machines and labour-saving devices deployed" },
      { value: "300,000+", label: "smallholder farmers directly sensitised" },
    ],
    inclusion:
      "Active MSPs include 1,200+ women, 84 persons with disabilities and 123 internally displaced persons; 579 operators and 14 mechanics have been trained.",
    ecosystem:
      "The wider programme has engaged 500+ stakeholders across 10+ key institutions, and supported the review and development of the National Agricultural Mechanisation Policy 2026 and a Mechanisation Investment Strategy (70+ stakeholders in pre-ratification review; 500+ delegates at ratification). My contribution sits on the technology and delivery side of that ecosystem.",
  },

  stack: [
    "FastAPI",
    "PostgreSQL",
    "PostGIS",
    "PgBouncer",
    "Redis",
    "Kafka",
    "Celery",
    "WebSockets",
    "Docker",
    "Coolify",
    "Traefik",
    "Next.js",
    "Redux",
    "Paystack",
    "CommCare",
  ],
};
