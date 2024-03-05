from api.repositories import rex_repository

from api.models.Rex import Rex
from api.models.Reference import Reference
from api.models.Region import Region
from api.models.SolutionRex import SolutionRex
from api.models.CoutRex import CoutRex


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
                        national_region=True if result["nationnalregion"] == 1 else False,
                        latitude=result["latregion"],
                        longitude=result["longregion"]
                    ),
                    ville_reference=result["villereference"],
                    techno=result["codetechno"],
                    code_secteur=result["codesecteur"],
                    is_recup_chaleur=False if result["isrecupchaleur"] == 0 else True
                )
            )
            data.append(rex)

    return data
