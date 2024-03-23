from api.repositories import sol_repository 
from api.repositories import sec_repository
  
from api.services import gain_rex_service

from api.models.Solution import Solution

import re


def get_multiple_solution(solutions, secteur_activite):
    data = []
    results = sol_repository.get_multiple_solution(solutions)
    id_sector = sec_repository.get_id_sector(str(secteur_activite))
    
    print(id_sector)
    result_mapping = {}  # Create a mapping from solution number to the solution object
    for result in results:
        gains = gain_rex_service.predict_gain_solution(result[0], id_sector)
        print(gains)
        
        solution = Solution(
            num=result[0],
            titre=result[1],
            degre_confiance=gains.number_of_based_solutions,
            gain_monetaire=gains.average_financial_gain,
            gain_watt=gains.average_energy_gain,
            gain_co2=gains.average_ges_gain
        )
        result_mapping[result[0]] = solution  # Map the solution number to the solution object
    
    # Create the ordered data list based on the order of solution numbers in 'solutions'
    for num in solutions:
        if num in result_mapping:  # Check if the solution number is in the mapping
            data.append(result_mapping[num])
    
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
