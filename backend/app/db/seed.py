"""Portfolio content: the source of truth for database-driven sections.

Loaded by `python -m app.db.content_sync`, which upserts each entry by its
natural key (see KEY_FIELDS in content_sync.py). Edit content here, then run the
sync; do not rename a key field without running the sync with --prune.

Every claim here must be traceable to real work. Programme-level outcomes
(e.g. ISSAM figures) belong in the frontend case study, clearly attributed,
not in personal experience entries.
"""

PROFILE = {
    "name": "Betini Akarandut",
    "title": "Backend & Cloud Engineer",
    "tagline": (
        "I build production backend systems, cloud infrastructure and data-driven applications "
        "that operate under real-world constraints."
    ),
    "bio": (
        "I lead backend and infrastructure engineering at TracTrac, a nationwide agricultural "
        "mechanisation platform: two production FastAPI backends, the PostgreSQL, Redis and Kafka "
        "infrastructure beneath them, and the deployment path that ships them. Alongside that I have "
        "delivered production backends for SolarAfRiC and VITAL 2, and co-founded SUBSEL Digital Services."
        "\n\n"
        "I came to software from a BEng in Chemical Engineering, which gave me a quantitative foundation "
        "in numerical methods, mathematical modelling and operations research. It still shapes how I "
        "reason about systems. The platforms I work on turn field activity into operational data, and "
        "I'm building toward data science and decision analytics as the next step from that."
    ),
    "location": "FCT-Abuja, Nigeria",
    "email": "betiniakarandut@gmail.com",
    "github_url": "https://github.com/betiniakarandut",
    "linkedin_url": "https://www.linkedin.com/in/betiniakarandut/",
    "hashnode_url": "https://hashnode.com/@betiniakarandut",
}

JOURNEY_EVENTS = [
    {
        "title": "B.Eng. Chemical Engineering — University of Port Harcourt",
        "event_date": "2017",
        "description": (
            "Quantitative foundation in calculus, probability and statistics, numerical methods, "
            "mathematical modelling and operations research. Graduated 2024, CGPA 3.72/5.00, Second "
            "Class Honours (Upper Division)."
        ),
    },
    {
        "title": "Started Software Engineering",
        "event_date": "2022-01",
        "description": (
            "Began software engineering alongside the degree: web development (Zero To Mastery "
            "Academy) and AWS Machine Learning Foundations (Udacity)."
        ),
    },
    {
        "title": "Early Backend Roles",
        "event_date": "2022-02",
        "description": (
            "Backend roles at Scoplex Technologies and later Retiny, building APIs, authentication "
            "and mobile-facing backend services."
        ),
    },
    {
        "title": "ALX Africa Software Engineering Certification",
        "event_date": "2022-09",
        "description": (
            "Software engineering programme, including a backend/DevOps placement in Kigali, Rwanda "
            "(Jan–Oct 2023)."
        ),
    },
    {
        "title": "Backend Developer — Join Momentum",
        "event_date": "2024-06",
        "description": "Backend APIs for an AI-powered job simulation platform, through Jan 2025.",
    },
    {
        "title": "Lead Backend/DevOps Engineer — TracTrac",
        "event_date": "2025-02",
        "description": (
            "Took on backend and infrastructure leadership for a production platform that operates "
            "in the field, not just behind a dashboard."
        ),
    },
    {
        "title": "SolarAfRiC & VITAL 2 — Production Backends Under Field Constraints",
        "event_date": "2026-04",
        "description": (
            "Delivered backends for an AI-assisted solar services marketplace (SolarAfRiC) and a "
            "livestock vaccination and field-operations platform (VITAL 2)."
        ),
    },
    {
        "title": "Beyond Implementation — ISSAM Learning Event & Pitch Challenge",
        "event_date": "2026",
        "description": (
            "Took on technical communication and programme delivery around the TracTrac platform: "
            "the ISSAM Year 2 Learning Event explainer, and leading the Young Innovators in "
            "Agricultural Mechanisation Pitch Challenge team."
        ),
    },
    {
        "title": "Co-Founder — SUBSEL Digital Services",
        "event_date": "2026-09",
        "description": "Co-founded a pre-launch digital services venture, owning product and engineering.",
    },
    {
        "title": "Toward Data & Decision Systems",
        "event_date": "2026",
        "description": (
            "Pursuing advanced training in data science and decision analytics, building on reporting "
            "infrastructure already running in production."
        ),
    },
]

# Stored in the `scholarships` table (name kept for API compatibility);
# `category` separates certifications, scholarships and awards.
CREDENTIALS = [
    {
        "name": "AWS Certified Solutions Architect – Associate",
        "category": "certification",
        "issuer": "AWS",
        "year": "In progress (2026)",
        "description": "Pursuing certification, expected 2026.",
    },
    {
        "name": "Software Engineering Certification",
        "category": "certification",
        "issuer": "ALX / Holberton School",
        "year": "2023",
        "description": "Software engineering training covering Python, Node.js and backend specialisation.",
    },
    {
        "name": "Web Development Certification",
        "category": "certification",
        "issuer": "Zero To Mastery Academy",
        "year": "2022",
        "description": "JavaScript and Node.js web development.",
    },
    {
        "name": "Bertelsmann Gen-Y Tech Booster Scholarship",
        "category": "scholarship",
        "issuer": "Bertelsmann",
        "year": "2024",
        "description": "Career growth and technical upskilling programme.",
    },
    {
        "name": "AWS Machine Learning Foundations",
        "category": "scholarship",
        "issuer": "AWS / Udacity",
        "year": "2022",
        "description": "Scholarship recipient — data analysis and ML fundamentals track.",
    },
    {
        "name": "Hacktoberfest Winner",
        "category": "award",
        "issuer": "Hacktoberfest",
        "year": "2022",
        "description": "Recognised for open-source contribution.",
    },
]

EXPERIENCES = [
    {
        "company": "TracTrac",
        "role": "Lead Backend/DevOps Engineer",
        "location": "Abuja, Nigeria · On-site",
        "start_date": "2025-02",
        "end_date": None,
        "is_current": True,
        "summary": (
            "Lead backend and infrastructure engineering for TracTrac Mechanisation Services Limited, "
            "a nationwide agricultural mechanisation platform with 60k+ users."
        ),
        "highlights": [
            "Architect and operate two production FastAPI backends on shared PostgreSQL, Redis and "
            "Kafka infrastructure, with Kafka/outbox event flows, Celery workers and PgBouncer "
            "transaction pooling.",
            "Led an offline-first workflow for tractor and labour-saving-device requests in "
            "low-connectivity areas, built on idempotent create/sync APIs and batch reconciliation; "
            "it replaced a paid third-party data-collection tool.",
            "Diagnosed a dashboard screen issuing 60+ backend requests and redesigned it around SWR "
            "caching, page-1-only fetching and server-side summary endpoints, documented as an ADR.",
            "Migrated infrastructure to a self-managed Contabo VPS with Coolify, running 20+ "
            "containerised applications, and right-sized capacity through capacity modelling.",
            "Built GPS farm measurement, live vehicle tracking, wallet/payment reconciliation and "
            "reporting that reconciles platform and field data for programme monitoring and donor "
            "documentation.",
            "Lead the Young Innovators in Agricultural Mechanisation Pitch Challenge team, and trained "
            "mechanisation service providers in Nasarawa and Kaduna on the platform.",
        ],
    },
    {
        "company": "SolarAfRiC (Feexet Limited)",
        "role": "Backend/DevOps Engineer (Contract)",
        "location": "Remote · Contract",
        "start_date": "2026-04",
        "end_date": "2026-06",
        "is_current": False,
        "summary": (
            "Designed and delivered the backend for a two-sided solar equipment services marketplace, "
            "independently from architecture through production."
        ),
        "highlights": [
            "Built a 7-state booking lifecycle with Paystack escrow-style payments, technician payout "
            "wallets, bank account resolution and a dispute workflow.",
            "Engineered context-aware diagnostics on OpenAI GPT-4o-mini: vision input and structured "
            "JSON output grounded in equipment specifications, location, nearby verified technicians, "
            "lessons and booking history, with multi-turn investigation and severity escalation.",
            "Built the technician learning platform: Mux/Cloudflare video playback, quizzes, learner "
            "progress and signed PDF certificates.",
            "Implemented storage fallback (Cloudinary → S3-compatible → local) with MIME sniffing, "
            "plus WebSocket messaging and Firebase Cloud Messaging.",
        ],
    },
    {
        "company": "VITAL 2 (Ikore International Development)",
        "role": "Backend/DevOps Engineer",
        "location": "Remote",
        "start_date": "2026-05",
        "end_date": "2026-08",
        "is_current": False,
        "summary": (
            "Sole backend engineer for a livestock vaccination and farmer field-operations platform, "
            "supporting two frontend engineers."
        ),
        "highlights": [
            "Delivered a production-ready FastAPI/PostgreSQL backend within six weeks; the platform "
            "onboarded 5,000+ farmers.",
            "Built voucher campaigns and QR-code generation, contributing to a 15% increase in farmer "
            "onboarding.",
            "Implemented bulk farmer import with rollback, audit trails and role-based access control.",
            "Built offline synchronisation for field data capture, and batched mass email within "
            "Brevo's sending limits.",
        ],
    },
    {
        "company": "SUBSEL Digital Services",
        "role": "Co-Founder — Product & Engineering Lead",
        "location": "Remote",
        "start_date": "2026-09",
        "end_date": None,
        "is_current": True,
        "summary": "Co-founded a pre-launch digital services venture; I own product direction and the backend.",
        "highlights": [
            "Designed a FastAPI backend of 28 models and 26 routers covering VTU, wallet funding and "
            "withdrawals, marketplace, task earnings, referrals, challenges and merchant advertising.",
            "Integrated two payment providers (Paystack and Monify) behind one wallet, with Celery and "
            "Redis for asynchronous processing.",
            "Implemented a pay-to-activate account model.",
            "Pre-launch: no public users or revenue yet.",
        ],
    },
    {
        "company": "Join Momentum",
        "role": "Backend Developer",
        "location": "Dover, Delaware, United States · Remote",
        "start_date": "2024-06",
        "end_date": "2025-01",
        "is_current": False,
        "summary": "Backend for an AI-powered job simulation platform.",
        "highlights": [
            "Designed Django REST APIs, reducing response time by 25%.",
            "Integrated OpenAI GPT and LangChain for automated candidate feedback, and automated "
            "certificate issuance via Certifier.io.",
            "Integrated digital badge APIs over OAuth2, increasing engagement by 40%, and automated "
            "workflows that reduced errors by 30%.",
            "Mentored junior developers, two of whom progressed into key contributors.",
        ],
    },
    {
        "company": "Retiny",
        "role": "Backend/Mobile Engineer",
        "location": "Port Harcourt, Nigeria",
        "start_date": "2024-03",
        "end_date": "2024-06",
        "is_current": False,
        "summary": "Backend APIs for client products, including real estate management and stock exchange platforms.",
        "highlights": [
            "Designed APIs with Swagger documentation, 2FA, third-party OAuth and role-based mobile routes.",
            "Introduced standardised error handling and Postman testing workflows.",
            "Configured Nginx load balancing.",
        ],
    },
    {
        "company": "ALX-Africa",
        "role": "Backend/DevOps Engineer",
        "location": "Kigali, Rwanda",
        "start_date": "2023-01",
        "end_date": "2023-10",
        "is_current": False,
        "summary": "Backend/DevOps engineering placement.",
        "highlights": [
            "Built secure authentication and user-management systems.",
            "Designed database schemas shared across services.",
            "Deployed APIs on AWS EC2 with logging, validation and error tracking.",
        ],
    },
]

PROJECTS = [
    {
        "title": "TracTrac Plus — Agricultural Mechanisation Platform",
        "slug": "tractrac-platform",
        "category": "backend-systems",
        "summary": (
            "Backend and infrastructure for an on-demand farm mechanisation platform connecting farmers, "
            "mechanisation service providers, field agents and operations teams."
        ),
        "tech_stack": (
            "FastAPI, PostgreSQL, PostGIS, PgBouncer, Redis, Kafka, Celery, WebSockets, Docker, Coolify, "
            "Next.js, Redux, Paystack, CommCare"
        ),
        "challenge": (
            "Field agents work where connectivity can't be assumed, yet bookings, farm measurements, job "
            "status and payments must reach the backend exactly once and reconcile with what happened "
            "in the field."
        ),
        "engineered": (
            "Offline-first request workflow with idempotent create/sync APIs and batch reconciliation. "
            "Kafka/outbox event flows, Redis caching and Celery workers across two FastAPI backends, with "
            "PgBouncer in front of PostgreSQL/PostGIS. GPS farm measurement, live vehicle tracking, "
            "wallet and payment reconciliation, CommCare integration and Excel exports for operations."
        ),
        "impact": (
            "Two production backends serving 60k+ users. The offline-first workflow replaced a paid "
            "third-party data-collection tool and extended the platform to communities without reliable "
            "connectivity."
        ),
        "facts": ["60k+ users", "2 production FastAPI backends", "20+ containerised apps operated"],
        "featured": True,
    },
    {
        "title": "SolarAfRiC — Solar Services Marketplace & AI Diagnostics",
        "slug": "solarafric-platform",
        "category": "applied-ai",
        "summary": (
            "Two-sided marketplace connecting solar equipment owners with verified technicians, with "
            "AI-assisted diagnostics, escrow-style payments and a technician learning platform."
        ),
        "tech_stack": (
            "FastAPI, PostgreSQL, Alembic, OpenAI GPT-4o-mini, Paystack, WebSockets, Firebase Cloud "
            "Messaging, Mux, Cloudinary, S3-compatible storage"
        ),
        "challenge": (
            "Remote diagnosis needs grounding in the specific equipment, where it is and who can fix it. "
            "Payments must be held until work is verified, and uploads must survive a storage provider "
            "failing."
        ),
        "engineered": (
            "A diagnostic workflow that assembles equipment specifications, conversation history, location, "
            "nearby verified technicians, lessons and booking history into GPT-4o-mini calls with vision "
            "input and structured JSON output, including multi-turn investigation and severity escalation. "
            "A 7-state booking lifecycle with Paystack escrow-style payments, payout wallets, bank account "
            "resolution and disputes. An LMS with Mux/Cloudflare playback, quizzes, progress and signed PDF "
            "certificates."
        ),
        "impact": "Delivered independently, from architecture through production implementation, on a contract engagement.",
        "facts": ["14 models", "22 endpoint modules", "29 migrations", "7-state booking lifecycle"],
        "featured": True,
    },
    {
        "title": "VITAL 2 — Livestock Vaccination & Field Operations",
        "slug": "vital2-platform",
        "category": "backend-systems",
        "summary": (
            "Backend for a livestock vaccination and farmer field-operations programme, built for data "
            "capture in low-connectivity areas."
        ),
        "tech_stack": "FastAPI, PostgreSQL, Alembic, QR code generation, Brevo, RBAC, offline sync",
        "challenge": (
            "Field teams had to onboard farmers and record work offline, campaign data arrived in bulk "
            "and had to be safely reversible, and the platform had six weeks to reach production."
        ),
        "engineered": (
            "Offline synchronisation for field capture; voucher campaigns with QR generation; bulk farmer "
            "import with rollback; audit trails and role-based access control; batched mass email within "
            "Brevo's sending limits. Sole backend engineer alongside two frontend engineers."
        ),
        "impact": (
            "Production-ready within six weeks; 5,000+ farmers onboarded, with voucher/QR workflows "
            "contributing to a 15% increase in onboarding."
        ),
        "facts": ["5,000+ farmers", "24 models", "33 endpoint modules", "39 migrations"],
        "featured": True,
    },
    {
        "title": "SUBSEL — Wallet & Marketplace Platform",
        "slug": "subsel-platform",
        "category": "entrepreneurial",
        "summary": (
            "Co-founded, pre-launch digital services platform: VTU, wallets, marketplace, task earnings "
            "and referrals on one backend."
        ),
        "tech_stack": "FastAPI, PostgreSQL, Celery, Redis, Paystack, Monify",
        "challenge": (
            "VTU purchases, wallet funding and withdrawals, task earnings, referral rewards and merchant "
            "advertising all move money through one wallet and two payment providers, and have to stay "
            "consistent without the modules becoming entangled."
        ),
        "engineered": (
            "A FastAPI backend of 28 models and 26 routers: wallet funding and withdrawals across Paystack "
            "and Monify, marketplace, task earnings, referrals, challenges, merchant advertising and a "
            "pay-to-activate account model, with Celery and Redis for asynchronous work."
        ),
        "impact": "Pre-launch — no public users or revenue yet. Product ownership alongside engineering.",
        "facts": ["28 models", "26 routers", "2 payment providers", "Pre-launch"],
        "featured": True,
    },
    {
        "title": "MeetDevs — Talent–Employer Matching Platform",
        "slug": "meetdevs",
        "category": "open-source",
        "summary": "Open-source contribution to a talent-employer matching platform.",
        "tech_stack": "REST API, Pagination",
        "challenge": "The talent listing loaded every candidate at once, slowing navigation as the roster grew.",
        "engineered": "Designed a pagination API (12 talents per page) and a navigation bar for browsing results.",
        "impact": "Cut load times and improved navigation for employer–developer matching.",
        "repo_url": "https://github.com/Ayobami6/MeetDevs/",
    },
    {
        "title": "Smart Brain",
        "slug": "smart-brain",
        "category": "foundational",
        "summary": "Face-detection web application with full frontend and backend architecture.",
        "tech_stack": "React, Node.js, PostgreSQL",
        "repo_url": "https://github.com/betiniakarandut/smart-brain",
        "live_url": "https://smart-brain2024.herokuapp.com/",
    },
    {
        "title": "Estimate SBHP",
        "slug": "estimate-sbhp",
        "category": "engineering",
        "summary": (
            "Engineering tool estimating static bottom hole pressure using the Sukkar and Cornell method "
            "with 98% accuracy. Final-year Chemical Engineering project."
        ),
        "tech_stack": "Python, PostgreSQL",
        "repo_url": "https://github.com/betiniakarandut/Estimate-SBHP",
    },
    {
        "title": "Job Simulator AI – Backend",
        "slug": "job-simulator-ai",
        "category": "ai",
        "summary": (
            "API backend for an AI-powered job simulation platform: OpenAI + LangChain feedback and "
            "automated certificate issuance via Certifier.io. Reduced API response time by 25% and "
            "cut workflow errors by 30%."
        ),
        "tech_stack": "Django REST Framework, PostgreSQL, Celery, Redis, LangChain, OpenAI",
    },
    {
        "title": "YouTube Server Clone",
        "slug": "youtube-server-clone",
        "category": "system-design",
        "summary": (
            "A YouTube-like backend built to practise system design: video upload, streaming endpoints, "
            "authentication, 2FA and Nginx load balancing."
        ),
        "tech_stack": "Node.js, Express.js, Docker, Nginx, PostgreSQL",
    },
    {
        "title": "Real Estate & Stock Exchange APIs",
        "slug": "real-estate-stock-exchange-api",
        "category": "api",
        "summary": (
            "RESTful APIs and database schemas for a real estate management platform and a stock exchange "
            "platform, delivered for clients at Retiny."
        ),
        "tech_stack": "Node.js, Express.js, PostgreSQL, Swagger",
    },
    {
        "title": "OTP Gmail API Auth Flow",
        "slug": "otp-gmail-auth",
        "category": "security",
        "summary": "OTP-based authentication flow using the Gmail API for one-time password delivery.",
        "tech_stack": "Python, FastAPI, Gmail API",
    },
]

# (name, proficiency) per category. Proficiency is stored but not displayed.
SKILLS = {
    "Backend": [
        ("Python", 5), ("FastAPI", 5), ("SQLAlchemy", 5), ("Pydantic", 5), ("REST API Design", 5),
        ("Django", 4), ("Node.js", 4), ("OAuth2", 4), ("Flask", 3),
    ],
    "Data": [
        ("PostgreSQL", 5), ("SQL", 5), ("Alembic", 4), ("SQLite", 4), ("PostGIS", 3),
        ("TimescaleDB", 3), ("MySQL", 3), ("MongoDB", 3),
    ],
    "Distributed Systems": [
        ("Kafka", 4), ("Redis", 4), ("Celery", 5), ("WebSockets / Socket.IO", 4), ("Outbox Pattern", 4),
    ],
    "Cloud & DevOps": [
        ("Docker", 4), ("Docker Compose", 4), ("Linux / VPS", 4), ("Coolify", 4), ("PgBouncer", 4),
        ("Render", 4), ("CI/CD (GitHub Actions, Azure DevOps)", 4), ("Traefik", 3), ("Nginx", 3),
        ("AWS EC2", 3), ("GCP", 2),
    ],
    "Geospatial": [
        ("GPS / Geospatial Processing", 4), ("Shapely", 3), ("pyproj", 3),
    ],
    "Payments": [
        ("Paystack", 4), ("Monify", 3), ("Transaction Reconciliation", 4),
        ("Decimal-Precision Financial Calculations", 4),
    ],
    "Applied AI": [
        ("OpenAI APIs (GPT-4o-mini)", 4), ("Vision Workflows", 4), ("Structured Outputs", 4),
        ("LangChain", 3), ("LangGraph", 3),
    ],
    "Integrations": [
        ("Firebase / FCM", 4), ("CommCare", 3), ("Contentful", 3),
    ],
    "Frontend": [
        ("JavaScript", 4), ("TypeScript", 3), ("React", 4), ("Next.js", 3), ("Redux", 3),
        ("TanStack Query", 3),
    ],
}

ARTICLES = [
    {
        "title": "Offline-First Systems in Low-Connectivity Environments",
        "url": "https://betiniakarandut.hashnode.dev/offline-first-systems-low-connectivity",
        "excerpt": (
            "Engineering notes on designing for retries, synchronization, and eventual consistency when "
            "users operate in low-connectivity environments."
        ),
        "published_at": "2026-06-15",
    },
    {
        "title": "Production AI Isn't an ML Problem. It's a Systems Problem.",
        "url": "https://betiniakarandut.hashnode.dev/production-ai-isn-t-an-ml-problem-it-s-a-systems-problem",
        "excerpt": (
            "Most discussions about AI focus on models — which one is better, which benchmark is higher. "
            "After building an AI-powered diagnostic platform for solar equipment, the real lessons were "
            "about systems, not models."
        ),
        "published_at": "2026-06-02",
    },
    {
        "title": "Teaching the Revolution: Field Notes from ISSAM, Tractrac Plus, and the Future of Nigerian Agriculture",
        "url": "https://betiniakarandut.hashnode.dev/teaching-the-revolution-field-notes-from-issam-tractrac-plus-and-the-future-of-nigerian-agriculture",
        "excerpt": (
            "What happens when you stop building for users and start building with them — field notes "
            "from months spent training mechanization service providers in Nigeria."
        ),
        "published_at": "2026-05-21",
    },
    {
        "title": "When More Workers Made It Worse: Connection Pools, Shared Postgres, and Demo-Day",
        "url": "https://betiniakarandut.hashnode.dev/when-more-workers-made-it-worse-connection-pools-shared-postgres-and-demo-day",
        "excerpt": (
            "TracTrac's backends started failing intermittently during practical training camps — a "
            "debugging story about connection pools, shared Postgres, and a demo-day deadline."
        ),
        "published_at": "2026-05-11",
    },
    {
        "title": "I Deployed My First Cloud Server...",
        "url": "https://betiniakarandut.hashnode.dev/i-deployed-my-first-cloud-server-and-almost-left-it-wide-open-beginner-friendly-guide",
        "excerpt": "Beginner-friendly guide to avoiding common EC2 security mistakes.",
        "published_at": "2026-03-21",
    },
    {
        "title": "Estimating Static Bottom Hole Pressure",
        "url": "https://betiniakarandut.hashnode.dev/estimating-static-bottom-hole-pressure-sbhp-using-the-sukkar-and-cornell-method",
        "excerpt": "Engineering write-up from final-year project implementation.",
        "published_at": "2023-12-21",
    },
]
