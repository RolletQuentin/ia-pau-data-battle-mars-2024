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
            dic.indexdictionnaire IN (1, 2, 5, 6)
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
        FROM mydatabase.tblsolution
        Where validsolution = 0;
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