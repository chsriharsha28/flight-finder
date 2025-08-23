from fastapi import FastAPI

app = FastAPI(title="Flight Finder")

@app.get("/")
def read_root():
    return {"message": "Welcome to Flight Finder API"}
