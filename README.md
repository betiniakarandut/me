# Betini Personal Website

Monorepo for a personal career website with:

- `backend/`: FastAPI API for profile content and contact submissions
- `frontend/`: Vite frontend with a premium textured visual theme

## Quick Start

### Backend

1. Create virtual environment:
   - `python -m venv .venv`
   - `.venv\Scripts\activate`
2. Install dependencies:
   - `pip install -r backend/requirements.txt`
3. Run:
   - `uvicorn app.main:app --reload --app-dir backend`

### Frontend

1. Install dependencies:
   - `cd frontend && npm install`
2. Run:
   - `npm run dev`

## Planned Architecture

- FastAPI REST backend for profile, experience, projects, and contact form
- Frontend renders sections from API data
- Future phases include database integration, CMS/admin, and deployment automation
