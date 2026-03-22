from flask import Flask
import os
import socket
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# --- READ CONFIG FROM ENVIRONMENT VARIABLES ---
tenant_id = os.getenv("AZURE_TENANT_ID")
client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")

credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret,
    additionally_allowed_tenants=["9f7b1444-2ef2-4a08-9f3e-4ba5b8019571"]
)

vault_url = "https://pkKeyVault12345.vault.azure.net/"
client = SecretClient(vault_url=vault_url, credential=credential)

@app.route("/")
def home():
    return {"status": "home"}

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/version")
def version():
    return {"version": "v1.0"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
