import re
import os


sql_path = "../../../mysql/db_backup_plateforme_2024-01-10_010001.sql"


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
    with open(sql_file_path, 'r') as file,  open(output_file_path, 'w') as output:
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

                    # Écriture des colonnes autres que les trois premières dans le fichier CSV
                    output.write('|'.join(columns[3:]) + '\n')

output_file_solution = "solutions.csv"
codes_solution = [1,2,5,6,9,10,11,12]

extractDictionnary(sql_path, output_file_solution, "sol", codes_solution)


output_file_technologie = "technologie.csv"
codes_technologie = [1,2,3,8,11,13,15]

extractDictionnary(sql_path, output_file_technologie, "tec", codes_technologie)