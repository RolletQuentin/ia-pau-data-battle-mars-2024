from api.repositories import sec_repository

from api.models.Sector import Sector

def get_all_sector():
    data = []

    sectors_dict = {}
    results = sec_repository.get_all_sector()

     # Traitement de chaque ligne de résultat
    for main_category, sub_category in results:
        # Vérifie si la catégorie principale est déjà dans le dictionnaire
        if main_category not in sectors_dict:
            # Si non, l'ajoute avec une nouvelle liste contenant la sous-catégorie
            sectors_dict[main_category] = [sub_category]
        else:
            # Si oui, ajoute simplement la sous-catégorie à la liste existante
            sectors_dict[main_category].append(sub_category)
    
    data = Sector(sectors=sectors_dict)
    return data