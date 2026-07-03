from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return JSONResponse(
        content={"message": "Guide Obsèques - en construction"},
        media_type="application/json; charset=utf-8"
    )