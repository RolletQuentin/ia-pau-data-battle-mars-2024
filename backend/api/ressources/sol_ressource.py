from fastapi import APIRouter, Body, HTTPException
from api.models.RequestBestSol import RequestBestSol

from api.services import sol_service 
from ai.models.model_find_solution import model_PAT
from api.models.Solution import Solution

router = APIRouter (
    prefix="/sol"
)

@router.post("/best_solutions")
async def best_solutions(data: RequestBestSol = Body(...)) -> list[Solution]:
        secteur_activite = data.secteur_activite
        if not sol_service.check_sector(secteur_activite):
            raise HTTPException(status_code=400, detail="Secteur d'activité incorrect")
        description = sol_service.clean_description(data.description)
        if not sol_service.check_description(description):
            raise HTTPException(status_code=422, detail="Description vide ou taille > 2048 caractere")
        solutions =  model_PAT(data.description,secteur_activite)        
        data = sol_service.get_multiple_solution(solutions,secteur_activite)
        return data