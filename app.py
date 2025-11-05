from prometheus_client import start_http_server, Gauge
import requests
import time

# URLs to check
URLS = [
    "https://httpstat.us/503",
    "https://httpstat.us/200"
]

# Define Prometheus metrics
url_up = Gauge('sample_external_url_up', 'Whether the URL is up (1) or down (0)', ['url'])
url_response_time = Gauge('sample_external_url_response_ms', 'Response time for the URL in ms', ['url'])

def check_url(url):
    """Check a single URL and update metrics."""
    start_time = time.time()
    try:
        response = requests.get(url, timeout=5)
        elapsed_ms = (time.time() - start_time) * 1000
        url_response_time.labels(url=url).set(elapsed_ms)
        
        if response.status_code == 200:
            url_up.labels(url=url).set(1)
        else:
            url_up.labels(url=url).set(0)
    except Exception:
        # In case of connection errors, mark it as down
        url_up.labels(url=url).set(0)
        url_response_time.labels(url=url).set(0)

def main():
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    print("✅ Metrics server running on http://localhost:8000/metrics")

    # Periodically check URLs
    while True:
        for url in URLS:
            check_url(url)
        time.sleep(10)  # check every 10 seconds

if __name__ == "__main__":
    main()
