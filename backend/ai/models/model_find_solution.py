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






def calculate_average_embedding(text, quantize=False, precision="binary"):
    # Diviser le texte en phrases
    sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
    # Calculer l'embedding de chaque phrase
    if quantize :
        sentence_embeddings = model.encode(sentences, precision=precision)
    else :
        sentence_embeddings = model.encode(sentences)
    # Prendre la moyenne des embeddings des phrases
    if len(sentence_embeddings) > 0:
        average_embedding = np.mean(sentence_embeddings, axis=0)
    else:
        average_embedding = np.zeros(model.get_sentence_embedding_dimension())
    return average_embedding

def pre_processing(texte):
    # Nettoyer HTML Tags
    texte = BeautifulSoup(texte, 'html.parser').get_text()
    # Remplacer "&nbsp;." par rien
    texte = re.sub(r'&nbsp;\.', '', texte)
    # Accents
    texte = unicodedata.normalize('NFD', texte).encode('ascii', 'ignore').decode("utf-8")
    # Retirer les numéros
    texte = re.sub(r'\b\d+\b', '', texte)
    # Tokenization, Lemmatization, Removing Stopwords, Lowercase
    doc = nlp(texte)
    phrases_propres = []
    for phrase in doc.sents:
        tokens = [token.lemma_.lower() for token in phrase if not token.is_stop and not token.is_punct and not token.is_space]
        phrase_propre = ' '.join(tokens)
        if phrase_propre:
            phrases_propres.append(phrase_propre + ".")  # Ajouter un point à la fin de la phrase propre
    # Joining the cleaned sentences back into a single string
    cleaned_text = ' '.join(phrases_propres)
    return cleaned_text


def pre_processing_sections(sections):
    clean_sections = []
    for texte in sections :
        # Nettoyer HTML Tags
        texte = BeautifulSoup(texte, 'html.parser').get_text()
        # Remplacer "&nbsp;." par rien
        texte = re.sub(r'&nbsp;\.', '', texte)
        # Accents
        texte = unicodedata.normalize('NFD', texte).encode('ascii', 'ignore').decode("utf-8")
        # Retirer les numéros
        texte = re.sub(r'\b\d+\b', '', texte)
        # Tokenization, Lemmatization, Removing Stopwords, Lowercase
        doc = nlp(texte)
        phrases_propres = []
        for phrase in doc.sents:
            tokens = [token.lemma_.lower() for token in phrase if not token.is_stop and not token.is_punct and not token.is_space]
            phrase_propre = ' '.join(tokens)
            if phrase_propre:
                phrases_propres.append(phrase_propre + "")
        # Joining the cleaned sentences back into a single string
        cleaned_text = ' '.join(phrases_propres)
        clean_sections.append(cleaned_text)
    return clean_sections




def load_and_merge_data(csv_file = '../data/solutions.csv'):
    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construction du chemin d'accès au fichier relatif à l'emplacement du script
    csv_file_path = os.path.join(script_dir, csv_file)
    # Charger le fichier CSV en spécifiant le séparateur '|'
    df = pd.read_csv(csv_file_path, sep='|', header=None)
    # Renommer les colonnes
    df.columns = ['id_solution', 'categorie', 'texte']
    # Filtrer les lignes pour les catégories spécifiées
    categories_specifiees = [1, 2, 5, 6]
    df_filtre = df[df['categorie'].isin(categories_specifiees)]
    # Pivoter les données pour obtenir les colonnes 'titre', 'definition', 'application' et 'bilan énergie'
    df_pivot = df_filtre.pivot(index='id_solution', columns='categorie', values='texte').reset_index()
    # Renommer les colonnes
    df_pivot.columns = ['id_solution', 'titre', 'definition', 'application', 'bilan_energie']
    # Gérer les valeurs NaN lors de la fusion des colonnes
    def combine_text(row):
        text_parts = [row[col] for col in colonnes if pd.notnull(row[col])]
        return text_parts
    # Sélectionner uniquement les colonnes 'id_solution' et les champs requis
    colonnes = ['titre', 'definition', 'application', 'bilan_energie']
    df_pivot['champs'] = df_pivot.apply(combine_text, axis=1)
    df_final = df_pivot[['id_solution', 'champs']]
    # Convertir en liste de listes pour chaque ligne
    result = df_final.values.tolist()
    return result


def calculate_section_embedding(sections):
    embeddings = []
    for section in sections :
        section_average_embedding = calculate_average_embedding(section)
        embeddings.append(section_average_embedding)
    return embeddings


def genere_embedding(data, output_file, quantize=False, precision="binary"):
    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, output_file)
    # Appliquer la fonction pour calculer l'embedding moyen à chaque texte
    if quantize:
        embeddings = data['clean_text'].apply(calculate_section_embedding, quantize=True)
    else :
        embeddings = data['clean_text'].apply(calculate_section_embedding)
    # Créer un nouveau DataFrame avec id_solution et les embeddings
    new_data = {
        'id_solution': data['id_solution'],
        'text_embedding': embeddings # Désormais mes embeddings sont des listes de solutions contenant chacune les vecteurs de toutes les phrases de la solution.
    }
    # Créer un DataFrame à partir des nouvelles données
    df_embeddings = pd.DataFrame(new_data)
    # Storer les embeddings dans un fichier
    with open(output_file_path, "wb") as fOut:
        pickle.dump(df_embeddings, fOut, protocol=pickle.HIGHEST_PROTOCOL)


def find_solution(text_to_compare, embeddings_file, quantize=False, precision="binary"):
    # Calculer l'embedding moyen du texte à comparer
    embedding_to_compare = calculate_average_embedding(text_to_compare, quantize, precision)
    # Charger les embeddings à partir du fichier
    with open(embeddings_file, "rb") as fIn:
        df_embeddings = pickle.load(fIn)
    list_similarities = []
    # Pour chaque solution
    for solution in df_embeddings['text_embedding'].values:
        embeddings_array = np.stack(solution)
        # Calculer la similarité cosinus entre l'embedding à comparer et les embeddings dans df_embeddings
        similarities = util.pytorch_cos_sim(embedding_to_compare.reshape(1, -1).astype(np.float64), embeddings_array.astype(np.float64))
        max_value, _ = similarities.max(dim=1)
        list_similarities.append(max_value)
    # Ajouter les similarités au DataFrame df_embeddings
    df_embeddings['similarity'] = list_similarities
    # Trier par similarité décroissante
    df_sorted = df_embeddings.sort_values(by='similarity', ascending=False)
    # Récupérer les id_solution et les similarités
    solution_info = df_sorted[['id_solution', 'similarity']].head(10)
    # Convertir en liste de tuples (id_solution, similarity)
    solution_list = list(zip(solution_info['id_solution'], solution_info['similarity']))
    return solution_list


# Charger le modèle spaCy pour le français
nlp = spacy.load("fr_core_news_sm")
# Charger le modèle
model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")

# Fonction appelé par notre utilisateur
def model_find_solution(description, secteur) :
    # !!!!!!!!!!!! ICI ON A CHOISI DE NE PAS INCLURE LE SECTEUR DANS NOTRE MODELE, COMMENTER LA LIGNE CI-DESOSUS POUR CHANGER CELA --------------
    secteur = ""
    # -------------------------

    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Définition du nom du fichier d'embeddings
    embeddings_file = "Architecture-3_paraphrase-multilingual-mpnet-base-v2_embeddings.pkl"
    # Construction du chemin d'accès au fichier relatif à l'emplacement du script
    embeddings_file_path = os.path.join(script_dir, embeddings_file)
    # Vérifier si le fichier d'embeddings existe
    if not os.path.exists(embeddings_file_path):
        print("Le fichier d'embeddings n'existe pas. Génération des embeddings en cours...")
        df_solutions = load_and_merge_data()
        # Convertir la liste de listes en DataFrame pandas
        df_solutions = pd.DataFrame(df_solutions, columns=['id_solution', 'text'])
        # Appliquer le traitement à la colonne "text" de notre df_solutions
        df_solutions['clean_text'] = df_solutions['text'].apply(pre_processing_sections)
        # Générer les embeddings et les sauvegarder dans le fichier
        genere_embedding(df_solutions, embeddings_file_path)
        print("Les embeddings ont été générés et sauvegardés avec succès.")
    # On commence par concaténer notre secteur et notre description.
    text = secteur + ". " + description
    # Ensuite on applique notre pré-processing
    clean_text = pre_processing(text)
    # Ensuite on cherche nos similarités 
    solutions = find_solution(clean_text, embeddings_file_path)
    # On return une liste contenant uniquement le numéros des solutions
    id_solutions = []
    for solution in solutions :
        id_solutions.append(solution[0])
    return id_solutions

if __name__ == "__main__":
    csv_file = "../studies/data/patrice_test_set.csv"
    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construction du chemin d'accès au fichier relatif à l'emplacement du script
    csv_file_path = os.path.join(script_dir, csv_file)


    # Lire le fichier CSV
    df_testset = pd.read_csv(csv_file_path)

    def test_accuracy(dataset=df_testset, top_n=1) :
        accuracy = 0
        for i in range(1,len(dataset)):
            predictions = model_find_solution("", dataset['Description'][i])
            if (dataset["id_solution"][i] in predictions[:top_n]):
                accuracy += 1/len(dataset)
            else :
                print("mal prédit : ", dataset["id_solution"][i])
        return accuracy
    
    # Tester l'accuracy
    print(test_accuracy())