from fastapi import APIRouter, Body, HTTPException
from api.models.RequestBestSol import RequestBestSol

from api.services import sol_service
from api.services import gain_rex_service
from api.services import cout_rex_service

from ai.models.model_find_solution import model_find_solution

from api.models.Solution import Solution
from api.models.DataSolution import DataSolution
from api.models.GainRex import GainRex
from api.models.CoutRex import CoutRex
from api.models.AverageGain import AverageGain
from api.models.AverageCout import AverageCout

router = APIRouter(
    prefix="/sol"
)


@router.post("/best_solutions")
async def best_solutions(data: RequestBestSol = Body(...)) -> list[Solution]:
    secteur_activite = data.secteur_activite
    if not sol_service.check_sector(secteur_activite):
        raise HTTPException(
            status_code=400, detail="Secteur d'activité incorrect")
    description = sol_service.clean_description(data.description)
    if not sol_service.check_description(description):
        raise HTTPException(
            status_code=422, detail="Description vide ou taille > 2048 caractere")
    solutions = model_find_solution(description, secteur_activite)
    data = sol_service.get_multiple_solution(solutions, secteur_activite)
    print(data)
    return data


@router.get("/data_solution/{code_solution}/{code_sector}")
async def get_data_solution(code_solution: int, code_sector: int) -> DataSolution:
    data = sol_service.get_data_solution(code_solution,code_sector)
    print(data)
    return data


@router.get("/gains/{code_solution}")
async def get_gains(code_solution: int) -> list[GainRex]:
    data = gain_rex_service.get_all_for_one_solution(
        code_solution)
    return data


@router.get("/couts/{code_solution}")
async def get_couts(code_solution: int) -> list[CoutRex]:
    data = cout_rex_service.get_all_for_one_solution(
        code_solution)
    return data


@router.get("/average_gain/{code_solution}/{code_secteur}")
async def get_average_gain(code_solution: int, code_secteur: int) -> AverageGain:
    data = gain_rex_service.predict_gain_solution(code_solution, code_secteur)
    return data


@router.get("/average_cout/{code_solution}/{code_secteur}")
async def get_average_cout(code_solution: int, code_secteur: int) -> AverageCout:
    data = cout_rex_service.predict_cout_solution(code_solution, code_secteur)
    return data


