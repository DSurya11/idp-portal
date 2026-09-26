FROM python:3.12-slim

# Non-root, like every idp workload (Kyverno disallow-root-containers).
RUN useradd --uid 10001 --create-home app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /usr/local/lib/python3.12/site-packages/pip* /usr/local/bin/pip*
COPY app ./app
ARG GIT_SHA=unknown
ENV GIT_SHA=${GIT_SHA}
USER 10001

EXPOSE 8000
# --timeout-keep-alive 75 > ALB idle timeout (60s): uvicorn must never close a
# connection the ALB still considers open (source of sporadic 502s).
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive", "75"]
