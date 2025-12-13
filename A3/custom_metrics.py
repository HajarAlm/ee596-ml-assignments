from typing import Callable

from prometheus_client import Histogram
from prometheus_fastapi_instrumentator.metrics import Info

PREDICTION_HIST = Histogram(
    "ml_prediction_value",
    "Prediction value returned by the model",
    buckets=(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60),
)

def prediction_value_metric() -> Callable[[Info], None]:
    def instrumentation(info: Info) -> None:
        pred = getattr(info.request.state, "prediction", None)
        if pred is None:
            return
        try:
            PREDICTION_HIST.observe(float(pred))
        except Exception:
            return

    return instrumentation
