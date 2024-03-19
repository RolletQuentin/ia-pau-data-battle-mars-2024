from fastapi import APIRouter, Body
from api.models.RequestBestSol import RequestBestSol

from api.services import sol_service
from ai.models.model_find_solution import model_PAT


router = APIRouter (
    prefix="/sol"
)

@router.post("/best_solutions")
async def best_solutions(data: RequestBestSol = Body(...)):
        secteur_activite = data.secteur_activite
        description = data.description
        solutions =  model_PAT(description,secteur_activite)        
        data = sol_service.get_multiple_solution(solutions,secteur_activite)
        return data