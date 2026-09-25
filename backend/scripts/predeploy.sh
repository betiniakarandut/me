#!/bin/sh
# Runs before each backend deploy (Railway preDeployCommand). Any failure exits
# non-zero, which stops the deploy and keeps the previous version serving.
set -eu

alembic upgrade head
python -m app.db.content_sync
