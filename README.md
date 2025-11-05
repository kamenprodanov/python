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


### Running Locally, build and push image, deploying to K8S cluster


### 1 Running Locally
```bash
pip install -r requirements.txt
python app.py
```

### 2 Build Docker image
```bash
docker build -t <my-dockerhub-username>/prometheus-url-checker:latest .
```
### 3 Push Docker image
```
docker push <my-dockerhub-username>/prometheus-url-checker:latest
```

### 4 Deploying to K8S cluster
aws eks update-kubeconfig --region eu-central-1 --name <your-cluster-name>
helm install url-checker ./helm/prometheus-url-checker \
  --namespace monitoring --create-namespace

### 5 Verifying

kubectl get pods -n monitoring
kubectl port-forward svc/url-checker 8000:8000 -n monitoring
curl localhost:8000/metrics

