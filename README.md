# betiniakarandut.com

Portfolio of Betini Akarandut, Backend & Cloud Engineer. A Vite frontend and a FastAPI + PostgreSQL backend, deployed as three Railway services.

```text
                betiniakarandut.com  (www → apex redirect)
                          │
                ┌─────────▼─────────┐
                │ frontend          │  Vite static build served by Caddy
                │ (Railway service) │
                └─────────┬─────────┘
                          │ fetch  https://api.betiniakarandut.com/api/v1
                ┌─────────▼─────────┐
                │ backend           │  FastAPI · SQLAlchemy · Alembic · uvicorn (1 worker)
                │ (Railway service) │  pre-deploy: alembic upgrade head + content sync
                └─────────┬─────────┘
                          │ private network (DATABASE_URL)
                ┌─────────▼─────────┐
                │ PostgreSQL        │  Railway managed database
                └───────────────────┘
```

## Layout

| Path | What it is |
| --- | --- |
| `frontend/` | Vanilla JS + Vite. `src/content/` holds the static narrative (hero, TracTrac case study, leadership); `src/components/` renders sections; `src/app/bootstrap.js` loads API-backed sections progressively. |
| `backend/app/` | FastAPI app: `api/v1/endpoints` → `services` → `repositories` → `models`, with Pydantic `schemas`. |
| `backend/app/db/seed.py` | Source of truth for database-driven content (profile, experience, projects, skills, articles, certifications, journey). |
| `backend/app/db/content_sync.py` | Idempotent upsert of `seed.py` into the database. |
| `backend/app/db/migrations/` | Alembic migration history. Never rewrite it; add new revisions. |
| `docs/DEPLOYMENT.md` | Railway, PostgreSQL migration, domain and verification runbook. |

## Local development

Backend (Python 3.12; matches the production Docker image):

```bash
cd backend
python -m venv venv && venv\Scripts\activate      # macOS/Linux: source venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env                              # SQLite by default
alembic upgrade head
python -m app.db.content_sync
uvicorn app.main:app --reload                     # http://127.0.0.1:8000/docs
```

Run commands from `backend/`: `.env`, the SQLite path and `alembic.ini` resolve relative to it.

Frontend:

```bash
cd frontend
npm ci
npm run dev                                       # http://localhost:5173, calls http://127.0.0.1:8000/api/v1
```

## Content changes

Edit `backend/app/db/seed.py`, then run `python -m app.db.content_sync` (production runs it on every deploy). Rows are matched on natural keys (project `slug`, article `url`, experience `company + start_date`, skill `name`, and so on), so re-running never duplicates content. Content that has been removed from `seed.py` is reported but kept. Use `--prune` to delete it, and `--dry-run` to preview.

Narrative content that is not a record (case studies, architecture diagrams, leadership) lives in `frontend/src/content/`.

## Environment variables

Backend (`backend/.env.example`): `DATABASE_URL`, `CORS_ORIGINS`, `DEBUG`, `GITHUB_USERNAME`, `GITHUB_TOKEN`, `RESEND_API_KEY`, `CONTACT_NOTIFICATION_EMAIL`, `CONTACT_FROM_EMAIL`, optional `CONTACT_RATE_LIMIT_*`.

Frontend (`frontend/.env.example`): `VITE_API_BASE_URL`, inlined at build time. It defaults to `http://127.0.0.1:8000/api/v1` in dev and `https://api.betiniakarandut.com/api/v1` in production builds.

## Checks

```bash
cd backend && python -m compileall -q app && pytest -q && alembic check
cd frontend && npm ci && npm run build
```

`TEST_DATABASE_URL=postgresql://… pytest` runs the same suite against PostgreSQL.

## API

All routes are under `/api/v1`: `GET /health`, `GET /health/ready`, `GET /profile`, `GET /profile/journey`, `GET /experience`, `GET /projects?featured=`, `GET /scholarships` (certifications, scholarships and awards), `GET /skills`, `GET /articles`, `GET /github/repositories`, `POST /contact`. Interactive docs are at `/docs`.
