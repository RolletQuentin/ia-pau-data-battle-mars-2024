from collections import Counter

from api.dependencies import weighted_mean

from api.models.GainRex import GainRex
from api.models.AverageGain import AverageGain

from api.repositories import gain_rex_repository

from api.services import monnaie_service
from api.services import energie_service


def get_all_for_one_rex(code_rex):
    results = gain_rex_repository.get_all_for_one_rex(code_rex)
    data = []
    for result in results:
        data.append(GainRex(
            num=result["numgainrex"],
            code_solution=result["codesolution"],
            code_rex=result["coderex"],
            gain_financier=result["gainfinanciergainrex"],
            monnaie=monnaie_service.get_short_monnaie(
                result["codemonnaiegainrex"]),
            code_periode_economie=result["codeperiodeeconomie"],
            gain_energie=result["energiegainrex"],
            unite_energie=result["uniteenergiegainrex"],
            code_periode_energie=result["codeperiodeenergie"],
            gain_ges=result["gesgainrex"],
            gain_reel=result["reelgainrex"],
            tri_reel=result["trireelgainrex"]
        ))


def get_all_for_one_solution(code_solution):
    results = gain_rex_repository.get_all_for_one_solution(code_solution)
    data = []
    for result in results:
        data.append(GainRex(
            num=result["numgainrex"],
            code_solution=result["codesolution"],
            code_rex=result["coderex"],
            gain_financier=result["gainfinanciergainrex"],
            monnaie=monnaie_service.get_short_monnaie(
                result["codemonnaiegainrex"]),
            code_periode_economie=result["codeperiodeeconomie"],
            gain_energie=result["energiegainrex"],
            unite_energie=result["uniteenergiegainrex"],
            code_periode_energie=result["codeperiodeenergie"],
            gain_ges=result["gesgainrex"],
            gain_reel=result["reelgainrex"],
            tri_reel=result["trireelgainrex"],
            nom_periode_economie=result["nomperiodeeconomie"],
            nom_unite_energie=result["nomenergie"],
            nom_periode_energie=result["nomperiodeenergie"],
            code_secteur=result["codesecteur"]
        ))

    return data


def predict_gain_solution(code_solution, code_secteur):
    """Predict the gain for a solution. The prediction is based on the gain of the solutions that are similar to the given solution.

    Args:
        code_solution (int): The code of the solution
        code_secteur (int): The code of the sector
    """

    # Get all the gains for the given solution
    gains_solutions: list[GainRex] = get_all_for_one_solution(code_solution)

    # Filter the gains by the sector
    gains_sector: list[GainRex] = None
    if gains_solutions:
        gains_sector = [
            gain for gain in gains_solutions if gain.code_secteur == code_secteur]

    # Remove the gains which are in the sector for not count them twice
    if gains_solutions:
        gains_solutions = [
            gain for gain in gains_solutions if gain.code_secteur != code_secteur]

    ############################################################################
    # gain_financier
    ############################################################################

    average_gain_financier = None
    financier_gains_solution = None
    financier_gains_sector = None

    # Get the average gain_financier (in euros) for the given solution. Return None if there is no gain_financier
    if gains_solutions:
        financier_gains_solution = [monnaie_service.convert_to_euro(
            gain.monnaie.num, gain.gain_financier) for gain in gains_solutions if gain.gain_financier is not None]

    # Get the average gain_financier (in euros) for the given solution and given sector. Return None if there is no gain_financier
    if gains_sector:
        financier_gains_sector = [monnaie_service.convert_to_euro(
            gain.monnaie.num, gain.gain_financier) for gain in gains_sector if gain.gain_financier is not None]

    average_gain_financier_solution = weighted_mean(
        financier_gains_solution) if financier_gains_solution else None
    average_gain_financier_sector = weighted_mean(
        financier_gains_sector) if financier_gains_sector else None

    if average_gain_financier_solution and average_gain_financier_sector:
        average_gain_financier = average_gain_financier_sector * \
            0.7 + average_gain_financier_solution * 0.3
    elif average_gain_financier_solution:
        average_gain_financier = average_gain_financier_solution
    elif average_gain_financier_sector:
        average_gain_financier = average_gain_financier_sector

    ############################################################################
    # gain_energie
    ############################################################################

    average_gain_energie = None
    energie_gains_solution = None
    energie_gains_sector = None
    normalized_energie_gains_solution = None
    normalized_energie_gains_sector = None
    nom_unite_energie = None

    # Get the average gain_energie for the given solution. Return None if there is no gain_energie
    if gains_solutions:
        energie_gains_solution = [
            (gain.gain_energie, gain.nom_unite_energie) for gain in gains_solutions if gain.gain_energie is not None]

    # Get the average gain_energie for the given solution and given sector. Return None if there is no gain_energie
    if gains_sector:
        energie_gains_sector = [
            (gain.gain_energie, gain.nom_unite_energie) for gain in gains_sector if gain.gain_energie is not None]

    # Normalize the energie_gains_solution
    if energie_gains_solution:
        normalized_energie_gains_solution = [energie_service.normalization(
            energie_gain[0], energie_gain[1]) for energie_gain in energie_gains_solution]

    # Normalize the energie_gains_sector
    if energie_gains_sector:
        normalized_energie_gains_sector = [energie_service.normalization(
            energie_gain[0], energie_gain[1]) for energie_gain in energie_gains_sector]

    # Keep the energy gains with the most same unit
    if normalized_energie_gains_sector:
        nom_unite_energie = Counter(
            [energie_gain[1] for energie_gain in normalized_energie_gains_sector]).most_common(1)[0][0]
        normalized_energie_gains_sector = [
            energie_gain[0] for energie_gain in normalized_energie_gains_sector if energie_gain[1] == nom_unite_energie]
        if normalized_energie_gains_solution:
            normalized_energie_gains_solution = [
                energie_gain[0] for energie_gain in normalized_energie_gains_solution if energie_gain[1] == nom_unite_energie]
    elif normalized_energie_gains_solution:
        nom_unite_energie = Counter(
            [energie_gain[1] for energie_gain in normalized_energie_gains_solution]).most_common(1)[0][0]
        normalized_energie_gains_solution = [
            energie_gain[0] for energie_gain in normalized_energie_gains_solution if energie_gain[1] == nom_unite_energie]

    average_gain_energie_solution = weighted_mean(
        normalized_energie_gains_solution) if normalized_energie_gains_solution else None
    average_gain_energie_sector = weighted_mean(
        normalized_energie_gains_sector) if normalized_energie_gains_sector else None

    if average_gain_energie_solution and average_gain_energie_sector:
        average_gain_energie = average_gain_energie_sector * \
            0.7 + average_gain_energie_solution * 0.3
    elif average_gain_energie_solution:
        average_gain_energie = average_gain_energie_solution
    elif average_gain_energie_sector:
        average_gain_energie = average_gain_energie_sector

    ############################################################################
    # gain_ges
    ############################################################################

    average_gain_ges = None
    ges_gains_solution = None
    ges_gains_sector = None
    predicted_gain_ges = None

    # Get the average gain_ges for the given solution
    if gains_solutions:
        ges_gains_solution = [
            gain.gain_ges for gain in gains_solutions if gain.gain_ges is not None]

    # Get the average gain_ges for the given solution and given sector
    if gains_sector:
        ges_gains_sector = [
            gain.gain_ges for gain in gains_sector if gain.gain_ges is not None]

    average_gain_ges_solution = weighted_mean(
        ges_gains_solution) if ges_gains_solution else None
    average_gain_ges_sector = weighted_mean(
        ges_gains_sector) if ges_gains_sector else None

    if average_gain_ges_solution and average_gain_ges_sector:
        average_gain_ges = average_gain_ges_sector * \
            0.7 + average_gain_ges_solution * 0.3
    elif average_gain_ges_solution:
        average_gain_ges = average_gain_ges_solution
    elif average_gain_ges_sector:
        average_gain_ges = average_gain_ges_sector

    # Calculate the predicted ges for the sector
    if average_gain_energie:
        predicted_gain_ges = energie_service.predict_ges(
            code_secteur, average_gain_energie)

    # Calculate the average_gain_ges with a linear combination of the average_gain_ges and the predicted_gain_ges
    if average_gain_ges and predicted_gain_ges:
        average_gain_ges = average_gain_ges * 0.7 + predicted_gain_ges * 0.3
    elif predicted_gain_ges:
        average_gain_ges = predicted_gain_ges

    ############################################################################
    # gain_reel
    ############################################################################

    average_gain_reel = None
    reel_gains_solution = None
    reel_gains_sector = None

    # Get the average gain_reel for the given solution
    if gains_solutions:
        reel_gains_solution = [
            gain.gain_reel for gain in gains_solutions if gain.gain_reel is not None]

    # Get the average gain_reel for the given solution and given sector
    if gains_sector:
        reel_gains_sector = [
            gain.gain_reel for gain in gains_sector if gain.gain_reel is not None]

    average_gain_reel_solution = weighted_mean(
        reel_gains_solution) if reel_gains_solution else None
    average_gain_reel_sector = weighted_mean(
        reel_gains_sector) if reel_gains_sector else None

    if average_gain_reel_solution and average_gain_reel_sector:
        average_gain_reel = average_gain_reel_sector * \
            0.7 + average_gain_reel_solution * 0.3
    elif average_gain_reel_solution:
        average_gain_reel = average_gain_reel_solution
    elif average_gain_reel_sector:
        average_gain_reel = average_gain_reel_sector

    ############################################################################
    # tri_reel
    ############################################################################

    average_tri_reel = None
    tri_reel_gains_solution = None
    tri_reel_gains_sector = None

    # Get the average tri_reel for the given solution
    if gains_solutions:
        tri_reel_gains_solution = [
            gain.tri_reel for gain in gains_solutions if gain.tri_reel is not None]

    # Get the average tri_reel for the given solution and given sector
    if gains_sector:
        tri_reel_gains_sector = [
            gain.tri_reel for gain in gains_sector if gain.tri_reel is not None]

    average_tri_reel_solution = weighted_mean(
        tri_reel_gains_solution) if tri_reel_gains_solution else None
    average_tri_reel_sector = weighted_mean(
        tri_reel_gains_sector) if tri_reel_gains_sector else None

    if average_tri_reel_solution and average_tri_reel_sector:
        average_tri_reel = average_tri_reel_sector * \
            0.7 + average_tri_reel_solution * 0.3
    elif average_tri_reel_solution:
        average_tri_reel = average_tri_reel_solution
    elif average_tri_reel_sector:
        average_tri_reel = average_tri_reel_sector

    ############################################################################
    # Calculate the number of based solutions
    ############################################################################

    number_of_based_solutions = 0

    if gains_solutions:
        number_of_based_solutions += len(gains_solutions)

    if gains_sector:
        number_of_based_solutions += len(gains_sector)

    ############################################################################
    # Return the average gains
    ############################################################################

    return AverageGain(
        number_of_based_solutions=number_of_based_solutions,
        average_financial_gain=average_gain_financier,
        average_energy_gain=average_gain_energie,
        average_ges_gain=average_gain_ges,
        average_real_gain=average_gain_reel,
        average_real_tri=average_tri_reel,
        nom_unite_energie=nom_unite_energie
    )
