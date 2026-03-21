from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"Hybrid SRE Project Running on {hostname}"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/version")
def version():
    return {"version": "v1.0"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)