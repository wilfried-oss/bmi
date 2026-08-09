from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BMICalculatorRequest(BaseModel):
    height: float
    weight: float


@app.get("/")
def welcome_route():
    return {"message": "Welcome de BMI Calculator API"}


@app.get("/healthz")
def health_check():
    return {"status": "ok"}


def _calculate_bmi(weight: float, height: float) -> float:
    if height <= 0 or weight <= 0:
        raise HTTPException(
            status_code=400, detail="Height and weight must be positive values."
        )
    return weight / (height**2)


def _input_validation(weight: float, height: float):
    if height <= 0 or weight <= 0:
        raise HTTPException(
            status_code=400, detail="Height and weight must be positive values."
        )


@app.post("/calculate_bmi")
def calculate_bmi(request: BMICalculatorRequest):
    _input_validation(request.weight, request.height)
    bmi = _calculate_bmi(request.weight, request.height)
    return {"bmi": bmi}
