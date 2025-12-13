from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict
from app.custom_metrics import prediction_value_metric

# Prometheus
from prometheus_fastapi_instrumentator import Instrumentator

# OpenTelemetry
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
import os

app = FastAPI(title="EE596 A3 ML API")

# ---- OTel setup ----
service_name = os.getenv("OTEL_SERVICE_NAME", "ee596-a3-ml-api")
endpoint = os.getenv("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "http://jaeger:4318/v1/traces")

provider = TracerProvider(resource=Resource.create({"service.name": service_name}))
provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint)))
trace.set_tracer_provider(provider)

FastAPIInstrumentor.instrument_app(app)
# --------------------

class PredictRequest(BaseModel):
    features: Dict[str, float]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: PredictRequest, request: Request):
    yhat = float(sum(payload.features.values()))
    request.state.prediction = yhat
    trace.get_current_span().set_attribute("ml.prediction", yhat)
    return {"prediction": yhat}


# Prometheus /metrics + custom metric
instrumentator = Instrumentator()
instrumentator.add(prediction_value_metric())
instrumentator.instrument(app).expose(app)