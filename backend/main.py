from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "¡Hola desde FastAPI en Render!"}
