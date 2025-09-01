from fastapi import FastAPI

app = FastAPI(
    title="Minha API Básica",
    description="Um projeto de exemplo com FastAPI e Uvicorn.",
    version="1.0.0",
)

@app.get("/auth/me")
def read_auth_me():
    """
    Este endpoint retorna uma mensagem de status simples.
    """
    return {"status": "Hello World"}

@app.get("/")
def read_root():
    return {"message": "API está no ar! Acesse /docs para ver a documentação."}