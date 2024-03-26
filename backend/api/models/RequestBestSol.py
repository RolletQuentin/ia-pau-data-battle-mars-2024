from pydantic import BaseModel


class RequestBestSol(BaseModel):
    secteur_activite : str
    description : str
    code_langue : int
    