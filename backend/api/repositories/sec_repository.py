from api.dependencies import mydb

def get_all_sector(code_langue):
    # Create cursor object
    cursor = mydb.cursor()

    # Execute the query
    query = """
        SELECT 
            dps.traductiondictionnaire AS nomParentSecteur, 
            ds.traductiondictionnaire AS nomSecteur 
        FROM 
            tblsecteur
        JOIN 
            tbldictionnaire AS dps 
            ON tblsecteur.codeparentsecteur = dps.codeappelobjet
        JOIN 
            tbldictionnaire AS ds 
            ON tblsecteur.numsecteur = ds.codeappelobjet
        WHERE 
            ds.codelangue = %s AND 
            ds.typedictionnaire = 'sec' AND 
            ds.indexdictionnaire = 1 AND 
            dps.codelangue = %s AND 
            dps.typedictionnaire = 'sec' AND 
            dps.indexdictionnaire = 1;
    """

    # The 'code_langue' needs to be passed twice because it is used twice in the query
    cursor.execute(query, (code_langue, code_langue))
    results = cursor.fetchall()
    cursor.close()

    return results


def get_list_sector(code_langue):
    # Création de l'objet cursor
    cursor = mydb.cursor()

    # Création de la requête avec paramètres
    query = """
        SELECT 
            traductiondictionnaire
        FROM 
            tbldictionnaire
        WHERE 
            codelangue = %s AND 
            typedictionnaire = "sec" AND 
            indexdictionnaire = 1;
    """
    
    cursor.execute(query, (code_langue,))

    # Récupération des résultats et conversion en une liste de chaînes
    results = cursor.fetchall()
    # Convertir chaque tuple en chaîne et les rassembler dans une nouvelle liste
    sector_list = [result[0] for result in results]

    # Fermeture du curseur
    cursor.close()
    
    return sector_list


def get_id_sector(sector,code_langue):
    # Création de l'objet cursor
    cursor = mydb.cursor()
    # Création de la requête avec paramètres
    query = """
        SELECT 
            codeappelobjet
        FROM 
            tbldictionnaire
        WHERE 
            codelangue = %s AND 
            typedictionnaire = "sec" AND 
            indexdictionnaire = 1 AND
            traductiondictionnaire = %s;
    """
    
    cursor.execute(query,(code_langue,sector))

    # Récupération des résultats et conversion en une liste de chaînes
    result = cursor.fetchone()

    # Fermeture du curseur après l'opération
    cursor.close()
    
    # Vérifiez si un résultat a été trouvé et retournez-le; sinon, retournez None
    return result[0]


def get_sector(code_sector,code_langue):
       # Create cursor object
    cursor = mydb.cursor()
    query = """
        SELECT 
            traductiondictionnaire
        FROM 
            tbldictionnaire 
        WHERE 
            codelangue = %s and
            typedictionnaire = 'sec' and 
            codeappelobjet = %s;
        """

    cursor.execute(query,(code_langue,code_sector))
    results = cursor.fetchall()
    cursor.close()
    return results[0][0] if results else None
