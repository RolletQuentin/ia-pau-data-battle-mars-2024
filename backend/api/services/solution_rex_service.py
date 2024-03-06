from api.models.GainRex import GainRex
from api.models.CoutRex import CoutRex
from api.models.SolutionRex import SolutionRex

from api.services import gain_rex_service, cout_rex_service


def get_solutions_for_one_rex(code_rex):
    gains: list[GainRex] = gain_rex_service.get_all_for_one_rex(code_rex)
    couts: list[CoutRex] = cout_rex_service.get_all_for_one_rex(code_rex)

    print(gains)
    print(couts)

    data = []
    num_solutions = []

    if gains is not None:
        # gains treatment
        for gain in gains:
            # it is the first time we encountred a solution
            if not (gain.code_solution in num_solutions):
                data.append(SolutionRex(
                    num=gain.code_solution,
                    couts=[],
                    gains=[gain]
                ))
                num_solutions.append(gain.code_solution)

            else:
                index_solution = num_solutions.index(gain.code_solution)
                solution: SolutionRex = data[index_solution]
                solution.gains.append(gain)

    if couts is not None:
        # couts treatment
        for cout in couts:
            # it is the first time we encountred a solution
            if not (cout.code_solution in num_solutions):
                data.append(SolutionRex(
                    num=cout.code_solution,
                    couts=[cout],
                    gains=[]
                ))
                num_solutions.append(cout.code_solution)

            else:
                index_solution = num_solutions.index(cout.code_solution)
                solution: SolutionRex = data[index_solution]
                solution.couts.append(cout)

    return data
