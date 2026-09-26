# ${{ values.name }}

${{ values.description }}

Created from the **idp python-service golden path** (Backstage template).

| What | Where |
|---|---|
| Code | `app/main.py` (FastAPI) |
| Image | ECR `svc/${{ values.name }}`, tagged with the commit SHA (built by `.github/workflows/ci.yml`) |
| Deployment | `idp-gitops` → `apps/${{ values.name }}` (Argo CD, automated sync) |
| URL | `http://<ALB>/${{ values.name }}/` |

Every push to `main`: build (native arm64) → push to ECR → Trivy gate.
