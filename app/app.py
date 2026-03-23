from flask import Flask, Response
import os
import socket
import time
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

# --- Prometheus imports ---
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# --- Prometheus metrics ---
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests",
    ["method", "endpoint", "http_status"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency",
    ["endpoint"]
)

# --- READ CONFIG FROM ENVIRONMENT VARIABLES ---
tenant_id = os.getenv("AZURE_TENANT_ID")
client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")

credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

vault_url = "https://pkKeyVault12345.vault.azure.net/"
client = SecretClient(vault_url=vault_url, credential=credential)

# --- Request monitoring middleware ---
@app.before_request
def start_timer():
    from flask import g
    g.start_time = time.time()

@app.after_request
def record_metrics(response):
    from flask import request, g
    resp_time = time.time() - g.start_time

    REQUEST_LATENCY.labels(request.path).observe(resp_time)
    REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()

    return response

@app.route("/")
def home():
    try:
        secret = client.get_secret("db-password").value
        return f"Secret from Azure Key Vault: {secret}"
    except Exception as e:
        return f"Error accessing secret: {str(e)}"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/version")
def version():
    return {"version": "v3.0"}

# --- Prometheus metrics endpoint ---
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)