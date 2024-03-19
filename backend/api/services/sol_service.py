from api.repositories import sol_repository
  
from ai.models.model2 import model_Quentin

from api.models.Solution import Solution



def get_multiple_solution(solutions,secteur_activite):
    data = []

    results = sol_repository.get_multiple_solution(solutions,secteur_activite)

    for result in results:
        
        gains = model_Quentin(result[0])
        solution = Solution(
            num=result[0],
            titre=result[1],
            degre_confiance=0,
            gain_monetaire=str(gains[0]),
            gain_watt=str(gains[1]),
            gain_co2=str(gains[2])
        )

        data.append(solution)
    
    return data