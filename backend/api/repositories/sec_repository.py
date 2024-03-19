from api.dependencies import mydb

def get_all_sector():
    # Create cursor object
    cursor = mydb.cursor()

    # Execute the query
    query = """
        SELECT dps.traductiondictionnaire AS nomParentSecteur, ds.traductiondictionnaire AS nomSecteur 
        FROM tblsecteur
        JOIN tbldictionnaire AS dps ON tblsecteur.codeparentsecteur = dps.codeappelobjet
        JOIN tbldictionnaire AS ds ON tblsecteur.numsecteur = ds.codeappelobjet
        where ds.codelangue=2 and ds.typedictionnaire="sec" and ds.indexdictionnaire=1 and dps.codelangue=2 and dps.typedictionnaire="sec" and dps.indexdictionnaire=1;

    """

    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()


    return results
