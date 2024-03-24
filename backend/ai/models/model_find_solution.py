import pandas as pd
import re
import unicodedata
import spacy
from bs4 import BeautifulSoup
from spacy.lang.fr.stop_words import STOP_WORDS
import pickle
from sentence_transformers import SentenceTransformer, util
import numpy as np
import os




def load_and_merge_data(csv_file='../data/solutions.csv'):
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

    # Ajouter un point à la fin des colonnes si nécessaire
    colonnes = ['titre', 'definition', 'application', 'bilan_energie']
    for col in colonnes:
        df_pivot[col] = df_pivot[col].apply(lambda x: x.strip() + '.' if isinstance(x, str) and x.strip()[-1] != '.' else x.strip() if isinstance(x, str) else x)
    
    # Gérer les valeurs NaN lors de la fusion des colonnes
    def combine_text(row):
        text_parts = [row[col] for col in colonnes if pd.notnull(row[col])]
        return ' '.join(text_parts)
    
    # Appliquer la fonction pour créer la nouvelle colonne 'text'
    df_pivot['text'] = df_pivot.apply(combine_text, axis=1)

    # Sélectionner uniquement les colonnes 'id_solution' et 'text'
    df_final = df_pivot[['id_solution', 'text']]
    
    return df_final

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

def genere_embedding(data, output_file, quantize=False, precision="binary"):
    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, output_file)
    
    # Appliquer la fonction pour calculer l'embedding moyen à chaque texte
    if quantize:
        embeddings = data['clean_text'].apply(calculate_average_embedding, quantize=True)
    else :
        embeddings = data['clean_text'].apply(calculate_average_embedding)
    
    # Créer un nouveau DataFrame avec id_solution et les embeddings
    new_data = {
        'id_solution': data['id_solution'],
        'text_embedding': embeddings
    }
    
    # Créer un DataFrame à partir des nouvelles données
    df_embeddings = pd.DataFrame(new_data)
    
    # Storer les embeddings dans un fichier
    with open(output_file_path, "wb") as fOut:
        pickle.dump(df_embeddings, fOut, protocol=pickle.HIGHEST_PROTOCOL)
    
    print("Les embeddings ont été storer avec succès.")

def find_solution(text_to_compare, embeddings_file, quantize=False, precision="binary"):
    # Calculer l'embedding moyen du texte à comparer
    embedding_to_compare = calculate_average_embedding(text_to_compare, quantize, precision)
    
    # Charger les embeddings à partir du fichier
    with open(embeddings_file, "rb") as fIn:
        df_embeddings = pickle.load(fIn)
    
    # Calculer la similarité cosinus entre l'embedding à comparer et les embeddings dans df_embeddings
    similarities = util.pytorch_cos_sim(embedding_to_compare.reshape(1, -1), df_embeddings['text_embedding'].values.tolist())
    
    # Ajouter les similarités au DataFrame df_embeddings
    df_embeddings['similarity'] = similarities.flatten()
    
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

def model_PAT(secteur, description):
    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Définition du nom du fichier d'embeddings
    embeddings_file = "paraphrase-multilingual-mpnet-base-v2_embeddings.pkl"

    # Construction du chemin d'accès au fichier relatif à l'emplacement du script
    embeddings_file_path = os.path.join(script_dir, embeddings_file)

    # Vérifier si le fichier d'embeddings existe
    if not os.path.exists(embeddings_file_path):
        print("Le fichier d'embeddings n'existe pas. Génération des embeddings en cours...")
        # Affachage des données chargées
        df_solutions = load_and_merge_data()
        # Appliquons le traitement à la colonne text de notre df_solutions
        df_solutions['clean_text'] = df_solutions['text'].apply(pre_processing)
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
    # Malheureusement nous n'avons pas reçu le domaine d
    # Malheureusement nous n'avons pas reçu le domaine d'activité correspondant aux
    # requetes avec Kerdos.Et pour certaines requetes nous n'avons pas l'Id_solution non
    # plus, dans ce cas il est remplacé par -1.
    dataset_test_kerdos = [
        ["Id_solution", "Domaine_activite", "Description"],
        [724, "", "C'est quoi la HP flottante ?"],
        [914, "", "Je voudrais dimensionner un panneau solaire."],
        [719, "", "Quel gain pour un variateur de vitesse ?"],
        [-1, "", "J'aimerais avoir une régulation optimisée de mon groupe froid."],
        [-1, "", "Comment faire pour réduire la consommation de mon compresseur d'air comprimé ?"]
    ]

    # On va tester sur notre dataset_test
    for i in range(1, len(dataset_test_kerdos)):
        print("--------------------------------------------")
        print("Solution attendue : ", dataset_test_kerdos[i][0])
        print(model_PAT(dataset_test_kerdos[i][1], dataset_test_kerdos[i][2]))