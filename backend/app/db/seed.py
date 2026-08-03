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
            "I'm a Backend & Cloud Engineer currently operating production systems across four companies. "
            "At TracTrac, I help run two production FastAPI backends serving 100,000+ registered users on "
            "a nationwide agricultural mechanization and logistics platform — offline-first field workflows, "
            "Kafka and outbox-pattern event flows, Redis caching, and PgBouncer-pooled PostgreSQL/PostGIS at "
            "the core. At SolarAfRiC (Feexet Limited), I engineer the backend behind a context-aware AI "
            "diagnostics system, escrow-style payments, and real-time technician chat. At VITAL 2 (Ikore "
            "International Development), I built offline-sync field operations that has onboarded 5,000+ "
            "farmers. At SUBSEL, I work full-stack on wallet, VTU, and marketplace infrastructure. "
            "\n\n"
            "I started in Chemical Engineering before transitioning into backend engineering through ALX "
            "Africa's software engineering program. Today I focus on the parts of a system that have to "
            "hold up in production: data consistency, caching strategy, deployment hardening, and the "
            "operational reality of running services under real-world constraints."
        ),
        location="FCT-Abuja, Nigeria",
        github_url="https://github.com/betiniakarandut",
        linkedin_url="https://www.linkedin.com/in/betini-akarandut/",
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
                description="Began a comprehensive one-year software engineering training (Python & Node.js) with ALX Africa.",
                sort_order=5,
            ),
            JourneyEvent(
                title="Graduated ALX Software Engineering",
                event_date="2023-11",
                description="Completed ALX program, specializing in backend development for the final three months.",
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
                title="Backend Developer Intern – Retiny",
                event_date="2024-03",
                description="Built YouTube-like server, financial platform APIs, real estate APIs, and stock exchange APIs. Implemented 2FA and load balancing with Nginx.",
                sort_order=9,
            ),
            JourneyEvent(
                title="Backend Developer Intern – Join Momentum",
                event_date="2024-07",
                description="Designed scalable APIs for the Job Simulator AI platform, reducing response time by 25%. Automated workflows and mentored junior developers.",
                sort_order=10,
            ),
            JourneyEvent(
                title="Extern Ambassador",
                event_date="2024-04",
                description="Became a full-time Extern Ambassador, representing the platform in the US remotely.",
                sort_order=11,
            ),
            JourneyEvent(
                title="Promoted to Full-time – Join Momentum",
                event_date="2025-01-14",
                description="Promoted from intern to full-time Back End Developer at Join Momentum.",
                sort_order=12,
            ),
            JourneyEvent(
                title="Lead Backend/DevOps Engineer – TracTrac",
                event_date="2025-02",
                description="Took on a lead backend/DevOps role architecting and operating production systems for a nationwide agricultural mechanization and logistics platform.",
                sort_order=13,
            ),
            JourneyEvent(
                title="Backend/DevOps Contract – SolarAfRiC (Feexet Limited)",
                event_date="2026-05",
                description="Began a backend/DevOps contract engineering the backend behind SolarAfRiC's context-aware AI diagnostics and escrow-style payment platform.",
                sort_order=14,
            ),
            JourneyEvent(
                title="Backend/DevOps Engineer – VITAL 2 (Ikore International Development)",
                event_date="2026",
                description="Joined part-time on VITAL 2, building offline-sync field operations for farmer support work that has onboarded 5,000+ farmers.",
                sort_order=15,
            ),
            JourneyEvent(
                title="Fullstack Engineer – SUBSEL",
                event_date="2026-07",
                description="Took on a full-time fullstack role at SUBSEL, building wallet, VTU, and marketplace infrastructure.",
                sort_order=16,
            ),
            JourneyEvent(
                title="Two Production FastAPI Backends at TracTrac",
                event_date="2026-08",
                description="TracTrac's platform has grown to 100,000+ registered users across two production FastAPI backends, with Kafka/outbox event flows, Redis caching, and PgBouncer-pooled PostgreSQL/PostGIS.",
                sort_order=17,
            ),
        ]
    )

    db.add_all(
        [
            Scholarship(
                name="AWS Udacity Scholarship",
                issuer="AWS / Udacity",
                year="2022",
                description="AWS Machine Learning Foundations track — data analysis and ML fundamentals.",
                sort_order=1,
            ),
            Scholarship(
                name="ALX Software Engineering Scholarship",
                issuer="ALX Africa",
                year="2022",
                description="Full scholarship for a one-year software engineering program covering Python, Node.js, and backend specialization.",
                sort_order=2,
            ),
            Scholarship(
                name="Bertelsmann Gen-Y Scholarship",
                issuer="Bertelsmann",
                year="2022",
                description="Career growth and technical upskilling program.",
                sort_order=3,
            ),
        ]
    )

    db.add_all(
        [
            Experience(
                company="TracTrac",
                role="Lead Backend/DevOps Engineer",
                location="Maitama, FCT, Nigeria · On-site",
                start_date="2025-02",
                end_date=None,
                is_current=True,
                summary=(
                    "Architect and operate two production FastAPI backends for a nationwide agricultural "
                    "mechanization and logistics platform serving 100,000+ registered users. Designed Kafka "
                    "and outbox-pattern event flows for reliable cross-service messaging, Redis caching "
                    "(including JWT hot-path caching), and PgBouncer transaction-mode pooling in front of "
                    "PostgreSQL/PostGIS. Built offline-first field workflows with synchronization and "
                    "reconciliation for low-connectivity rural operations, GPS-based farm measurement, and a "
                    "CommCare integration. Diagnosed a production dashboard generating 60+ backend requests "
                    "per load and redesigned its data-loading architecture. Modeled scalability from 10 to "
                    "500+ concurrent users, and operate 20+ operational dashboards, Paystack payment "
                    "reconciliation, and real-time notifications across the platform. Deployed and maintain "
                    "services with Docker across VPS, Render, and Coolify, including migration-gated "
                    "deployments and health-check-driven rollouts."
                ),
                sort_order=1,
            ),
            Experience(
                company="SolarAfRiC (Feexet Limited)",
                role="Backend/DevOps Engineer",
                location="Remote · Contract",
                start_date="2026-05",
                end_date=None,
                is_current=True,
                summary=(
                    "Backend/DevOps contract engineering the systems behind SolarAfRiC's operations "
                    "platform: a context-aware AI diagnostics feature combining vision input, structured "
                    "LLM outputs, and equipment, location, technician, and LMS context; an escrow-style "
                    "payment lifecycle with payout wallets, bank resolution, and a dispute workflow; a "
                    "3-tier file storage fallback; and real-time WebSocket chat with FCM push notifications "
                    "alongside an LMS with certificate generation."
                ),
                sort_order=2,
            ),
            Experience(
                company="VITAL 2 (Ikore International Development)",
                role="Backend/DevOps Engineer",
                location="Remote · Part-Time",
                start_date="2026",
                end_date=None,
                is_current=True,
                summary=(
                    "Part-time backend/DevOps engineering for a farmer support program that has onboarded "
                    "5,000+ farmers. Built offline-sync field operations for low-connectivity environments, "
                    "voucher-based campaign workflows with QR code generation, bulk data import with "
                    "rollback, and audit trails for field data integrity."
                ),
                sort_order=3,
            ),
            Experience(
                company="SUBSEL",
                role="Fullstack Engineer",
                location="Remote",
                start_date="2026-07",
                end_date=None,
                is_current=True,
                summary=(
                    "Building wallet, VTU, and marketplace infrastructure for a digital services platform "
                    "spanning payments, subscriptions, and rewards. Working across backend services (wallet "
                    "ledger, multiple payment provider integrations, subscription and activation lifecycle, "
                    "referral and commission logic, asynchronous processing) and the customer-facing "
                    "frontend."
                ),
                sort_order=4,
            ),
            Experience(
                company="Join Momentum",
                role="Back End Developer",
                location="Dover, Delaware, United States · Remote",
                start_date="2025-01",
                end_date="2026-01",
                is_current=False,
                summary=(
                    "Promoted from intern to full-time Back End Developer in January 2025. "
                    "Optimized system performance by designing scalable APIs for the Job Simulator AI platform, reducing response time by 25%. "
                    "Built and normalized secure databases for multi-level user management. "
                    "Collaborated with product owners and frontend teams in an Agile environment. "
                    "Automated critical workflows, reducing errors by 30%. "
                    "Mentored junior developers; two became key contributors to the team."
                ),
                sort_order=5,
            ),
            Experience(
                company="Join Momentum",
                role="Back End Developer Intern",
                location="Dover, Delaware, United States · Remote",
                start_date="2024-07",
                end_date="2025-01",
                is_current=False,
                summary=(
                    "Designed and implemented scalable APIs for the Job Simulator AI platform. "
                    "Built and normalized secure databases improving data integrity. "
                    "Collaborated in an Agile environment to deliver high-impact features on schedule. "
                    "Automated critical workflows and contributed to team growth by mentoring junior developers."
                ),
                sort_order=6,
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
                    "and logistics platform serving 100,000+ registered users."
                ),
                tech_stack="FastAPI, PostgreSQL, PostGIS, Kafka, Redis, PgBouncer, Docker, Paystack",
                challenge=(
                    "Field agents and farmers often operate with little or no connectivity, and the "
                    "platform needed to reliably synchronize GPS farm measurements, bookings, and payments "
                    "across two backend services without losing data or double-processing events."
                ),
                engineered=(
                    "Designed Kafka and outbox-pattern event flows for reliable cross-service messaging, "
                    "Redis caching (including JWT hot-path caching), and PgBouncer transaction-mode pooling "
                    "in front of PostgreSQL/PostGIS. Built offline-first field workflows with "
                    "synchronization and reconciliation, GPS-based farm measurement, a CommCare "
                    "integration, and 20+ operational dashboards. Diagnosed a dashboard generating 60+ "
                    "backend requests per load and redesigned its loading architecture, and modeled "
                    "scalability from 10 to 500+ concurrent users."
                ),
                impact=(
                    "Two production FastAPI backends now serve 100,000+ registered users, with "
                    "offline-first workflows sustaining field operations in low-connectivity rural areas."
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
                    "Delivered as a backend/DevOps contract engagement, in active production use for solar "
                    "equipment diagnostics, bookings, and payments."
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
                    "offline, and campaign/voucher data imported in bulk needed to be safe to roll back when "
                    "it went wrong."
                ),
                engineered=(
                    "Designed offline-sync field operations workflows for low-connectivity environments, "
                    "voucher-based campaign workflows with QR code generation, bulk data import with "
                    "rollback, and audit trails for field data integrity."
                ),
                impact="The platform has onboarded 5,000+ farmers through field operations.",
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
                    "Building wallet architecture, VTU integration, multiple payment provider integrations, "
                    "subscription/activation lifecycle, referral/commission logic, asynchronous processing, "
                    "and marketplace architecture across backend and frontend."
                ),
                impact="In active full-time development since July 2026.",
                featured=True,
                sort_order=4,
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
                sort_order=5,
            ),
            Project(
                title="Estimate SBHP",
                slug="estimate-sbhp",
                category="engineering",
                summary="Engineering tool for estimating static bottom hole pressure using the Sukkar and Cornell method. Final-year Chemical Engineering project.",
                tech_stack="Python",
                repo_url="https://github.com/betiniakarandut/Estimate-SBHP",
                featured=False,
                sort_order=6,
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
                sort_order=7,
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
                sort_order=8,
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
                sort_order=9,
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
                sort_order=10,
            ),
        ]
    )

    db.add_all(
        [
            # Backend
            Skill(name="Python", category="Backend", proficiency=5),
            Skill(name="FastAPI", category="Backend", proficiency=5),
            Skill(name="Django", category="Backend", proficiency=4),
            Skill(name="Node.js", category="Backend", proficiency=4),
            Skill(name="REST API Design", category="Backend", proficiency=5),
            Skill(name="WebSockets", category="Backend", proficiency=4),
            # Data
            Skill(name="PostgreSQL", category="Data", proficiency=5),
            Skill(name="PostGIS", category="Data", proficiency=4),
            Skill(name="Redis", category="Data", proficiency=4),
            # Distributed Systems
            Skill(name="Kafka", category="Distributed Systems", proficiency=4),
            Skill(name="Outbox Pattern", category="Distributed Systems", proficiency=4),
            Skill(name="Celery", category="Distributed Systems", proficiency=5),
            # Cloud & Infrastructure
            Skill(name="Docker", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="Linux / VPS", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="Render", category="Cloud & Infrastructure", proficiency=4),
            Skill(name="Coolify", category="Cloud & Infrastructure", proficiency=4),
            # DevOps
            Skill(name="Alembic", category="DevOps", proficiency=4),
            Skill(name="PgBouncer", category="DevOps", proficiency=4),
            Skill(name="CI/CD", category="DevOps", proficiency=4),
            Skill(name="Health Checks", category="DevOps", proficiency=4),
            # Integrations
            Skill(name="Paystack", category="Integrations", proficiency=4),
            Skill(name="Firebase / FCM", category="Integrations", proficiency=4),
            Skill(name="OpenAI (Vision & Structured Outputs)", category="Integrations", proficiency=4),
            Skill(name="CommCare", category="Integrations", proficiency=3),
            # Frontend
            Skill(name="React", category="Frontend", proficiency=4),
            Skill(name="TypeScript", category="Frontend", proficiency=3),
            Skill(name="JavaScript", category="Frontend", proficiency=4),
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
