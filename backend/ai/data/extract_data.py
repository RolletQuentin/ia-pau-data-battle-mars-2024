import re
import os
import csv
import mysql.connector


sql_path = "../../../mysql/db_backup_plateforme_2024-01-10_010001.sql"

def clean(text):
    text = re.sub('<.*?>', '',text)
    text = re.sub(r"\\'", "'", text)  # Remplace \' par '
    text = re.sub(r"\\n", " ", text)  # Remplace \n par un espace
    text = re.sub(r"\\r", " ", text)  # Remplace \r par un espace
    text = re.sub(r'\\"', '"', text)  # Remplace \" par "
    text = re.sub(r"^'", '', text)  # Supprime l'apostrophe au début de la chaîne
    text = re.sub(r"'$", '', text)  # Supprime l'apostrophe à la fin de la chaîne
    text = re.sub(r'\s+', ' ', text).strip()  # Nettoie les espaces multiples et enlève les espaces de début et de fin
    return text


def extractDictionnary(sql_path,output_file,element,codes):
    # Obtention du chemin absolu du répertoire contenant le script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construction du chemin d'accès au fichier SQL relatif à l'emplacement du script
    sql_file_path = os.path.join(script_dir, sql_path)
    output_file_path = os.path.join(script_dir, output_file)

    # Conversion de la liste des codes en une chaîne pour l'expression régulière
    codes_pattern = '|'.join(map(str, codes))

    # Expression régulière pour extraire les lignes qui correspondent à vos critères
    pattern = re.compile(rf",2,'{element}',(.{{1,4}}?),(?:{codes_pattern})," )

    # Ouverture et traitement du fichier SQL
    with open(sql_file_path, 'r') as file,  open(output_file_path, 'w',encoding='utf-8') as output:
        for line in file:
            # Divise la ligne en plusieurs lignes si elle contient "),("
            split_lines = re.split(r'\),\(', line)
            for sub_line in split_lines:
                # Vérifie si la sous-ligne correspond au motif
                if pattern.search(sub_line):
                    # Séparation des colonnes par des virgules
                    columns = sub_line.split(',',5)                 
                    columns[5] = re.sub('<.*?>', '',columns[5])
                    columns[5] = re.sub(r"\\'", "'", columns[5])  # Remplace \' par '
                    columns[5] = re.sub(r"\\n", " ", columns[5])  # Remplace \n par un espace
                    columns[5] = re.sub(r"\\r", " ", columns[5])  # Remplace \r par un espace
                    columns[5] = re.sub(r'\\"', '"', columns[5])  # Remplace \" par "
                    columns[5] = re.sub(r"^'", '', columns[5])  # Supprime l'apostrophe au début de la chaîne
                    columns[5] = re.sub(r"'$", '', columns[5])  # Supprime l'apostrophe à la fin de la chaîne
                    columns[5] = re.sub(r'\s+', ' ', columns[5]).strip()  # Nettoie les espaces multiples et enlève les espaces de début et de fin

                    # Écriture des colonnes autres que les trois premières dans le fichier CSV
                    output.write('|'.join(columns[3:]) + '\n')


def getSolutions():
    mydb = mysql.connector.connect(
        host="localhost",
        user="myuser",
        password="mypassword",
        database="mydatabase"
    )

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, "solutions.csv")

    cursor = mydb.cursor(dictionary=True)  # Use a dictionary cursor

    query = """
        SELECT 
            sol.numsolution AS codeSolution,
            CASE
                WHEN sol.codeparentsolution = 1 THEN NULL
                ELSE sol.codeparentsolution
            END AS codeParent,
            dic.indexdictionnaire AS categorie, 
            dic.traductiondictionnaire AS content
        FROM 
            tbldictionnaire AS dic
        JOIN 
            tblsolution AS sol ON dic.codeappelobjet = sol.numsolution
        LEFT JOIN 
            tblsolution AS solpar ON sol.codeparentsolution = solpar.numsolution
        WHERE 
            dic.codelangue = 2 AND 
            dic.typedictionnaire = 'sol' AND
            sol.validsolution = 1 AND
            dic.indexdictionnaire IN (1, 2, 5, 6, 9, 10, 11, 12)
        ORDER BY 
            sol.numsolution;
    """
    cursor.execute(query)
    solutions = cursor.fetchall()
    
    # Convert solutions into a more usable structure (e.g., a dictionary)

    solutions_dict = {}
    for row in solutions:
        key = (row['codeSolution'], row['categorie'])  # Clé unique sous forme de tuple
        value = {'codeParent': row['codeParent'], 'content': row['content']}  # Valeurs associées à la clé
        solutions_dict[key] = value

    csv_data = []
    # Update the original solutions list with inherited content
    for sol in solutions:
        if sol['codeParent'] and sol['categorie'] == 1:
            for i in [1,2,5,6,9,10,11,12]:
                if solutions_dict.get((sol["codeSolution"],i)) is None and solutions_dict.get((sol["codeParent"],i)) is not None:
                    content = solutions_dict.get((sol["codeParent"], i))['content']
                    csv_data.append([sol['codeSolution'], i, clean(content)])
        
        csv_data.append([sol['codeSolution'], sol['categorie'], clean(sol['content'])])
   
    # Write solutions to a CSV file
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')  # utiliser | comme séparateur
        for row in csv_data:
            writer.writerow(row)
    
    cursor.close()
    mydb.close()


getSolutions()  


def mapSolutionsToTech():

    mydb = mysql.connector.connect(
        host="localhost",
        user="myuser",
        password="mypassword",
        database="mydatabase"
    )
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, "solutions_Technologies_Mapping.csv")
    
    cursor = mydb.cursor()

    query = f"""
        SELECT numsolution,
            validsolution 
        FROM mydatabase.tblsolution;
    """

    cursor.execute(query)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for row in cursor:
            # Création d'une chaîne de caractères pour chaque ligne, où les valeurs sont séparées par des virgules
            formatted_row = '|'.join(map(str, row))
            # Écriture de la chaîne dans le fichier de sortie
            output_file.write(formatted_row + '\n')

    cursor.close()
    mydb.close()

mapSolutionsToTech()

