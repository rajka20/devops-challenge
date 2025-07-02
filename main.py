from fastapi import FastAPI, Request
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Prometheus counter
request_counter = Counter("request_count", "Total number of API requests")

@app.post("/api")
async def handle_request(request: Request):
    request_counter.inc()
    headers = dict(request.headers)
    method = request.method
    body = await request.json()
    return {
        "message": "Welcome to our demo API, here are the details of your request:",
        "headers": headers,
        "method": method,
        "body": body
    }

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest()

