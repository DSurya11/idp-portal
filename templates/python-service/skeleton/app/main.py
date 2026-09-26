"""${{ values.name }} - ${{ values.description }}

Created from the idp "python-service" golden path.

Routing: the shared ALB forwards /${{ values.name }}/... unchanged (no path stripping), so
every route is served both under the prefix (traffic via the ALB) and at the root
(kubelet probes hit the pod directly).
"""
import os

from fastapi import APIRouter, FastAPI

SERVICE_NAME = "${{ values.name }}"
router = APIRouter()


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}


@router.get("/")
def index() -> dict:
    return {
        "service": SERVICE_NAME,
        "message": "Hello from the idp golden path",
        "version": os.environ.get("GIT_SHA", "unknown"),
    }


app = FastAPI(title=SERVICE_NAME)
app.include_router(router)
app.include_router(router, prefix=f"/{SERVICE_NAME}")
