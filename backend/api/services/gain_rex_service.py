from api.models.GainRex import GainRex
from api.models.AverageGain import AverageGain

from api.repositories import gain_rex_repository

from api.services import monnaie_service


def get_all_for_one_rex(code_rex):
    results = gain_rex_repository.get_all_for_one_rex(code_rex)
    data = []
    for result in results:
        data.append(GainRex(
            num=result["numgainrex"],
            code_solution=result["codesolution"],
            code_rex=result["coderex"],
            gain_financier=result["gainfinanciergainrex"],
            monnaie=monnaie_service.get_monnaie(result["codemonnaiegainrex"]),
            code_periode_economie=result["codeperiodeeconomie"],
            gain_energie=result["energiegainrex"],
            unite_energie=result["uniteenergiegainrex"],
            code_periode_energie=result["codeperiodeenergie"],
            gain_ges=result["gesgainrex"],
            gain_reel=result["reelgainrex"],
            tri_reel=result["trireelgainrex"]
        ))


def get_all_for_one_solution(code_solution, code_secteur):
    results = gain_rex_repository.get_all_for_one_solution(
        code_solution, code_secteur)
    data = []
    for result in results:
        data.append(GainRex(
            num=result["numgainrex"],
            code_solution=result["codesolution"],
            code_rex=result["coderex"],
            gain_financier=result["gainfinanciergainrex"],
            monnaie=monnaie_service.get_monnaie(result["codemonnaiegainrex"]),
            code_periode_economie=result["codeperiodeeconomie"],
            gain_energie=result["energiegainrex"],
            unite_energie=result["uniteenergiegainrex"],
            code_periode_energie=result["codeperiodeenergie"],
            gain_ges=result["gesgainrex"],
            gain_reel=result["reelgainrex"],
            tri_reel=result["trireelgainrex"]
        ))

    return data


def predict_gain_solution(code_solution, code_secteur):
    """Predict the gain for a solution. The prediction is based on the gain of the solutions that are similar to the given solution.

    Args:
        code_solution (int): The code of the solution
    """
    # Get all the gains for the given solution
    gains = get_all_for_one_solution(code_solution, code_secteur)

    # Get the average gain_financier for the given solution. Return None if there is no gain_financier
    financier_gains = [
        gain.gain_financier for gain in gains if gain.gain_financier is not None]
    average_gain_financier = sum(financier_gains) / \
        len(financier_gains) if financier_gains else None

    # Give the average gain_energie for the given solution. Return None if there is no gain_energie
    energie_gains = [
        gain.gain_energie for gain in gains if gain.gain_energie is not None]
    average_gain_energie = sum(energie_gains) / \
        len(energie_gains) if energie_gains else None

    # Give the average gain_ges for the given solution
    ges_gains = [gain.gain_ges for gain in gains if gain.gain_ges is not None]
    average_gain_ges = sum(ges_gains) / len(ges_gains) if ges_gains else None

    # Give the average gain_reel for the given solution
    reel_gains = [
        gain.gain_reel for gain in gains if gain.gain_reel is not None]
    average_gain_reel = sum(reel_gains) / \
        len(reel_gains) if reel_gains else None

    # Give the average tri_reel for the given solution
    tri_reel_gains = [
        gain.tri_reel for gain in gains if gain.tri_reel is not None]
    average_tri_reel = sum(tri_reel_gains) / \
        len(tri_reel_gains) if tri_reel_gains else None

    return AverageGain(
        number_of_based_solutions=len(gains),
        average_financial_gain=average_gain_financier,
        average_energy_gain=average_gain_energie,
        average_ges_gain=average_gain_ges,
        average_real_gain=average_gain_reel,
        average_real_tri=average_tri_reel
    )
