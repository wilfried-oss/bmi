# BMI

A small FastAPI service that calculates Body Mass Index.

Send your weight and height, get back your BMI plus a short piece of advice based on which range you fall into.

## Stack

- Python 3.14
- FastAPI
- Uvicorn
- Pytest for testing
- uv for dependency management and builds

## Installation

This project uses [uv](https://docs.astral.sh/uv/). Once it's installed:

```bash
git clone https://github.com/wilfried-oss/bmi.git
cd bmi
uv sync
```

## Running the server

```bash
uv run uvicorn api:app --reload
```

The app is available at `http://localhost:8000`. The homepage serves the static file `static/index.html` directly.

## Endpoints

| Method | Route            | Description                           |
| ------ | ---------------- | ------------------------------------- |
| GET    | `/`              | Homepage                              |
| GET    | `/healthz`       | Health check                          |
| POST   | `/calculate_bmi` | Calculates BMI from weight and height |

### Example request

```bash
curl -X POST http://localhost:8000/calculate_bmi \
  -H "Content-Type: application/json" \
  -d '{"weight": 70, "height": 1.75}'
```

Response:

```json
{
  "bmi": 22.86,
  "advice": "Normal weight, keep up the good work!"
}
```

`weight` is in kilograms, `height` in meters. A zero or negative value for either one returns a 400 error.

## Tests

```bash
uv run pytest
```

## Roadmap

- Stronger input validation (units, edge cases) : WORK IN PROGRESS
- Per-user calculation history
