from api.repositories import sol_repository 
from api.repositories import sec_repository
  
from api.services import gain_rex_service
from api.services import cout_rex_service

from api.models.Solution import Solution
from api.models.DataSolution import DataSolution

import re


def get_multiple_solution(solutions, secteur_activite):
    data = []
    results = sol_repository.get_multiple_solution(solutions)
    id_sector = sec_repository.get_id_sector(str(secteur_activite))
    
    print(id_sector)
    result_mapping = {}  # Create a mapping from solution number to the solution object
    for result in results:
        gain = gain_rex_service.predict_gain_solution(result[0], id_sector)
        cout = cout_rex_service.predict_cout_solution(result[0], id_sector)
        
        solution = Solution(
            num=result[0],
            titre=result[1],
            estimPersoGain=gain,
            estimPersoCout=cout
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

# def get_data_solution(code_solution):
#     results = sol_repository.get_data_solution(code_solution)
#     return DataSolution(

#     )