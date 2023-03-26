from fastapi import FastAPI

from mortgage_calculator.views import router as calculator_router

app = FastAPI()
app.include_router(calculator_router)


@app.get("/")
def healthcheck():
    return {"status": "ok"}
