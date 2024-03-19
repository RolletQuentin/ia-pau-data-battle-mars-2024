from pydantic import BaseModel


class RequestBestSol(BaseModel):
    secteur_activite : str
    description : str
    