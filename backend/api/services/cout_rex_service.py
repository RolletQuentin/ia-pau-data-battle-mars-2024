from api.models.CoutRex import CoutRex
from api.models.AverageCout import AverageCout

from api.repositories import cout_rex_repository

from api.services import monnaie_service


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


def get_all_for_one_solution(code_solution, code_secteur):
    results = cout_rex_repository.get_all_for_one_solution(
        code_solution, code_secteur)
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


def predict_cout_solution(code_solution, code_secteur):
    """Predict the cout for a solution. The prediction is based on the cout of the solutions that are similar to the given solution.

    Args:
        code_solution (int): The code of the solution
    """
    # Get all the couts for the given solution
    couts = get_all_for_one_solution(code_solution, code_secteur)

    # Get the average cout_reel for the given solution
    couts = [monnaie_service.convert_to_euro(
        cout.monnaie.num, cout.cout_reel) for cout in couts if cout.cout_reel is not None]
    average_cout = sum(couts) / len(couts) if couts else None

    return AverageCout(
        number_of_based_solutions=len(couts),
        average_cout=average_cout
    )
