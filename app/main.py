from fastapi import FastAPI

app = FastAPI(title="DevOps Atividade API", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "API FastAPI rodando com CI/CD!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
