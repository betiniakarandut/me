# Deployment & migration runbook

Target: Railway (frontend + backend + PostgreSQL) on `betiniakarandut.com`, replacing Render + SQLite.

Nothing in this document has been executed against Railway, Render or DNS yet. Each step is written to be run and verified by hand.

## 1. Railway services

Create one Railway project from the GitHub repo with three services.

| Service | Root Directory | Config file path (service settings) | Build | Runs |
| --- | --- | --- | --- | --- |
| `backend` | `/backend` | `/backend/railway.json` | `backend/Dockerfile` (Python 3.12) | pre-deploy `sh scripts/predeploy.sh`, then `uvicorn … --port $PORT --proxy-headers` |
| `frontend` | `/frontend` | `/frontend/railway.json` | `frontend/Dockerfile` (Node 22 build → Caddy) | Caddy serving `dist/` on `$PORT` |
| `Postgres` | — | — | Railway PostgreSQL template | — |

Railway's config file does **not** follow the Root Directory, so set the config file path explicitly as shown. Watch patterns (`/backend/**`, `/frontend/**`) keep a change in one service from redeploying the other.

### Backend variables

| Name | Value |
| --- | --- |
| `DATABASE_URL` | `${{Postgres.DATABASE_URL}}` (reference variable; private network) |
| `CORS_ORIGINS` | `https://betiniakarandut.com,https://www.betiniakarandut.com` |
| `DEBUG` | `false` |
| `GITHUB_TOKEN` | classic PAT with no scopes (optional; raises the GitHub rate limit) |
| `RESEND_API_KEY` | Resend API key (new/rotated, see §6) |
| `CONTACT_NOTIFICATION_EMAIL` | inbox that receives contact-form messages |
| `CONTACT_FROM_EMAIL` | `onboarding@resend.dev` until the domain is verified in Resend, then e.g. `contact@betiniakarandut.com` |

### Frontend variables

| Name | Value |
| --- | --- |
| `VITE_API_BASE_URL` | `https://api.betiniakarandut.com/api/v1` |

`VITE_API_BASE_URL` is a **build-time** value: the Dockerfile declares it as a build `ARG`, and changing it requires a redeploy. Before the custom domains are live, set it to the backend's Railway domain (`https://<backend>.up.railway.app/api/v1`), and add the frontend's Railway domain (`https://<frontend>.up.railway.app`) to `CORS_ORIGINS`.

## 2. Deploy order

1. **Postgres:** create the database service.
2. **Backend:** deploy. The pre-deploy step runs `alembic upgrade head` and then `python -m app.db.content_sync`. If either fails, the deploy stops and nothing starts serving. The health check is `GET /api/v1/health/ready`, which returns 503 when the database is unreachable.
3. **Frontend:** deploy with `VITE_API_BASE_URL` pointing at the backend.
4. Verify on the Railway domains (§7) before touching DNS.

## 3. Database: SQLite → PostgreSQL

Content does **not** need a data copy. It is regenerated deterministically from `backend/app/db/seed.py` by the pre-deploy content sync. Verified locally on PostgreSQL 17: a fresh `alembic upgrade head` reaches `20260925_0004`, `alembic check` reports no drift, and a second sync changes nothing.

The only data that can't be regenerated is **`contact_messages` on the Render production database**. The local `backend/betini_site.db` is a development copy: **do not** copy its contact messages into production.

To carry over production messages:

1. From the Render dashboard, confirm what production uses: `DATABASE_URL`, and whether a persistent disk is attached. With SQLite on an ephemeral disk, earlier messages may already be gone.
2. Download the Render SQLite file, or get its Postgres URL.
3. From `backend/`, with `DATABASE_URL` set to the Railway Postgres **public** URL:

   ```bash
   python -m app.db.transfer_contacts --source "sqlite:///path/to/render_betini_site.db" --dry-run
   python -m app.db.transfer_contacts --source "sqlite:///path/to/render_betini_site.db"
   ```

   The transfer is idempotent (matched on email + timestamp + message). New rows take ids from the Postgres sequence, so no `setval` is needed.

Content updates from now on: edit `seed.py` and deploy. Rows removed from `seed.py` are reported, not deleted. To delete them, run `python -m app.db.content_sync --prune` once in a Railway shell.

## 4. Custom domain (Namecheap → Railway)

| Hostname | Railway service | Notes |
| --- | --- | --- |
| `betiniakarandut.com` | frontend | canonical |
| `www.betiniakarandut.com` | frontend | Caddy 301-redirects to the apex |
| `api.betiniakarandut.com` | backend | API origin used by the frontend |

Add each hostname under the service's **Settings → Networking → Custom Domain**. Railway shows the exact DNS records to create (a CNAME target, plus a TXT verification record). Copy those values into Namecheap **Advanced DNS**.

Check before choosing DNS: the apex (`@`) needs a CNAME-style record. Confirm that your Namecheap DNS plan supports an ALIAS/CNAME-flattened record at `@`. If it does not, move DNS hosting to a provider that does, such as Cloudflare in DNS-only mode.

Domain references already point at the new domain: `frontend/index.html` (canonical, Open Graph, Twitter, JSON-LD), `frontend/public/robots.txt`, `frontend/public/sitemap.xml`, the frontend's production API default, and `frontend/Caddyfile` (www redirect).

## 5. CORS

Production must list only the real site origins in `CORS_ORIGINS`. Credentials are off, and only `GET`, `POST` and `OPTIONS` with `Content-Type` are allowed. When `CORS_ORIGINS` is unset, it defaults to the local Vite dev/preview servers.

## 6. Security checklist

- `backend/.env` is gitignored and was never committed (history checked). It contains a live Resend API key used locally: **rotate it** and set the new key only as a Railway variable.
- Keep `DEBUG=false`.
- `POST /api/v1/articles/sync-hashnode` has been removed: it was unauthenticated, unused by the frontend, and blocked by Cloudflare. Articles are curated in `seed.py`.
- `POST /api/v1/contact`: validation, a honeypot field, a 16 KB body limit and an in-memory rate limit (5 per client and 50 site-wide per hour by default). The limiter is process-local, so keep **one** uvicorn worker (see the Dockerfile).
- `/docs` stays public: the API is read-only apart from the contact form, and the docs are part of the portfolio. Remove it with `FastAPI(docs_url=None, redoc_url=None, openapi_url=None)` if that changes.

## 7. Verification checklist

Backend (Railway domain first, then `api.betiniakarandut.com`):

- [ ] Deploy logs show `alembic upgrade head` reaching `20260925_0004` and the content sync committing.
- [ ] `GET /api/v1/health` → `{"status":"ok"}`; `GET /api/v1/health/ready` → `{"status":"ok","database":"ok"}`.
- [ ] `GET /api/v1/profile`, `/profile/journey`, `/experience`, `/projects?featured=true` (4), `/projects` (11), `/scholarships`, `/skills`, `/articles`, `/github/repositories` all return 200.
- [ ] A request with `Origin: https://example.com` gets no `access-control-allow-origin` header.
- [ ] A redeploy leaves row counts unchanged (the content sync is idempotent).

Frontend:

- [ ] `https://betiniakarandut.com` renders the hero immediately and API sections fill in.
- [ ] `https://www.betiniakarandut.com/anything` → 301 to `https://betiniakarandut.com/anything`.
- [ ] `/resume.pdf`, `/robots.txt`, `/sitemap.xml`, `/og-image.png` return 200.
- [ ] Browser devtools: no CORS errors; API calls go to `api.betiniakarandut.com`.
- [ ] A contact-form submission returns 201 and the notification email arrives.
- [ ] Social preview checks out in a link-preview debugger (LinkedIn Post Inspector, X card validator).

## 8. Rollback

- **Application:** redeploy the previous successful deployment from the Railway dashboard. Migrations are additive (`20260925_0004` only adds nullable/defaulted columns), so older code keeps working against the newer schema.
- **Schema:** `alembic downgrade 20260803_0003` removes the three added columns. Run it only if you also redeploy the old code.
- **Cutover:** keep the Render services running until the Railway deployment passes §7 on both the Railway domains and the custom domain. Until DNS for `betiniakarandut.com` is switched, the Render site is unaffected. Do not delete the Render database until the contact-message transfer is confirmed.
