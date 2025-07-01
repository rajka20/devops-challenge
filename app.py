from flask import Flask, request
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNTER = Counter("api_requests_total", "Total API Requests")

@app.route("/api", methods=["GET", "POST"])
def api():
    REQUEST_COUNTER.inc()
    headers = dict(request.headers)
    method = request.method
    body = request.get_json(silent=True)
    return f"""
Welcome to our demo API, here are the details of your request:

***Headers***:
{headers}

***Method***:
{method}

***Body***:
{body}
"""

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

