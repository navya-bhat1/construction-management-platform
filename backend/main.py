from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Construction Management Platform Running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/task")
def get_task():
    return {
        "task": [
            {"id": 1, "task": "Foundation Work"},
            {"id": 2, "task": "Site Inspection"}
        ]
    }