from api.repositories import sol_repository 
from api.repositories import sec_repository
from api.repositories import tec_repository
  
from api.services import gain_rex_service
from api.services import cout_rex_service

from api.models.Solution import Solution
from api.models.DataSolution import DataSolution

from api.models.EstimPerso import EstimPerso


from api.models.EstimGen import EstimGen

from api.models.DataRex import DataRex
from api.models.CoutSol import CoutSol
from api.models.GainSol import GainSol

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
            estimPersoCout=cout,
            codeSector=id_sector
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


def clean_description(message):
    message = re.sub('<.*?>', '',message)
    message = re.sub(r"\\'", "'", message)  # Remplace \' par '
    message = re.sub(r"\\n", " ", message)  # Remplace \n par un espace
    message = re.sub(r"\\r", " ", message)  # Remplace \r par un espace
    message = re.sub(r'\\"', '"', message)  # Remplace \" par "
    message = re.sub(r"^'", '', message)  # Supprime l'apostrophe au début de la chaîne
    message = re.sub(r"'$", '', message)  # Supprime l'apostrophe à la fin de la chaîne
    message = re.sub(r'\s+', ' ', message).strip()  # Nettoie les espaces multiples et enlève les espaces de début et de fin
    return message

def clean(message):
    # message = re.sub('<.*?>', '',message)
    # message = re.sub(r"\\'", "'", message)  # Remplace \' par '
    # message = re.sub(r"\\n", " ", message)  # Remplace \n par un espace
    # message = re.sub(r"\\r", " ", message)  # Remplace \r par un espace
    # message = re.sub(r'\\"', '"', message)  # Remplace \" par "
    # message = re.sub(r"^'", '', message)  # Supprime l'apostrophe au début de la chaîne
    # message = re.sub(r"'$", '', message)  # Supprime l'apostrophe à la fin de la chaîne
    # message = re.sub(r'\s+', ' ', message).strip()  # Nettoie les espaces multiples et enlève les espaces de début et de fin
    return message


def check_description(description):
    if len(description) == 0 or len(description) > 2048:
        return False
    return True


def update_data_from_results(data, results, codes):
    for result in results:
        content = result["traductiondictionnaire"]
        match result["indexdictionnaire"]:
            case 1: data.titre = clean(content)
            case 2: data.definition = clean(content)
            case 5: data.application = clean(content)
            case 6: data.bilanEnergie = clean(content)
            case 9:
                if codes.get("minRDP") is not None and codes.get("maxRDP") is not None:
                    data.estimGen.cout.pouce = f"{int(codes['minRDP'])} - {int(codes['maxRDP'])} % {clean(content)}"
            case 10:
                for difficulte in content.split('</LI>'):
                    cleaned_difficulte = clean(difficulte)
                    if cleaned_difficulte:
                        data.estimGen.cout.difficulte.append(cleaned_difficulte)
            case 11:
                if codes.get("minGain") is not None and codes.get("maxGain") is not None:
                    data.estimGen.gain.gain = f"{int(codes['minGain'])} - {int(codes['maxGain'])} % {clean(content)}"
            case 12:
                for positif in content.split('</LI>'):
                    cleaned_positif = clean(positif)
                    if cleaned_positif:
                        data.estimGen.gain.positif.append(cleaned_positif)


def get_data_solution(code_solution,code_sector):
    data = DataSolution(
        numSolution=code_solution,
        estimPerso=EstimPerso(
            estimPersoCout=cout_rex_service.predict_cout_solution(code_solution,code_sector), 
            estimPersoGain=gain_rex_service.predict_gain_solution(code_solution,code_sector)
        ), 
        estimGen=EstimGen(
            cout=CoutSol(
                difficulte=[]
            ), 
            gain=GainSol(
                positif=[]
            )
        )  
    )

    codes = sol_repository.get_codes_solution(code_solution)
    print(code_sector)
    print(data)
    if codes is None: 
        return data
    
    if (codes["codeTechnologie"] is not None) :
        data.numTechnologie = codes["codeTechnologie"]
        data.technologie = clean(tec_repository.get_technologie(codes["codeTechnologie"]))
    
    if (codes["jaugeCout"] is not None) :
        data.estimGen.cout.jaugeCout = codes["jaugeCout"]

    if (codes["jaugeGain"] is not None) :
        data.estimGen.gain.jaugeGain = codes["jaugeGain"]

    if ((codes["codeParent"] is not None) and (codes["codeParent"] != code_solution)):
        parent_results = sol_repository.get_data_solution(codes["codeParent"])
        update_data_from_results(data, parent_results, codes)


    results = sol_repository.get_data_solution(code_solution)
    print(data)

    update_data_from_results(data, results, codes)



    # Récupérer les données de gain et de coût
    gain = gain_rex_service.get_all_for_one_solution(code_solution)
    cout = cout_rex_service.get_all_for_one_solution(code_solution)

    # Initialiser le dictionnaire pour regrouper les données par code_rex
    rex_groups = {}
    for item in gain:
        if item.code_rex not in rex_groups:
            rex_groups[item.code_rex] = DataRex(
                numRex=item.code_rex, 
                sector= clean(sec_repository.get_sector(item.code_secteur)),
                cout=None,  # Initialiser à None au lieu d'une liste vide
                gain=None)  # Initialiser à None au lieu d'une liste vide
        # Définir gain comme le premier élément trouvé s'il n'est pas déjà défini
        if not rex_groups[item.code_rex].gain:
            rex_groups[item.code_rex].gain = item

    for item in cout:
        if item.code_rex not in rex_groups:
            rex_groups[item.code_rex] = DataRex(
                numRex=item.code_rex, 
                sector= clean(sec_repository.get_sector(item.code_secteur)),
                cout=None,  # Initialiser à None au lieu d'une liste vide
                gain=None)  # Initialiser à None au lieu d'une liste vide
        # Définir cout comme le premier élément trouvé s'il n'est pas déjà défini
        if not rex_groups[item.code_rex].cout:
            rex_groups[item.code_rex].cout = item

    list_rex = list(rex_groups.values())
    data.listRex = list_rex


    return data

