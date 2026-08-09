from fastapi import FastAPI
from fastapi.responses import HTTPException
from pydantic import BaseModel

app = FastAPI()


class BMICalculatorRequest(BaseModel):
    height: float
    weight: float


@app.get("/healthz")
def health_check():
    return {"status": "ok"}


def _calculate_bmi(height: float, weight: float) -> float:
    if height <= 0 or weight <= 0:
        raise HTTPException(status_code=400, detail="Height and weight must be positive values.")
    return weight / (height ** 2)

