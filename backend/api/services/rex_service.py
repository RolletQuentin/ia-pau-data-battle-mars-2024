from api.repositories import rex_repository

from api.services import monnaie_service
from api.services import solution_rex_service

from api.models.Rex import Rex
from api.models.Reference import Reference
from api.models.Region import Region
from api.models.TauxMonnaie import TauxMonnaie
from api.models.Techno import Techno


def get_all():
    data = []
    rex_nums = []
    results = rex_repository.get_all()

    for result in results:

        # if the rex is not already created, we created it
        if not (result["numrex"] in rex_nums):
            rex = Rex(
                num=result["numrex"],
                reference=Reference(
                    num=result["codereference"],
                    region=Region(
                        num=result["numregion"],
                        code_pays=result["codepays"],
                        national_region=True if result["nationalregion"] == 1 else False,
                        latitude=result["latregion"],
                        longitude=result["longregion"]
                    ),
                    ville_reference=result["villereference"],
                    techno=Techno(
                        num=result["codetechno"],
                        sigle="nothing"  # TODO : change this to get the real sigle
                    ) if result["codetechno"] > 1 else None,
                    code_secteur=result["codesecteur"],
                    is_recup_chaleur=False if result["isrecupchaleur"] == 0 else True
                ),
                code_public=result["codepublic"],
                monnaie=monnaie_service.get_monnaie(result["codemonnaie"]),
                taux_monnaie=TauxMonnaie(
                    num=result["codetauxmonnaie"],
                    monnaie=monnaie_service.get_monnaie(result["codemonnaie"]),
                    annee=result["anneetauxmonnaie"],
                    valeur_taux=result["valeurtauxmonnaie"]
                ),
                gain_financier=result["gainfinancierrex"],
                code_gain_financier_periode=result["gainfinancierperioderex"],
                gain_energie=result["energierex"],
                code_unite_energie=result["codeuniteenergie"],
                code_periode_energie=result["codeperiodeenergie"],
                code_energie=result["codeenergierex"],
                gain_ges=result["gesrex"],
                ratio_gain=result["ratiogainrex"],
                tri=result["trirex"],
                capex=result["capexrex"],
                capex_periode=result["capexperioderex"],
                opexrex=result["opexrex"],
                techno1=Techno(
                    num=result["codeTechno1"],
                    sigle=result["sigletechno1"]
                ) if result["codeTechno1"] > 1 else None,
                techno2=Techno(
                    num=result["codeTechno2"],
                    sigle=result["sigletechno2"]
                ) if result["codeTechno2"] > 1 else None,
                techno3=Techno(
                    num=result["codeTechno3"],
                    sigle=result["sigletechno3"]
                ) if result["codeTechno3"] > 1 else None,
                code_travaux=result["codetravaux"],
                code_reseau=result["codereseau"],
                solutions=solution_rex_service.get_solutions_for_one_rex(
                    result["numrex"])
            )
            data.append(rex)

    return data
