# Prometheus URL Checker

A simple Python service that checks the health and response time of external URLs and exposes metrics in Prometheus format.

---

## 🧠 Features
- Checks two external URLs every 10 seconds.
- Reports:
  - `sample_external_url_up`: 1 (up) or 0 (down)
  - `sample_external_url_response_ms`: response time in milliseconds
- Exposes metrics at `/metrics`.

---

## 🐍 Run Locally

```bash
pip install -r requirements.txt
python app.py

