from api.repositories import monnaie_repository

from api.models.Monnaie import Monnaie


def get_short_monnaie(code_monnaie: int):
    result = monnaie_repository.get_short_monnaie(code_monnaie)
    return Monnaie(
        num=result["nummonnaie"],
        short_monnaie=result["shortmonnaie"],
        valeur_taux=result["valeurtauxmonnaie"]
    )


def convert_to_euro(code_monnaie: int, amount: float):
    monnaie = get_short_monnaie(code_monnaie)
    return amount * monnaie.valeur_taux
