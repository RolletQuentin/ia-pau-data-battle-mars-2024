from api.repositories import solution_rex_repository


def get_solutions_for_one_rex(code_rex):
    results = solution_rex_repository.get_all_for_one_rex(code_rex)
    data = []
    return data
