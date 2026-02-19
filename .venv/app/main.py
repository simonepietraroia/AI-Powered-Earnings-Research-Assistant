from fastapi import FastAPI

app = FastAPI(title="Earnings Research Assistant")

@app.get("/")
def root():
    return {"message": "API running"}
