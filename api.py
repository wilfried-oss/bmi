from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


class BMICalculatorRequest(BaseModel):
    height: float
    weight: float


@app.get("/")
def welcome_route():
    return FileResponse("static/index.html")


@app.get("/healthz")
def health_check():
    return {"status": "ok"}


def _input_validation(weight: float, height: float):
    if height <= 0 or weight <= 0:
        raise HTTPException(
            status_code=400, detail="Height and weight must be positive values."
        )


def _calculate_bmi(weight: float, height: float) -> float:
    if height <= 0 or weight <= 0:
        raise HTTPException(
            status_code=400, detail="Height and weight must be positive values."
        )
    return weight / (height**2)


def _advice(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight, you should consider gaining some weight."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight, keep up the good work!"
    elif 25 <= bmi < 29.9:
        return "Overweight, you should consider losing some weight."
    else:
        return "Obesity, you should consult with a healthcare provider for advice."


@app.post("/calculate_bmi")
def calculate_bmi(request: BMICalculatorRequest):
    _input_validation(request.weight, request.height)
    bmi = _calculate_bmi(request.weight, request.height)
    advice = _advice(bmi)
    return {"bmi": round(bmi, 2), "advice": advice}


# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")
