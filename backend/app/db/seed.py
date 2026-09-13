from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.article import Article
from app.models.experience import Experience
from app.models.journey_event import JourneyEvent
from app.models.profile import Profile
from app.models.project import Project
from app.models.scholarship import Scholarship
from app.models.skill import Skill


def seed_initial_data(db: Session) -> None:
    existing_profile = db.execute(select(Profile.id)).first()
    if existing_profile:
        return

    profile = Profile(
        name="Betini Akarandut",
        title="Backend & Cloud Engineer",
        tagline=(
            "Building reliable, data-driven systems for real-world environments."
        ),
        bio=(
            "I design and operate backend systems, distributed services, and cloud infrastructure for "
            "applications at the intersection of technology, agriculture, and emerging markets. I lead "
            "backend and infrastructure work at TracTrac Mechanisation Services Limited (TracTrac), a "
            "Nigerian agricultural mechanization platform supporting farmers and service providers across "
            "low-connectivity environments — architecting two production FastAPI backends serving "
            "60,000+ registered users, offline-first field systems, geospatial services, and payment "
            "infrastructure. I've since co-founded SUBSEL Digital Services, a pre-launch venture, and "
            "earlier built production systems at SolarAfRiC, VITAL 2, and Join Momentum. "
            "\n\n"
            "My BEng in Chemical Engineering gave me a quantitative foundation in mathematics, statistics, "
            "numerical methods, mathematical modelling, and operations research before I moved into "
            "software engineering. That foundation still shapes how I approach backend work: the systems "
            "I build at TracTrac already generate and reconcile operational data — hectares mechanized, "
            "farmers reached, revenue, service delivery — and I'm pursuing advanced training in data "
            "science and decision analytics to take that data further, toward better operational and "
            "development decisions."
        ),
        location="FCT-Abuja, Nigeria",
        email="betiniakarandut@gmail.com",
        github_url="https://github.com/betiniakarandut",
        linkedin_url="https://www.linkedin.com/in/betiniakarandut/",
        hashnode_url="https://hashnode.com/@betiniakarandut",
    )
    db.add(profile)

    db.add_all(
        [
            JourneyEvent(
                title="B.Eng. Chemical Engineering — University of Port Harcourt",
                event_date="2017",
                description=(
                    "Built a quantitative foundation in calculus, probability & statistics, numerical "
                    "methods, mathematical modelling & operations research, and computer programming. "
                    "Graduated 2024, CGPA 3.72/5.00, Second Class Honours (Upper Division)."
                ),
                sort_order=1,
            ),
            JourneyEvent(
                title="Started Software Engineering",
                event_date="2022-01",
                description=(
                    "Began learning software engineering while completing Chemical Engineering — web "
                    "development (Zero To Mastery Academy) and AWS Machine Learning Foundations (Udacity)."
                ),
                sort_order=2,
            ),
            JourneyEvent(
                title="ALX Africa Software Engineering Certification",
                event_date="2022-09",
                description=(
                    "Completed ALX Africa's software engineering program, including a backend/DevOps "
                    "engineering placement in Kigali, Rwanda (Jan–Oct 2023)."
                ),
                sort_order=3,
            ),
            JourneyEvent(
                title="Early Backend Roles",
                event_date="2022-02",
                description=(
                    "Backend engineering roles at Scoplex Technologies and Retiny, building APIs, "
                    "authentication, and mobile-facing backend services."
                ),
                sort_order=4,
            ),
            JourneyEvent(
                title="Backend Developer — Join Momentum",
                event_date="2024-06",
                description=(
                    "Designed backend APIs for an AI-powered job simulation platform, through Jan 2025."
                ),
                sort_order=5,
            ),
            JourneyEvent(
                title="Lead Backend/DevOps Engineer — TracTrac",
                event_date="2025-02",
                description=(
                    "Took on backend and infrastructure leadership for a nationwide agricultural "
                    "mechanization platform — production systems operating directly in the field, not "
                    "just behind a dashboard."
                ),
                sort_order=6,
            ),
            JourneyEvent(
                title="SolarAfRiC & VITAL 2 — Data-Intensive Field Systems",
                event_date="2026-04",
                description=(
                    "Delivered production backends for an AI-assisted diagnostics platform (SolarAfRiC) "
                    "and a farmer field-operations platform (VITAL 2) — both generating operational data "
                    "under real field constraints."
                ),
                sort_order=7,
            ),
            JourneyEvent(
                title="Co-Founder — SUBSEL Digital Services",
                event_date="2026-09",
                description=(
                    "Co-founded a pre-launch digital services venture, building product and engineering "
                    "leadership experience alongside backend work."
                ),
                sort_order=8,
            ),
            JourneyEvent(
                title="Toward Data & Decision Systems",
                event_date="2026",
                description=(
                    "Pursuing advanced training in data science and decision analytics, building on "
                    "reporting infrastructure already built in production — the natural next step from "
                    "operating systems that generate data to turning that data into decisions."
                ),
                sort_order=9,
            ),
        ]
    )

    db.add_all(
        [
            Scholarship(
                name="AWS Certified Solutions Architect – Associate",
                issuer="AWS",
                year="In progress (2026)",
                description="Pursuing certification, expected 2026.",
                sort_order=1,
            ),
            Scholarship(
                name="Bertelsmann Gen-Y Tech Booster Scholarship",
                issuer="Bertelsmann",
                year="2024",
                description="Career growth and technical upskilling program.",
                sort_order=2,
            ),
            Scholarship(
                name="Software Engineering Certification",
                issuer="ALX / Holberton School",
                year="2023",
                description="Certified software engineering training covering Python, Node.js, and backend specialization.",
                sort_order=3,
            ),
            Scholarship(
                name="Web Development Certification",
                issuer="Zero To Mastery Academy",
                year="2022",
                description="JavaScript and Node.js web development certification.",
                sort_order=4,
            ),
            Scholarship(
                name="AWS Machine Learning Foundations",
                issuer="AWS / Udacity",
                year="2022",
                description="Scholarship recipient — data analysis and ML fundamentals track.",
                sort_order=5,
            ),
            Scholarship(
                name="Hacktoberfest Winner",
                issuer="Hacktoberfest",
                year="2022",
                description="Recognized for open-source contribution.",
                sort_order=6,
            ),
        ]
    )

    db.add_all(
        [
            Experience(
                company="TracTrac",
                role="Lead Backend/DevOps Engineer",
                location="Abuja, Nigeria · On-site",
                start_date="2025-02",
                end_date=None,
                is_current=True,
                summary=(
                    "Architect and operate two production FastAPI backends for TracTrac Mechanisation "
                    "Services Limited (TracTrac), a nationwide agricultural mechanization and logistics "
                    "platform serving 60,000+ registered users. Led an offline-first system for tractor "
                    "and labour-saving-device requests in low-connectivity areas, expanding digital access "
                    "for remote farming communities and replacing a paid third-party data-collection tool. "
                    "Built reporting infrastructure that reconciles platform and field data for monitoring "
                    "hectares mechanized, farmers reached, revenue, cooperatives, states, and service "
                    "delivery. Built GPS-based farm measurement and offline synchronization/reconciliation "
                    "workflows, alongside payment, notification, and operational systems. Provisioned and "
                    "migrated infrastructure to a self-managed Contabo VPS and Coolify, running 20+ "
                    "containerized applications and reducing infrastructure costs through capacity "
                    "modelling and right-sizing. Designed Kafka/outbox event flows, Redis caching, "
                    "PostgreSQL/PostGIS infrastructure, Celery workers, and PgBouncer transaction pooling. "
                    "Diagnosed a production dashboard issue involving intermittent failures under load, "
                    "driven by request fan-out; investigated database performance, caching, locking, "
                    "pagination, and aggregate-query behavior, then redesigned the dashboard around "
                    "page-scoped fetching and server-computed, cached summaries while preserving the "
                    "existing response contract — documented as an ADR. Provided field and technical "
                    "support and trained mechanization service providers in Nasarawa and Kaduna on the "
                    "technology supporting smallholder farmers. Deliver monthly and quarterly technical "
                    "reporting supporting program monitoring and donor documentation."
                ),
                sort_order=1,
            ),
            Experience(
                company="SolarAfRiC (Feexet Limited)",
                role="Backend/DevOps Engineer (Contract)",
                location="Remote · Contract",
                start_date="2026-04",
                end_date="2026-06",
                is_current=False,
                summary=(
                    "Engineered backend infrastructure for an AI-assisted solar equipment diagnostics "
                    "platform integrating vision inputs, structured LLM outputs, equipment/location data, "
                    "and technician context. Built escrow-style payments, technician communication, "
                    "file-storage fallback, and learning-management workflows end-to-end, delivered "
                    "independently from architecture through production implementation."
                ),
                sort_order=2,
            ),
            Experience(
                company="VITAL 2 (Ikore International Development)",
                role="Backend/DevOps Engineer",
                location="Remote",
                start_date="2026-05",
                end_date="2026-08",
                is_current=False,
                summary=(
                    "Delivered a production-ready farmer field-operations platform within six weeks, "
                    "supporting offline data capture in low-connectivity areas and onboarding 5,000+ "
                    "farmers. Built voucher and QR-code workflows contributing to a 15% increase in "
                    "farmer onboarding, alongside bulk data import with rollback and audit trails. Served "
                    "as the sole backend engineer supporting two frontend engineers, owning backend "
                    "updates, bug resolution, production support, and post-review improvements."
                ),
                sort_order=3,
            ),
            Experience(
                company="SUBSEL Digital Services",
                role="Co-Founder — Product & Engineering Lead",
                location="Remote",
                start_date="2026-09",
                end_date=None,
                is_current=True,
                summary=(
                    "Co-founded a digital services venture — vision: \"Where Innovation Meets "
                    "Opportunity.\" Building platform infrastructure spanning marketplace, payments, "
                    "subscriptions, rewards, and commission workflows, developed alongside my younger "
                    "brother as part of supporting his professional development in digital marketing. "
                    "Pre-launch: no public users or revenue yet."
                ),
                sort_order=4,
            ),
            Experience(
                company="Join Momentum",
                role="Backend Developer",
                location="Dover, Delaware, United States · Remote",
                start_date="2024-06",
                end_date="2025-01",
                is_current=False,
                summary=(
                    "Designed scalable Django REST APIs for an AI-powered Job Simulator platform, reducing "
                    "response time by 25% and integrating OpenAI GPT and LangChain for automated candidate "
                    "feedback. Integrated secure digital badge APIs using OAuth2, increasing engagement by "
                    "40%, while automating workflows that reduced errors by 30%. Mentored junior "
                    "developers, two of whom progressed into key contributors, while collaborating within "
                    "Agile Scrum teams."
                ),
                sort_order=5,
            ),
            Experience(
                company="Retiny",
                role="Backend/Mobile Engineer",
                location="Port Harcourt, Nigeria",
                start_date="2024-03",
                end_date="2024-06",
                is_current=False,
                summary=(
                    "Designed APIs with Swagger docs, 2FA, third-party OAuth, and role-based mobile "
                    "routes; introduced standardized error handling, Postman testing workflows, and Nginx "
                    "load balancing."
                ),
                sort_order=6,
            ),
            Experience(
                company="ALX-Africa",
                role="Backend/DevOps Engineer",
                location="Kigali, Rwanda",
                start_date="2023-01",
                end_date="2023-10",
                is_current=False,
                summary=(
                    "Built secure authentication and user-management systems, designed cross-service "
                    "database schemas, and deployed APIs on AWS EC2 with logging, validation, and error "
                    "tracking."
                ),
                sort_order=7,
            ),
        ]
    )

    db.add_all(
        [
            Project(
                title="TracTrac — Agricultural Platform Backend",
                slug="tractrac-platform",
                category="backend-systems",
                summary=(
                    "Production backend and distributed systems for TracTrac Mechanisation Services "
                    "Limited, a nationwide agricultural mechanization and logistics platform serving "
                    "60,000+ registered users."
                ),
                tech_stack="FastAPI, PostgreSQL, PostGIS, Kafka, Redis, PgBouncer, Celery, Docker, Paystack",
                challenge=(
                    "Field agents and farmers often operate with little or no connectivity, and the "
                    "platform needed to reliably synchronize GPS farm measurements, bookings, and payments "
                    "across two backend services — while also turning platform and field data into "
                    "operational reporting that program partners could rely on."
                ),
                engineered=(
                    "Led an offline-first system for tractor and labour-saving-device requests in "
                    "low-connectivity areas, replacing a paid third-party data-collection tool. Built "
                    "reporting infrastructure reconciling platform and field data to monitor hectares "
                    "mechanized, farmers reached, revenue, cooperatives, and service delivery. Designed "
                    "Kafka/outbox event flows, Redis caching, PgBouncer transaction pooling in front of "
                    "PostgreSQL/PostGIS, and Celery-based asynchronous processing. Provisioned and "
                    "migrated infrastructure to a self-managed Contabo VPS and Coolify, running 20+ "
                    "containerized applications."
                ),
                impact=(
                    "Two production FastAPI backends now serve 60,000+ registered users, with an "
                    "offline-first system expanding digital access for remote farming communities and "
                    "operational reporting supporting program monitoring and donor documentation."
                ),
                featured=True,
                sort_order=1,
            ),
            Project(
                title="SolarAfRiC — AI Diagnostics & Payments Platform",
                slug="solarafric-platform",
                category="applied-ai",
                summary=(
                    "Backend for a solar equipment service platform combining context-aware AI diagnostics "
                    "with escrow-style payments and real-time technician communication."
                ),
                tech_stack="Python, FastAPI, OpenAI (vision + structured outputs), PostgreSQL, WebSockets, Firebase Cloud Messaging",
                challenge=(
                    "Diagnosing solar equipment issues remotely takes more than a chatbot — it needs "
                    "grounding in the specific equipment, its location, technician availability, and prior "
                    "booking history, while payments between customers, technicians, and the platform need "
                    "to be held safely until work is verified."
                ),
                engineered=(
                    "Built an application layer around an LLM combining vision input, structured outputs, "
                    "and equipment, location, and technician context. Engineered escrow-style payments, "
                    "technician communication, a file-storage fallback, and learning-management workflows "
                    "end-to-end."
                ),
                impact=(
                    "Delivered independently, from architecture through production implementation, as a "
                    "backend/DevOps contract engagement."
                ),
                featured=True,
                sort_order=2,
            ),
            Project(
                title="VITAL 2 — Farmer Field Operations Platform",
                slug="vital2-platform",
                category="backend-systems",
                summary=(
                    "Backend for a farmer support program's field operations, covering offline data "
                    "capture, voucher campaigns, and bulk data integrity."
                ),
                tech_stack="Python, PostgreSQL, QR code generation, offline-sync architecture",
                challenge=(
                    "Field agents onboarding farmers in low-connectivity rural areas needed to keep "
                    "working offline, campaign/voucher data imported in bulk needed to be safe to roll "
                    "back when it went wrong, and the platform had to reach production within a six-week "
                    "window."
                ),
                engineered=(
                    "Designed offline data-capture workflows for low-connectivity environments, "
                    "voucher and QR-code workflows, and bulk data import with rollback and audit trails "
                    "— as the sole backend engineer supporting two frontend engineers."
                ),
                impact=(
                    "Delivered production-ready within six weeks; onboarded 5,000+ farmers, with "
                    "voucher/QR workflows contributing to a 15% increase in farmer onboarding."
                ),
                featured=True,
                sort_order=3,
            ),
            Project(
                title="SUBSEL Digital Services",
                slug="subsel-platform",
                category="entrepreneurial",
                summary=(
                    "Co-founded, pre-launch digital services venture — marketplace, payments, "
                    "subscriptions, and rewards infrastructure."
                ),
                tech_stack="React, TypeScript, PostgreSQL, wallet & payment provider integrations",
                challenge=(
                    "Building a platform from zero as a founder rather than an employee — architecting a "
                    "wallet ledger, multiple payment providers, and a subscription lifecycle alongside a "
                    "referral system, without the marketplace and payments logic becoming tangled, while "
                    "also owning product direction."
                ),
                engineered=(
                    "Co-founded with my younger brother; building wallet-ledger and marketplace "
                    "infrastructure spanning subscriptions, rewards, and payment-provider integrations, "
                    "kept cleanly decoupled by design."
                ),
                impact=(
                    "Pre-launch: demonstrates product ownership, engineering leadership, and "
                    "entrepreneurial execution — no public users or revenue yet."
                ),
                featured=True,
                sort_order=4,
            ),
            Project(
                title="MeetDevs — Talent–Employer Matching Platform",
                slug="meetdevs",
                category="open-source",
                summary="Open-source contribution to a talent-employer matching platform.",
                tech_stack="REST API, Pagination",
                challenge=(
                    "The platform's talent listing loaded every candidate at once, slowing navigation as "
                    "the roster grew."
                ),
                engineered=(
                    "Designed a pagination API (12 talents per page) and built a user-friendly navigation "
                    "bar to improve employer-developer connections."
                ),
                impact="Cut load times and improved navigation for employer–developer matching.",
                repo_url="https://github.com/Ayobami6/MeetDevs/",
                featured=False,
                sort_order=5,
            ),
            Project(
                title="Smart Brain",
                slug="smart-brain",
                category="foundational",
                summary="Face-detection web application with full frontend and backend architecture.",
                tech_stack="React, Node.js, PostgreSQL",
                repo_url="https://github.com/betiniakarandut/smart-brain",
                live_url="https://smart-brain2024.herokuapp.com/",
                featured=False,
                sort_order=6,
            ),
            Project(
                title="Estimate SBHP",
                slug="estimate-sbhp",
                category="engineering",
                summary=(
                    "Engineering tool estimating static bottom hole pressure using the Sukkar and Cornell "
                    "method with 98% accuracy. Final-year Chemical Engineering project."
                ),
                tech_stack="Python, PostgreSQL",
                repo_url="https://github.com/betiniakarandut/Estimate-SBHP",
                featured=False,
                sort_order=7,
            ),
            Project(
                title="Job Simulator AI – Backend",
                slug="job-simulator-ai",
                category="ai",
                summary=(
                    "Scalable API backend for an AI-powered job simulation platform. "
                    "Integrated OpenAI + LangChain for simulation feedback and automated certificate issuance via Certifier.io. "
                    "Reduced API response time by 25% and automated critical workflows, cutting errors by 30%."
                ),
                tech_stack="Django REST Framework, PostgreSQL, Celery, Redis, LangChain, OpenAI",
                repo_url=None,
                live_url=None,
                featured=False,
                sort_order=8,
            ),
            Project(
                title="YouTube Server Clone",
                slug="youtube-server-clone",
                category="system-design",
                summary=(
                    "A YouTube-like backend server built to sharpen system design skills. "
                    "Features video upload, streaming endpoints, user authentication, 2FA, and Nginx load balancing."
                ),
                tech_stack="Node.js, Express.js, Docker, Nginx, PostgreSQL",
                repo_url=None,
                live_url=None,
                featured=False,
                sort_order=9,
            ),
            Project(
                title="Real Estate & Stock Exchange APIs",
                slug="real-estate-stock-exchange-api",
                category="api",
                summary=(
                    "Designed and implemented RESTful APIs and database schemas for a real estate management platform "
                    "and a stock exchange platform. Delivered for clients during internship at Retiny."
                ),
                tech_stack="Node.js, Express.js, PostgreSQL, Swagger",
                repo_url=None,
                live_url=None,
                featured=False,
                sort_order=10,
            ),
            Project(
                title="OTP Gmail API Auth Flow",
                slug="otp-gmail-auth",
                category="security",
                summary="OTP-based authentication flow using the Gmail API — secure one-time password delivery for user verification.",
                tech_stack="Python, FastAPI, Gmail API",
                repo_url=None,
                live_url=None,
                featured=False,
                sort_order=11,
            ),
        ]
    )

    db.add_all(
        [
            # Backend
            Skill(name="Python", category="Backend", proficiency=5),
            Skill(name="FastAPI", category="Backend", proficiency=5),
            Skill(name="Django", category="Backend", proficiency=4),
            Skill(name="Flask", category="Backend", proficiency=3),
            Skill(name="Node.js", category="Backend", proficiency=4),
            Skill(name="REST API Design", category="Backend", proficiency=5),
            Skill(name="WebSockets / Socket.IO", category="Backend", proficiency=4),
            Skill(name="OAuth2", category="Backend", proficiency=4),
            # Data
            Skill(name="PostgreSQL", category="Data", proficiency=5),
            Skill(name="TimescaleDB", category="Data", proficiency=3),
            Skill(name="Redis", category="Data", proficiency=4),
            Skill(name="MySQL", category="Data", proficiency=3),
            Skill(name="MongoDB", category="Data", proficiency=3),
            # Distributed Systems
            Skill(name="Kafka", category="Distributed Systems", proficiency=4),
            Skill(name="Outbox Pattern", category="Distributed Systems", proficiency=4),
            Skill(name="Celery", category="Distributed Systems", proficiency=5),
            # Geospatial
            Skill(name="PostGIS", category="Geospatial", proficiency=3),
            Skill(name="Shapely", category="Geospatial", proficiency=3),
            Skill(name="pyproj", category="Geospatial", proficiency=3),
            Skill(name="GPS / Geospatial Processing", category="Geospatial", proficiency=4),
            # Payments
            Skill(name="Paystack", category="Payments", proficiency=4),
            Skill(name="Transaction Reconciliation", category="Payments", proficiency=4),
            Skill(name="Decimal-Precision Financial Calculations", category="Payments", proficiency=4),
            # Cloud & Infrastructure
            Skill(name="Docker", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="Linux / VPS", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="Traefik", category="Cloud & Infrastructure", proficiency=3),
            Skill(name="Nginx", category="Cloud & Infrastructure", proficiency=3),
            Skill(name="Coolify", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="Render", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="AWS EC2", category="Cloud & Infrastructure", proficiency=3),
            Skill(name="GCP", category="Cloud & Infrastructure", proficiency=2),
            # DevOps
            Skill(name="Alembic", category="DevOps", proficiency=4),
            Skill(name="PgBouncer", category="DevOps", proficiency=4),
            Skill(name="CI/CD (GitHub Actions, Azure DevOps)", category="DevOps", proficiency=4),
            Skill(name="Health Checks", category="DevOps", proficiency=4),
            # Integrations
            Skill(name="Firebase / FCM", category="Integrations", proficiency=4),
            Skill(name="OpenAI (Vision & Structured Outputs)", category="Integrations", proficiency=4),
            Skill(name="LangChain", category="Integrations", proficiency=3),
            Skill(name="LangGraph", category="Integrations", proficiency=3),
            Skill(name="Contentful", category="Integrations", proficiency=3),
            # Frontend
            Skill(name="React", category="Frontend", proficiency=4),
            Skill(name="TypeScript", category="Frontend", proficiency=3),
            Skill(name="JavaScript", category="Frontend", proficiency=4),
            Skill(name="Next.js", category="Frontend", proficiency=3),
        ]
    )

    db.add_all(
        [
            Article(
                title="I Deployed My First Cloud Server...",
                source="Hashnode",
                url="https://betiniakarandut.hashnode.dev/i-deployed-my-first-cloud-server-and-almost-left-it-wide-open-beginner-friendly-guide",
                excerpt="Beginner-friendly guide to avoiding common EC2 security mistakes.",
                published_at="2026-03-21",
            ),
            Article(
                title="Estimating Static Bottom Hole Pressure",
                source="Hashnode",
                url="https://betiniakarandut.hashnode.dev/estimating-static-bottom-hole-pressure-sbhp-using-the-sukkar-and-cornell-method",
                excerpt="Engineering write-up from final-year project implementation.",
                published_at="2023-12-21",
            ),
        ]
    )

    db.commit()
