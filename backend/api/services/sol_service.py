from bs4 import BeautifulSoup

from api.repositories import sol_repository 
from api.repositories import sec_repository
from api.repositories import tec_repository
from api.repositories import rex_repository
from api.repositories import cout_rex_repository
from api.repositories import gain_rex_repository

from api.repositories import pays_repository

from api.services import gain_rex_service
from api.services import cout_rex_service
from api.services import monnaie_service

from api.models.Solution import Solution
from api.models.DataSolution import DataSolution

from api.models.EstimPerso import EstimPerso


from api.models.EstimGen import EstimGen

from api.models.DataRex import DataRex
from api.models.CoutRex import CoutRex
from api.models.Monnaie import Monnaie
from api.models.GainRex import GainRex

from api.models.Content import Content


from api.models.CoutSol import CoutSol
from api.models.GainSol import GainSol


import re


def get_multiple_solution(solutions, secteur_activite):
    data = []
    results = sol_repository.get_multiple_solution(solutions)
    id_sector = sec_repository.get_id_sector(str(secteur_activite))
    
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
    
    message = BeautifulSoup(message, 'html.parser').text
    message = re.sub(r"\\'", "'", message)  # Remplace \' par '
    message = re.sub(r"\\n", " ", message)  # Remplace \n par un espace
    message = re.sub(r"\\r", " ", message)  # Remplace \r par un espace
    message = re.sub(r'\\"', '"', message)  # Remplace \" par "
    message = re.sub(r"^'", '', message)  # Supprime l'apostrophe au début de la chaîne
    message = re.sub(r"'$", '', message)  # Supprime l'apostrophe à la fin de la chaîne
    message = re.sub(r'\s+', ' ', message).strip()  # Nettoie les espaces multiples et enlève les espaces de début et de fin
    return message
    message = re.sub(r"\\n", " ", message)  # Remplace \n par un espace


def getTabHTML(html_text: str) -> list[Content]:
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # Find all tables in the HTML
    tables = soup.find_all('table')

    # If there are no tables, return a Content object with all text in 'before'
    if not tables:
        return [Content(before=soup.text.strip())]

    # List to hold Content objects
    contents = []

    # Split the HTML content by tables to process each separately
    parts = re.split('<table.*?</table>', html_text, flags=re.IGNORECASE | re.DOTALL)

    # Initialize an index for the tables to keep track of which tables have been processed
    table_index = 0

    for part in parts[:-1]:  # Exclude the last part for now
        before_text = BeautifulSoup(part, 'html.parser').text.strip()
        # Initialize tab as None; it will be replaced if a table exists
        tab = None
        
        if table_index < len(tables):
            # Extracting the table and converting it into list[list[str]]
            tab = []
            for row in tables[table_index].find_all('tr'):
                cols = row.find_all('td') or row.find_all('th')
                tab.append([ele.text.strip() for ele in cols])
            table_index += 1  # Move to the next table for the next iteration

        # Add the Content object for this section
        contents.append(Content(before=before_text, tab=tab))

    # Handle the last part of the HTML (after the last table, if any)
    last_text = BeautifulSoup(parts[-1], 'html.parser').text.strip()
    if contents:
        contents[-1].after = last_text
    else:
        # This case should not happen since we return early if there are no tables
        contents.append(Content(before=last_text))

    return contents


def cleanHTML(message):
    return  BeautifulSoup(message, 'html.parser').text.strip()

def check_description(description):
    if len(description) == 0 or len(description) > 2048:
        return False
    return True


def update_data_from_results(data, results, codes):
    for result in results:
        content = result["traductiondictionnaire"]
        match result["indexdictionnaire"]:
            case 1: data.titre = cleanHTML(content)
            case 2: data.definition = getTabHTML(content)
            case 5: data.application = getTabHTML(content)
            case 6: data.bilanEnergie = getTabHTML(content)
            case 9:
                if codes.get("minRDP") is not None and codes.get("maxRDP") is not None:
                    data.estimGen.cout.pouce = f"{int(codes['minRDP'])} - {int(codes['maxRDP'])} % {cleanHTML(content)}"
            case 10:
                for difficulte in content.split('</LI>'):
                    cleaned_difficulte = cleanHTML(difficulte)
                    if cleaned_difficulte:
                        data.estimGen.cout.difficulte.append(cleaned_difficulte)
            case 11:
                if codes.get("minGain") is not None and codes.get("maxGain") is not None:
                    data.estimGen.gain.gain = f"{int(codes['minGain'])} - {int(codes['maxGain'])} % {cleanHTML(content)}"
            case 12:
                for positif in content.split('</LI>'):
                    cleaned_positif = cleanHTML(positif)
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
    if codes is None: 
        return data
    
    if (codes["codeTechnologie"] is not None) :
        data.numTechnologie = codes["codeTechnologie"]
        data.technologie = tec_repository.get_technologie(codes["codeTechnologie"])
    
    if (codes["jaugeCout"] is not None) :
        data.estimGen.cout.jaugeCout = codes["jaugeCout"]

    if (codes["jaugeGain"] is not None) :
        data.estimGen.gain.jaugeGain = codes["jaugeGain"]

    if ((codes["codeParent"] is not None) and (codes["codeParent"] != code_solution)):
        parent_results = sol_repository.get_data_solution(codes["codeParent"])
        update_data_from_results(data, parent_results, codes)


    results = sol_repository.get_data_solution(code_solution)

    update_data_from_results(data, results, codes)



    # Récupérer les données de gain et de coût
    rexs = rex_repository.get_all_for_one_solution(code_solution)

    list_rex = []
    # Initialiser le dictionnaire pour regrouper les données par code_rex
    for rex in rexs:
        if ((rex["codesecteur"] == code_sector) and (rex["codesecteur"] is not None)):
            list_rex.append(
                DataRex(
                    numRex= rex["coderex"],
                    sector= sec_repository.get_sector(rex["codesecteur"]),
                    pays = pays_repository.get_pays_from_coderegion(rex["coderegion"]),
                    date = rex["datereference"],
                    cout=CoutRex(
                        code_rex= rex["coderex"],
                        num = rex["numcoutrex"],
                        code_solution=code_solution,
                        text=cout_rex_repository.get_text(rex["numcoutrex"]),
                        cout_reel= rex["reelcoutrex"],
                        monnaie=monnaie_service.get_short_monnaie(rex["codemonnaiecoutrex"]),
                        code_unite_cout= rex["codeunitecoutrex"],
                        code_difficulte= rex["codedifficulte"],
                        code_sector= rex["codesecteur"]
                    ),
                    gain=GainRex(
                        code_rex=rex["coderex"],
                        num=rex["numgainrex"],
                        code_solution= code_solution,
                        text=gain_rex_repository.get_text(rex["numgainrex"]),
                        gain_financier=rex["gainfinanciergainrex"],
                        monnaie=monnaie_service.get_short_monnaie(
                            rex["codemonnaiegainrex"]),
                        code_periode_economie= rex["codeperiodeeconomie"],
                        gain_energie= rex["energiegainrex"],
                        unite_energie=rex["uniteenergiegainrex"],
                        code_periode_energie=rex["codeperiodeenergie"],
                        gain_ges=rex["gesgainrex"],
                        gain_reel=rex["reelgainrex"],
                        tri_reel=rex["trireelgainrex"],
                        nom_periode_economie=rex["nomperiodeeconomie"],
                        nom_unite_energie=rex["nomenergie"],
                        nom_periode_energie=rex["nomperiodeenergie"],
                        code_secteur=rex["codesecteur"]

                    )
                )
            )
    
    for rex in rexs:
        if ((rex["codesecteur"] != code_sector) and (rex["codesecteur"] is not None)):
            list_rex.append(
                DataRex(
                    numRex= rex["coderex"],
                    sector= sec_repository.get_sector(rex["codesecteur"]),
                    pays = pays_repository.get_pays_from_coderegion(rex["coderegion"]),
                    date = rex["datereference"],
                    cout=CoutRex(
                        code_rex= rex["coderex"],
                        num = rex["numcoutrex"],
                        code_solution=code_solution,
                        text=cout_rex_repository.get_text(rex["numcoutrex"]),
                        cout_reel= rex["reelcoutrex"],
                        monnaie=monnaie_service.get_short_monnaie(rex["codemonnaiecoutrex"]),
                        code_unite_cout= rex["codeunitecoutrex"],
                        code_difficulte= rex["codedifficulte"],
                        code_sector= rex["codesecteur"]
                    ),
                    gain=GainRex(
                        code_rex=rex["coderex"],
                        num=rex["numgainrex"],
                        code_solution= code_solution,
                        text=gain_rex_repository.get_text(rex["numgainrex"]),
                        gain_financier=rex["gainfinanciergainrex"],
                        monnaie=monnaie_service.get_short_monnaie(rex["codemonnaiegainrex"]),
                        code_periode_economie= rex["codeperiodeeconomie"],
                        gain_energie= rex["energiegainrex"],
                        unite_energie=rex["uniteenergiegainrex"],
                        code_periode_energie=rex["codeperiodeenergie"],
                        gain_ges=rex["gesgainrex"],
                        gain_reel=rex["reelgainrex"],
                        tri_reel=rex["trireelgainrex"],
                        nom_periode_economie=rex["nomperiodeeconomie"],
                        nom_unite_energie=rex["nomenergie"],
                        nom_periode_energie=rex["nomperiodeenergie"],
                        code_secteur=rex["codesecteur"]

                    )
                )
            )
    
    data.listRex = list_rex
    return data

