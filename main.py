from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Guide Obsèques - en construction"}