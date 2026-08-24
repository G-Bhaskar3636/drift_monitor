FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml .
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY drift_monitor/ drift_monitor/
COPY tests/ tests/
COPY examples/ examples/
COPY README.md .

CMD ["python", "-m", "pytest"]