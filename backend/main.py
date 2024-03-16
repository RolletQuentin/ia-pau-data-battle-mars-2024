from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.ressources import solution
from api.ressources import rex_ressource

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(solution.router)
app.include_router(rex_ressource.router)


@app.get("/")
async def root():
    return {"message": "Hello world from FastAPI!"}
