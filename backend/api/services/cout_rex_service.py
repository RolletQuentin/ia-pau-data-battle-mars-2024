from api.models.CoutRex import CoutRex

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
            monnaie=monnaie_service.get_monnaie(result["codemonnaiecoutrex"]),
            code_unite_cout=result["codeunitecoutrex"],
            code_difficulte=result["codedifficulte"]
        ))

    return data
