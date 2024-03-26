from api.repositories import gain_rex_repository


def normalization(amount, nom_energie):

    normalized_amount = amount
    normalized_nom_energie = nom_energie

    # Convert MWh to kWh
    if nom_energie == "MWh":
        normalized_amount = amount * 1000
        normalized_nom_energie = "kWh"

    # Convert GWh to kWh
    if nom_energie == "GWh":
        normalized_amount = amount * 1000000
        normalized_nom_energie = "kWh"

    # Convert GJ to kWh
    if nom_energie == "GJ":
        normalized_amount = amount * 277.778
        normalized_nom_energie = "kWh"

    # Convert tep to kWh
    if nom_energie == "tep":
        normalized_amount = amount * 11630
        normalized_nom_energie = "kWh"

    # Convert MMBtu to kWh
    if nom_energie == "MMBtu":
        normalized_amount = amount * 293.071
        normalized_nom_energie = "kWh"

    # Convert therms to kWh
    if nom_energie == "therms":
        normalized_amount = amount * 29.3071
        normalized_nom_energie = "kWh"

    # Convert litre to m3
    if nom_energie == "litre":
        normalized_amount = amount / 1000
        normalized_nom_energie = "m3"

    # Convert MAP (mètre cube apparent) to m3
    if nom_energie == "MAP":
        normalized_amount = amount
        normalized_nom_energie = "m3"

    # Convert gallon to m3
    if nom_energie == "gallon":
        normalized_amount = amount * 0.00378541
        normalized_nom_energie = "m3"

    # Convert tonne to kg
    if nom_energie == "tonne":
        normalized_amount = amount * 1000
        normalized_nom_energie = "kg"

    # Convert pounds to kg
    if nom_energie == "pounds":
        normalized_amount = amount * 0.453592
        normalized_nom_energie = "kg"

    # Convert W to kW
    if nom_energie == "W":
        normalized_amount = amount / 1000
        normalized_nom_energie = "kW"

    # Convert HP to kW
    if nom_energie == "HP":
        normalized_amount = amount * 0.7457
        normalized_nom_energie = "kW"

    # Convert kVA to kW
    if nom_energie == "kVA":
        normalized_amount = amount
        normalized_nom_energie = "kW"

    # Convert kWél to kW
    if nom_energie == "kWél":
        normalized_amount = amount
        normalized_nom_energie = "kW"

    # Convert pouce to m
    if nom_energie == "pouce":
        normalized_amount = amount * 0.0254
        normalized_nom_energie = "m"

    # Convert feet to m
    if nom_energie == "feet":
        normalized_amount = amount * 0.3048
        normalized_nom_energie = "m"

    # Convert mm to m
    if nom_energie == "mm":
        normalized_amount = amount / 1000
        normalized_nom_energie = "m"

    # Convert mètre linéaire to m
    if nom_energie == "mètre linéaire":
        normalized_amount = amount
        normalized_nom_energie = "m"

    # Convert pouce² to m²
    if nom_energie == "pouce²":
        normalized_amount = amount * 0.00064516
        normalized_nom_energie = "m²"

    # Convert foot² to m²
    if nom_energie == "foot²":
        normalized_amount = amount * 0.092903
        normalized_nom_energie = "m²"

    # Convert acres to m²
    if nom_energie == "acres":
        normalized_amount = amount * 4046.86
        normalized_nom_energie = "m²"

    # Convert hectare to m²
    if nom_energie == "hectare":
        normalized_amount = amount * 10000
        normalized_nom_energie = "m²"

    # Convert MWh cumac to kWh cumac
    if nom_energie == "MWh cumac":
        normalized_amount = amount * 1000
        normalized_nom_energie = "kWh cumac"

    return normalized_amount, normalized_nom_energie


def predict_ges(code_secteur: int, average_gain_energie: float):

    all_gains_from_sector = gain_rex_repository.get_all_for_one_secteur_ges(
        code_secteur)

    # Get the coefficient between the gain_energie and the gain_ges for the given sector
    coefficient = 0
    for gain in all_gains_from_sector:
        if gain["energiegainrex"] and gain["gesgainrex"] and gain["energiegainrex"] != 0:
            coefficient += gain["gesgainrex"] / gain["energiegainrex"]

    # Calculate the average gain_ges for the given solution
    if len(all_gains_from_sector) == 0:
        predicted_gain_ges = 0
    else:
        predicted_gain_ges = average_gain_energie * \
            coefficient / len(all_gains_from_sector)

    return predicted_gain_ges
