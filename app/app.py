from flask import Flask
import socket
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

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
