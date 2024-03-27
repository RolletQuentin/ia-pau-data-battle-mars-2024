import sys
import pprint

from api.services import gain_rex_service
from api.services import cout_rex_service

from api.models.AverageGain import AverageGain
from api.models.AverageCout import AverageCout


def calculate_costs_and_gains(code_solution, code_secteur):
    gain: AverageGain = gain_rex_service.predict_gain_solution(
        code_solution, code_secteur, code_langue=2, print_data=False)
    cout: AverageCout = cout_rex_service.predict_cout_solution(
        code_solution, code_secteur)

    return {
        "gain": {
            "number_of_based_solution": gain.number_of_based_solutions,
            "average_fiancial_gain": gain.average_financial_gain,
            "average_energy_gain": gain.average_energy_gain,
            "average_ges_gain": gain.average_ges_gain,
            "average_real_gain": gain.average_real_gain,
            "average_real_tri": gain.average_real_tri,
            "nom_unite_energie": gain.nom_unite_energie,
            "nom_periode_energie": gain.nom_periode_energie,
            "nom_periode_economie": gain.nom_periode_economie
        },
        "cout": {
            "number_of_based_solution": cout.number_of_based_solutions,
            "average_cout": cout.average_cout
        }
    }


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)

    # Vérifiez que les arguments nécessaires sont fournis
    if len(sys.argv) != 3:
        print("Usage: python main.py <code_solution> <code_secteur>")
        sys.exit(1)

    code_solution = sys.argv[1]
    code_secteur = sys.argv[2]

    # Appelez la fonction pour calculer les coûts et les gains
    pp.pprint(calculate_costs_and_gains(code_solution, code_secteur))
