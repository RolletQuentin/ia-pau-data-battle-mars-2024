import re
import os
import csv
import warnings
import mysql.connector

from bs4 import BeautifulSoup

sql_path = "../../../mysql/db_backup_plateforme_2024-01-10_010001.sql"

warnings.filterwarnings("ignore", category=UserWarning)

def cleanHTML(html_content):
    # Utilise BeautifulSoup pour convertir le contenu HTML en texte, tout en décodant les entités HTML.
    return BeautifulSoup(html_content, 'html.parser').get_text()

def clean(text):
    # Nettoie le HTML et convertit les entités en texte normal.
    text = cleanHTML(text)
    # Remplace les séquences d'échappement par leur caractère correspondant.
    text = re.sub(r"\\'", "'", text)  # Remplace \' par '
    text = re.sub(r"\\n", " ", text)  # Remplace \n par un espace
    text = re.sub(r"\\r", " ", text)  # Remplace \r par un espace
    # Supprime tous les guillemets doubles
    text = re.sub(r'"', '', text)  # Retire tous les guillemets doubles
    text = re.sub(r"'", '', text)  # Retire tous les guillemets doubles
    # Remplace les espaces multiples et les nouvelles lignes par un seul espace, et enlève les espaces de début et de fin.
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def getSolutions():
    mydb = mysql.connector.connect(
        host="localhost",
        user="myuser",
        password="mypassword",
        database="mydatabase"
    )

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, "solutions2.csv")

    cursor = mydb.cursor(dictionary=True)  # Use a dictionary cursor

    query = """
        SELECT 
            sol.numsolution AS codeSolution,
            sol.codetechno AS codeTechno,
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
    cursor.close()

    cursor = mydb.cursor(dictionary=True)  # Use a dictionary cursor

    query = """
        SELECT 
            codeappelobjet AS codeTechno,
            indexdictionnaire AS categorie,
            traductiondictionnaire AS content
        FROM 
            mydatabase.tbldictionnaire 
        where 
            typedictionnaire = "tec" and 
            indexdictionnaire in ( 1, 2) and 
            codelangue = 2 
        order by 
            codeappelobjet;
    """
    cursor.execute(query)
    technos = cursor.fetchall()
    cursor.close()

    
    # Convert solutions into a more usable structure (e.g., a dictionary)

    solutions_dict = {}
    for row in solutions:
        key = (row['codeSolution'], row['categorie'])  # Clé unique sous forme de tuple
        value = {'codeParent': row['codeParent'], 'content': row['content']}  # Valeurs associées à la clé
        solutions_dict[key] = value


    techno_dict = {}
    for row in technos:
        key = (row["codeTechno"], row['categorie'])
        value = {'codeTechno': row['codeTechno'], 'content': row['content']}
        techno_dict[key] = value

    csv_data = []
    # Update the original solutions list with inherited content
    for sol in solutions:
        if sol['categorie'] == 1 :
            if sol['codeTechno'] and sol['codeTechno'] != 1:
                for i in [1,2]:
                    if techno_dict.get((sol['codeTechno'], i)):
                        content = clean(techno_dict.get((sol['codeTechno'], i))['content'])
                        csv_data.append([sol['codeSolution'], i+20, clean(content)])

            if sol['codeParent']:
                for i in [1,2,5,6,9,10,11,12]:
                    if solutions_dict.get((sol["codeSolution"],i)) is None and solutions_dict.get((sol["codeParent"],i)) is not None:
                        content = clean(solutions_dict.get((sol["codeParent"], i))['content'])
                        csv_data.append([sol['codeSolution'], i, clean(content)])
        
        csv_data.append([sol['codeSolution'], sol['categorie'], clean(sol['content'])])
    
    # Write solutions to a CSV file
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')  # utiliser | comme séparateur
        for row in csv_data:
            writer.writerow(row)
    
    mydb.close()


getSolutions()  

