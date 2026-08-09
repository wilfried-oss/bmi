from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class BMICalculatorRequest(BaseModel):
    height: float
    weight: float


@app.get("/healthz")
def health_check():
    return {"status": "ok"}
