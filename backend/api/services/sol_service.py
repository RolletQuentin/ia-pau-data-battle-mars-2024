from api.repositories import sol_repository 
from api.repositories import sec_repository
  
from ai.models.model2 import model_Quentin

from api.models.Solution import Solution

import re


def get_multiple_solution(solutions,secteur_activite):
    data = []

    results = sol_repository.get_multiple_solution(solutions)

    for result in results:
        
        gains = model_Quentin(result[0],secteur_activite)
        solution = Solution(
            num=result[0],
            titre=result[1],
            degre_confiance=gains[0],
            gain_monetaire=str(gains[1]),
            gain_watt=str(gains[2]),
            gain_co2=str(gains[3])
        )

        data.append(solution)
    
    return data


def check_sector(sector):
    sectors = sec_repository.get_list_sector()
    if sector in sectors:
        return True
    else:
        return False


def clean_description(description):
    description = re.sub('<.*?>', '',description)
    description = re.sub(r"\\'", "'", description)  # Remplace \' par '
    description = re.sub(r"\\n", " ", description)  # Remplace \n par un espace
    description = re.sub(r"\\r", " ", description)  # Remplace \r par un espace
    description = re.sub(r'\\"', '"', description)  # Remplace \" par "
    description = re.sub(r"^'", '', description)  # Supprime l'apostrophe au début de la chaîne
    description = re.sub(r"'$", '', description)  # Supprime l'apostrophe à la fin de la chaîne
    description = re.sub(r'\s+', ' ', description).strip()  # Nettoie les espaces multiples et enlève les espaces de début et de fin
    return description

def check_description(description):
    if len(description) == 0 or len(description) > 2048:
        return False
    return True
