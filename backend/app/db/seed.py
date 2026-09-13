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
            "I design, build, deploy, and operate production systems across distributed backends, "
            "cloud infrastructure, databases, payments, and real-time platforms."
        ),
        bio=(
            "I'm a Backend & Cloud Engineer with 3+ years designing, building, deploying, and operating "
            "production systems. I currently run two production FastAPI backends at TracTrac serving "
            "60,000+ registered users on a nationwide agricultural mechanization and logistics platform, "
            "and build backend services for the Job Simulator AI platform at Join Momentum. Recent "
            "engagements include SolarAfRiC (context-aware AI diagnostics and escrow-style payments), "
            "VITAL 2 (offline-sync field operations that onboarded 5,000+ farmers), and SUBSEL (wallet "
            "and VTU infrastructure). "
            "\n\n"
            "I started in Chemical Engineering before transitioning into backend engineering through ALX "
            "Africa. Today I focus on the parts of a system that have to hold up in production — data "
            "consistency, caching strategy, deployment hardening, and cost-efficient infrastructure: at "
            "TracTrac alone, capacity modeling and right-sized infrastructure cut hosting costs by 60%, "
            "while an offline-first system I proposed and led fully replaced a paid third-party "
            "data-collection tool, eliminating ₦5M+ in annual third-party costs."
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
                title="Tech Journey Started",
                event_date="2022-01-14",
                description="Started learning software engineering while studying 400L Chemical Engineering.",
                sort_order=1,
            ),
            JourneyEvent(
                title="Web Developer Course – Zero To Mastery Academy",
                event_date="2022-01-14",
                description="Studied web development with JavaScript and Node.js through Zero To Mastery Academy, completing certification in late March 2022.",
                sort_order=2,
            ),
            JourneyEvent(
                title="Python Developer Intern – Scoplex Technologies",
                event_date="2022-02",
                description="First professional role at an oil servicing company in Port Harcourt.",
                sort_order=3,
            ),
            JourneyEvent(
                title="AWS ML Foundations – Udacity",
                event_date="2022-08",
                description="Completed AWS Machine Learning Foundations apprenticeship.",
                sort_order=4,
            ),
            JourneyEvent(
                title="ALX Software Engineering Program",
                event_date="2022-09",
                description="Began a comprehensive software engineering training program with ALX Africa, including a backend/DevOps engineering placement in Kigali, Rwanda.",
                sort_order=5,
            ),
            JourneyEvent(
                title="Graduated ALX Software Engineering",
                event_date="2023-11",
                description="Completed ALX program, specializing in backend development for the final months.",
                sort_order=6,
            ),
            JourneyEvent(
                title="Joined United People Global",
                event_date="2023-12",
                description="Became a full-time member contributing to UN Sustainable Development Goals.",
                sort_order=7,
            ),
            JourneyEvent(
                title="Extern – Market Research Analyst",
                event_date="2024-03",
                description="Completed a research internship identifying top policy influencers in North America across Environment, Labor, and Community Impact domains.",
                sort_order=8,
            ),
            JourneyEvent(
                title="Backend/Mobile Engineer – Retiny",
                event_date="2024-03",
                description="Designed a YouTube-style API with Swagger docs, 2FA, third-party OAuth, and role-based mobile routes; introduced error-handling standards and Nginx load balancing.",
                sort_order=9,
            ),
            JourneyEvent(
                title="Back End Developer – Join Momentum",
                event_date="2024-06",
                description="Joined Join Momentum designing scalable APIs for the Job Simulator AI platform.",
                sort_order=10,
            ),
            JourneyEvent(
                title="Extern Ambassador",
                event_date="2024-04",
                description="Became a full-time Extern Ambassador, representing the platform in the US remotely.",
                sort_order=11,
            ),
            JourneyEvent(
                title="Lead Backend/DevOps Engineer – TracTrac",
                event_date="2025-02",
                description="Took on a lead backend/DevOps role architecting and operating production systems for a nationwide agricultural mechanization and logistics platform.",
                sort_order=12,
            ),
            JourneyEvent(
                title="Backend/DevOps Contract – SolarAfRiC (Feexet Limited)",
                event_date="2026-04",
                description="Began a backend/DevOps contract engineering, solo and end-to-end, the backend behind SolarAfRiC's context-aware AI diagnostics and escrow-style payment platform.",
                sort_order=13,
            ),
            JourneyEvent(
                title="Backend/DevOps Engineer – VITAL 2 (Ikore International Development)",
                event_date="2026-05",
                description="Delivered a production-ready farmer field operations platform within 6 weeks of program flag-off, onboarding 5,000+ farmers.",
                sort_order=14,
            ),
            JourneyEvent(
                title="Fullstack Engineer – SUBSEL",
                event_date="2026-07",
                description="Took on a fullstack role at SUBSEL, building wallet-ledger, VTU, and marketplace infrastructure.",
                sort_order=15,
            ),
            JourneyEvent(
                title="60% Infrastructure Cost Reduction at TracTrac",
                event_date="2026-09",
                description="TracTrac's platform now serves 60,000+ registered users across two production FastAPI backends; capacity modeling and right-sized infrastructure cut hosting costs by 60%.",
                sort_order=16,
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
                issuer="ALX-Holberton School",
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
                description="AWS Machine Learning Foundations track — data analysis and ML fundamentals.",
                sort_order=5,
            ),
            Scholarship(
                name="Hacktoberfest'22 Winner",
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
                    "Architect and operate two production FastAPI backends serving 60,000+ registered "
                    "users on a nationwide agricultural mechanization and logistics platform. Proposed and "
                    "led design/implementation of an offline-first system for tractor and labour-saving-device "
                    "requests in low-connectivity areas — now the platform's highest demand-generation and "
                    "fulfillment channel for remote farmers, fully replacing the paid third-party (CommCare) "
                    "data-collection tool. Provisioned a Contabo VPS from scratch in 4 days (first use of "
                    "the stack) and manage DevOps for 20+ containerized apps with health checks and "
                    "migration-gated rollouts; cut infrastructure costs by 60% via capacity modeling "
                    "(10 → 500+ concurrent users) and right-sized vertical scaling. Designed Kafka + "
                    "outbox-pattern event flows, Redis caching (incl. JWT hot-path), and PgBouncer "
                    "transaction pooling over PostgreSQL/PostGIS for reliable cross-service messaging. "
                    "Built GPS-based 'Measure a Farm' and offline sync/reconciliation workflows; integrated "
                    "Paystack with automated reconciliation, 20+ operational dashboards, and real-time "
                    "notifications (Socket.IO, Firebase). Diagnosed a dashboard firing 60+ backend requests "
                    "per load; redesigned it around page-scoped fetching and server-computed summaries, "
                    "documented as an ADR to prevent regression. Deliver monthly and quarterly technical "
                    "reports for Mastercard Foundation (donor) documentation and ETK monitoring under the "
                    "ISSAM program."
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
                    "Engineered the backend for a context-aware AI diagnostics platform (vision input, "
                    "structured LLM outputs, equipment/location/technician/LMS context) in active production "
                    "for solar equipment servicing. Built an escrow-style payment lifecycle with payout "
                    "wallets, bank resolution, and dispute workflows, holding customer funds safely until "
                    "work verification. Implemented real-time technician chat (WebSockets + FCM push), a "
                    "3-tier file storage fallback, and an LMS with automated certificate generation — "
                    "delivered solo, end-to-end."
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
                    "Delivered a production-ready farmer field operations platform within 6 weeks of "
                    "program flag-off; 5,000+ farmers onboarded via offline data capture in low-connectivity "
                    "areas. Ran voucher campaigns with QR-code workflows driving a 15% lift in farmer "
                    "onboarding; built bulk data import with rollback and audit trails for field data "
                    "integrity. Sole backend engineer serving 2 frontend engineers (mobile & web); "
                    "represented the team during peak periods, owning update requests, bug fixes, and "
                    "post-review user feedback."
                ),
                sort_order=3,
            ),
            Experience(
                company="SUBSEL",
                role="Fullstack Engineer",
                location="Remote",
                start_date="2026-07",
                end_date="2026-09",
                is_current=False,
                summary=(
                    "Built wallet-ledger and VTU infrastructure spanning subscriptions, rewards marketplace, "
                    "multiple payment-provider integrations, and referral/commission logic, kept cleanly "
                    "decoupled by design. Implemented asynchronous processing for payment and provisioning "
                    "flows across backend services and a React/TypeScript frontend."
                ),
                sort_order=4,
            ),
            Experience(
                company="Join Momentum",
                role="Back End Developer",
                location="Dover, Delaware, United States · Remote",
                start_date="2024-06",
                end_date=None,
                is_current=True,
                summary=(
                    "Designed scalable APIs for the Job Simulator AI platform (Django REST Framework), "
                    "reducing response time by 25%; integrated OpenAI GPT + LangChain for automated "
                    "candidate feedback. Integrated digital badge APIs with secure OAuth2, boosting "
                    "engagement by 40%; automated critical workflows, reducing errors by 30%. Mentored "
                    "junior developers — two became key contributors — and collaborated in Agile Scrum "
                    "sprints (Contentful CMS integration)."
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
                    "Designed a YouTube-style API (Swagger, 2FA, third-party OAuth, role-based mobile "
                    "routes); introduced error-handling standards, Postman testing workflows, and Nginx "
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
                    "Spearheaded secure authentication and user management; designed cross-service "
                    "database schema; deployed APIs on AWS EC2 with logging, validation layers, and error "
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
                    "Production backend and distributed systems for a nationwide agricultural mechanization "
                    "and logistics platform serving 60,000+ registered users."
                ),
                tech_stack="FastAPI, PostgreSQL, PostGIS, Kafka, Redis, PgBouncer, Docker, Paystack",
                challenge=(
                    "Field agents and farmers often operate with little or no connectivity, and the "
                    "platform needed to reliably synchronize GPS farm measurements, bookings, and payments "
                    "across two backend services without losing data or double-processing events — while "
                    "infrastructure spend had to stay lean on self-managed VPS hosting."
                ),
                engineered=(
                    "Proposed and led an offline-first system for tractor and labour-saving-device requests "
                    "in low-connectivity areas, fully replacing a paid third-party (CommCare) data-collection "
                    "tool. Designed Kafka and outbox-pattern event flows for reliable cross-service "
                    "messaging, Redis caching (including JWT hot-path caching), and PgBouncer transaction-mode "
                    "pooling in front of PostgreSQL/PostGIS. Built GPS-based farm measurement, 20+ operational "
                    "dashboards, and provisioned a Contabo VPS from scratch to run 20+ containerized apps with "
                    "health checks and migration-gated rollouts. Diagnosed a dashboard generating 60+ backend "
                    "requests per load and redesigned its loading architecture, and cut infrastructure costs "
                    "60% via capacity modeling (10 to 500+ concurrent users) and right-sized scaling."
                ),
                impact=(
                    "Two production FastAPI backends now serve 60,000+ registered users; the offline-first "
                    "system became the platform's highest demand-generation channel while eliminating ₦5M+ "
                    "in annual third-party costs, and infrastructure spend dropped 60%."
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
                    "Built an application layer around an LLM combining vision input, structured JSON "
                    "outputs, and equipment, location, technician, and LMS context to produce context-aware "
                    "diagnostic assistance with safety/severity escalation. Engineered an escrow-style "
                    "payment lifecycle with payout wallets, bank resolution, and a dispute workflow, a "
                    "3-tier file storage fallback, real-time WebSocket chat with FCM push notifications, "
                    "and an LMS with certificate generation."
                ),
                impact=(
                    "Delivered solo, end-to-end, as a backend/DevOps contract engagement now in active "
                    "production use for solar equipment diagnostics, bookings, and payments."
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
                    "Field agents onboarding farmers in low-connectivity rural areas needed to keep working "
                    "offline, campaign/voucher data imported in bulk needed to be safe to roll back when "
                    "it went wrong, and the platform had to reach production within a 6-week program window."
                ),
                engineered=(
                    "Designed offline-sync field operations workflows for low-connectivity environments, "
                    "voucher-based campaign workflows with QR code generation, bulk data import with "
                    "rollback, and audit trails for field data integrity — as the sole backend engineer "
                    "serving 2 frontend engineers (mobile & web)."
                ),
                impact=(
                    "Delivered production-ready within 6 weeks of program flag-off; onboarded 5,000+ "
                    "farmers, with voucher/QR campaigns driving a 15% lift in farmer onboarding."
                ),
                featured=True,
                sort_order=3,
            ),
            Project(
                title="SUBSEL — Digital Services & Wallet Platform",
                slug="subsel-platform",
                category="fullstack",
                summary=(
                    "Fullstack engineering on a digital services platform spanning wallet infrastructure, "
                    "VTU, subscriptions, and a rewards marketplace."
                ),
                tech_stack="React, TypeScript, PostgreSQL, wallet & payment provider integrations",
                challenge=(
                    "The platform needed to support a wallet ledger, multiple payment providers, and a "
                    "subscription/activation lifecycle alongside a referral and commission system, without "
                    "the marketplace and payments logic becoming tangled."
                ),
                engineered=(
                    "Built wallet-ledger and VTU infrastructure spanning subscriptions, rewards marketplace, "
                    "multiple payment-provider integrations, and referral/commission logic kept cleanly "
                    "decoupled by design, plus asynchronous processing for payment and provisioning flows "
                    "across backend services and a React/TypeScript frontend."
                ),
                impact="Built full-time from July to September 2026.",
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
            Skill(name="WebSockets", category="Backend", proficiency=4),
            Skill(name="OAuth2", category="Backend", proficiency=4),
            # Data
            Skill(name="PostgreSQL", category="Data", proficiency=5),
            Skill(name="PostGIS", category="Data", proficiency=4),
            Skill(name="Redis", category="Data", proficiency=4),
            Skill(name="MySQL", category="Data", proficiency=3),
            Skill(name="MongoDB", category="Data", proficiency=3),
            # Distributed Systems
            Skill(name="Kafka", category="Distributed Systems", proficiency=4),
            Skill(name="Outbox Pattern", category="Distributed Systems", proficiency=4),
            Skill(name="Celery", category="Distributed Systems", proficiency=5),
            # Cloud & Infrastructure
            Skill(name="Docker", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="Linux / VPS", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="Render", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="Coolify", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="AWS EC2", category="Cloud & Infrastructure", proficiency=3),
            Skill(name="GCP", category="Cloud & Infrastructure", proficiency=2),
            # DevOps
            Skill(name="Alembic", category="DevOps", proficiency=4),
            Skill(name="PgBouncer", category="DevOps", proficiency=4),
            Skill(name="CI/CD", category="DevOps", proficiency=4),
            Skill(name="Health Checks", category="DevOps", proficiency=4),
            # Integrations
            Skill(name="Paystack", category="Integrations", proficiency=4),
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
