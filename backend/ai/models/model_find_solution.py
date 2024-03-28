import pandas as pd
import re
import unicodedata
import spacy
from bs4 import BeautifulSoup
from spacy.lang.fr.stop_words import STOP_WORDS
import pickle
from sentence_transformers import SentenceTransformer, util
from sentence_transformers.quantization import quantize_embeddings
import numpy as np
import os
import copy


def load_and_merge_data(csv_file='../data/solutions.csv'):
    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construction du chemin d'accès au fichier relatif à l'emplacement du script
    csv_file_path = os.path.join(script_dir, csv_file)
    dictionnaire_solution = {1: "Titre", 2: "Description", 5: "Application",
                             6: "Bilan énergétique", 21: "Titre technologie", 22: "Description technologie"}
    # Charger le fichier CSV en spécifiant le séparateur '|'
    df = pd.read_csv(csv_file_path, sep='|', header=None)
    # Initialiser une liste pour stocker les données de chaque solution
    solutions_data = []
    # Parcourir chaque ligne du DataFrame
    for index, row in df.iterrows():
        id_sol = row[0]
        section = row[1]
        texte = row[2]
        # Vérifier si la section correspond à une clé dans le dictionnaire de solutions
        if section in dictionnaire_solution:
            # Récupérer le nom de la section
            section_name = dictionnaire_solution[section]
            # Chercher si la solution existe déjà dans la liste
            solution_exists = False
            for solution in solutions_data:
                if solution[0] == id_sol:
                    solution_exists = True
                    solution[1][section_name] = texte
                    break
            # Si la solution n'existe pas encore, la créer
            if not solution_exists:
                new_solution = [id_sol, {section_name: texte}]
                solutions_data.append(new_solution)
    return solutions_data


def clean_df_solutions(df_solutions):
    cleaned_data = []
    for item in df_solutions:
        index = item[0]
        solution = item[1]
        cleaned_solution = {}
        for key, value in solution.items():
            if (key == 'Titre' or key == 'Titre technologie'):
                # Pour les titres, ne pas enlever les chiffres
                cleaned_solution[key] = clean_text(
                    str(value), remove_numbers=False)
            else:
                # Pour les autres champs, enlever les chiffres
                cleaned_solution[key] = clean_text(
                    str(value), remove_numbers=True)
        cleaned_data.append([index, cleaned_solution])
    return cleaned_data


def clean_text(text, remove_numbers=True):
    # Nettoyer HTML Tags
    text = BeautifulSoup(text, 'html.parser').get_text()
    # Remplacer "&nbsp;." par rien
    text = re.sub(r'&nbsp;\.', '', text)
    # Supprimer les "l'"
    text = re.sub(r"\bl'", '', text)
    # Accents
    text = unicodedata.normalize('NFD', text).encode(
        'ascii', 'ignore').decode("utf-8")
    if remove_numbers:
        # Retirer les numéros
        text = re.sub(r'\b\d+\b', '', text)
    # Supprimer les caractères seuls
    text = re.sub(r'\b\w\b', '', text)
    # Tokenization, Lemmatization, Removing Stopwords, Lowercase
    doc = nlp(text)
    cleaned_sentences = []
    for sentence in doc.sents:
        tokens = [token.lemma_.lower(
        ) for token in sentence if not token.is_stop and not token.is_punct and not token.is_space]
        clean_sentence = ' '.join(tokens)
        if clean_sentence:
            # Ajouter un point à la fin de la phrase propre
            cleaned_sentences.append(clean_sentence)
    # Joining the cleaned sentences back into a single string
    cleaned_text = ' '.join(cleaned_sentences)
    return cleaned_text


def encoder_embeddings(data, model, output_file):
    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, output_file)
    # Faire une copie de data
    data = copy.deepcopy(data)
    # Fonction pour encoder chaque texte

    def encoder_texte(texte):
        return model.encode(texte)
    # Pour chaque entrée dans les données, encoder tous les champs texte
    for entry in data:
        # print("DEBUG : entry = ", entry)
        for champ, valeur in entry[1].items():
            # print("DEBUG : champ =", champ, ", valeur = ", valeur)
            if isinstance(valeur, str):  # S'assurer que la valeur est une chaîne de caractères
                # Calculer l'embedding
                embedding = encoder_texte(valeur)
                # Remplacer le texte par l'embedding
                entry[1][champ] = embedding.tolist()
    # Sauvegarder les embeddings dans un fichier
    with open(output_file_path, 'wb') as file:
        pickle.dump(data, file)
    return data


def calculate_average_embedding(text, model):
    # Diviser le texte en phrases
    sentences = [sentence.strip()
                 for sentence in text.split('.') if sentence.strip()]
    sentence_embeddings = model.encode(sentences)
    # Prendre la moyenne des embeddings des phrases
    if len(sentence_embeddings) > 0:
        average_embedding = np.mean(sentence_embeddings, axis=0)
    else:
        average_embedding = np.zeros(model.get_sentence_embedding_dimension())
    return average_embedding


def encoder_embeddings_moyenne_sentences(data, model, output_file):
    # Faire une copie de data
    data = copy.deepcopy(data)
    # Pour chaque entrée dans les données, encoder tous les champs texte
    for entry in data:
        # print("DEBUG : entry = ", entry)
        for champ, valeur in entry[1].items():
            # print("DEBUG : champ =", champ, ", valeur = ", valeur)
            if isinstance(valeur, str):  # S'assurer que la valeur est une chaîne de caractères
                # Calculer l'embedding en faisant la moyenne de l'embedding de chaque phrase.
                embedding = calculate_average_embedding(valeur, model)
                # Remplacer le texte par l'embedding
                entry[1][champ] = embedding.tolist()
    # Sauvegarder les embeddings dans un fichier
    with open(output_file, 'wb') as file:
        pickle.dump(data, file)
    return data


# # --------------------------------- GENERER L EMBEDDING ----------------------------------------------------
# # Charger le modèle de langue SpaCy
nlp = spacy.load("fr_core_news_sm")
# # Appel de la fonction pour obtenir les données
# df_solutions = load_and_merge_data()
# df_solutions_clean = clean_df_solutions(df_solutions)
# path_embedding_file = "embeddings/FR_camembert_large_avec_moyenne_phrases.pkl"
# solutions_embeddings = encoder_embeddings_moyenne_sentences(df_solutions_clean, model, path_embedding_file)
# # ----------------------------------------------------------------------------------------------------------


# ---------------------------------- INFERENCE --------------------------------------------------------------

# Fonction appelé par notre utilisateur
# Langue : 2 = Français, 3 = Anglais et 4 = Espagnol
def model_find_solution(description, secteur, langage=2, seuil_similarite=0.8, min_sol=5):
    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Si le langage est FR on prend camembert, sinon on prend l'mpnet-base-v2
    if (langage == 2):
        # Charger le modèle
        model = SentenceTransformer("dangvantuan/sentence-camembert-large")
        # Définition du nom du fichier d'embeddings
        embeddings_file = "FR_camembert_large_avec_moyenne_phrases.pkl"
        weights = {"Titre": 1.7, "Description": 2, "Application": 0.7,
                   "Bilan énergétique": 1.7, "Titre technologie": 0.7, "Description technologie": 2}
    else:
        # Charger le modèle
        model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")
        embeddings_file = "model_final_magb_sans_somme_sentences.pkl"
        weights = {"Titre": 1, "Description": 1, "Application": 1,
                   "Bilan énergétique": 1, "Titre technologie": 1, "Description technologie": 1}

    # Construction du chemin d'accès au fichier relatif à l'emplacement du script
    embeddings_file_path = os.path.join(script_dir, embeddings_file)

    # !!!!!!!!!!!! ICI ON A CHOISI DE NE PAS INCLURE LE SECTEUR DANS NOTRE MODELE, COMMENTER LA LIGNE CI-DESOSUS POUR CHANGER CELA --------------
    secteur = ""
    # -------------------------
    # On commence par concaténer notre secteur et notre description.
    requete = secteur + ". " + description
    # Ensuite on applique notre pré-processing
    clean_requete = clean_text(requete, remove_numbers=False)
    clean_requete_vecteur = model.encode(clean_requete)
    # On va lire notre fichier d'embeddings
    with open(embeddings_file_path, "rb") as fIn:
        solutions_embeddings = pickle.load(fIn)
    solutions_similarities = []
    # Maintenant pour chaque solution on va garder notre meilleur similarité cosinus avec notre requete. De plus nous ajouton un poids à chaque champs de notre solution,
    # Description * 1.3, Titre * 0.7, et 1 pour tous les autres.
    # On se retrouve donc avec une liste [[id_sol, max_similarité], ...]
    # Pour chaque entrée dans les données, encoder tous les champs texte
    for entry in solutions_embeddings:
        max_similarity = 0
        id_solution = entry[0]
        for champ, valeur_vecteur in entry[1].items():
            # Coeficient multiplicateur
            weight = weights[champ]
            # On calcul la similarité
            similarity = util.pytorch_cos_sim(
                valeur_vecteur, clean_requete_vecteur)*weight
            # On met à jour le max de similarité
            if similarity > max_similarity:
                max_similarity = similarity
        solution_similarity = [id_solution, max_similarity]
        solutions_similarities.append(solution_similarity)
    # print("DEBUG : ",solutions_similarities)
    # On trie notre liste de solution par ordre croissant
    solutions_similarities.sort(key=lambda x: x[1], reverse=True)
    # On sélectionne les 5 meilleures solutions
    top_min_sol_solutions = [sol[0] for sol in solutions_similarities[:min_sol]]
    # On applique le seuil de similarité aux solutions restantes
    remaining_solutions = [sol[0] for sol in solutions_similarities[min_sol:] if sol[1] > seuil_similarite]
    # On concatène les deux listes de solutions
    final_solutions = top_min_sol_solutions + remaining_solutions
    # On retourne que les solutions et non la similarité
    return final_solutions


if __name__ == "__main__":
    # csv_file = "../studies/data/patrice_test_set.csv"
    csv_file = "../studies/data/dataset_test_Kerdos.csv"

    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construction du chemin d'accès au fichier relatif à l'emplacement du script
    csv_file_path = os.path.join(script_dir, csv_file)

    # Lire le fichier CSV
    df_testset = pd.read_csv(csv_file_path)

    def test_accuracy(dataset=df_testset, top_n=1):
        accuracy = 0
        for i in range(1, len(dataset)):
            predictions = model_find_solution(dataset['Description'][i], "")
            if (dataset["id_solution"][i] in predictions[:top_n]):
                accuracy += 1/len(dataset)
            else:
                print("mal prédit : ", dataset["id_solution"][i])
        return accuracy

    # Tester l'accuracy
    print(test_accuracy())
