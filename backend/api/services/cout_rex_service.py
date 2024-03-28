from api.models.CoutRex import CoutRex
from api.models.AverageCout import AverageCout

from api.repositories import cout_rex_repository

from api.services import monnaie_service

from api.dependencies import weighted_mean


def get_all_for_one_rex(code_rex):
    results = cout_rex_repository.get_all_for_one_rex(code_rex)
    data = []
    for result in results:
        data.append(CoutRex(
            num=result["numcoutrex"],
            code_solution=result["codesolution"],
            code_rex=result["coderex"],
            cout_reel=result["reelcoutrex"],
            monnaie=monnaie_service.get_short_monnaie(
                result["codemonnaiecoutrex"]),
            code_unite_cout=result["codeunitecoutrex"],
            code_difficulte=result["codedifficulte"]
        ))

    return data


def get_all_for_one_solution(code_solution):
    results = cout_rex_repository.get_all_for_one_solution(
        code_solution)
    data = []
    for result in results:
        data.append(CoutRex(
            num=result["numcoutrex"],
            code_solution=result["codesolution"],
            code_rex=result["coderex"],
            cout_reel=result["reelcoutrex"],
            monnaie=monnaie_service.get_short_monnaie(
                result["codemonnaiecoutrex"]),
            code_unite_cout=result["codeunitecoutrex"],
            code_difficulte=result["codedifficulte"],
            code_secteur=result["codesecteur"]
        ))

    return data


def predict_cout_solution(code_solution, code_secteur):
    """Predict the cout for a solution. The prediction is based on the cout of the solutions that are similar to the given solution.

    Args:
        code_solution (int): The code of the solution
    """
    int(code_solution)
    int(code_secteur)

    # Get all the couts for the given solution
    couts_solutions = get_all_for_one_solution(code_solution)

    # Get all the couts for the given sector
    couts_sector: list[CoutRex] = None
    if couts_solutions:
        couts_sector = [
            cout for cout in couts_solutions if cout.code_secteur == code_secteur]

    # Remove the couts which are in the sector for not count them twice
    couts_solutions = [
        cout for cout in couts_solutions if cout.code_secteur != code_secteur]

    ############################################################################################################
    # cout
    ############################################################################################################

    average_cout = None
    average_cout_sector = None
    average_cout_solution = None

    # Get the average cout_reel (in euros) for the given solution
    if couts_solutions:
        average_cout_solution = [monnaie_service.convert_to_euro(
            cout.monnaie.num, cout.cout_reel) for cout in couts_solutions if cout.cout_reel is not None]

    # Get the average cout_reel (in euros) for the given sector
    if couts_sector:
        average_cout_sector = [monnaie_service.convert_to_euro(
            cout.monnaie.num, cout.cout_reel) for cout in couts_sector if cout.cout_reel is not None]

    average_cout_solution = weighted_mean(
        average_cout_solution) if average_cout_solution else None
    average_cout_sector = weighted_mean(
        average_cout_sector) if average_cout_sector else None

    if average_cout_solution and average_cout_sector:
        average_cout = average_cout_sector * 0.7 + average_cout_solution * 0.3
    elif average_cout_solution:
        average_cout = average_cout_solution
    elif average_cout_sector:
        average_cout = average_cout_sector

    ############################################################################################################
    # Calculate the number of based solutions
    ############################################################################################################

    number_of_based_solutions = 0

    if couts_solutions:
        number_of_based_solutions += len(couts_solutions)

    if couts_sector:
        number_of_based_solutions += len(couts_sector)

    ############################################################################################################
    # Return the result
    ############################################################################################################

    return AverageCout(
        number_of_based_solutions=number_of_based_solutions,
        average_cout=average_cout
    )
