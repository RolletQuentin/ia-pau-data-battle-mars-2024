from api.models.GainRex import GainRex

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
