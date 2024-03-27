from api.dependencies import mydb


def get_technologie(code_technologie,code_langue):
       # Create cursor object
    cursor = mydb.cursor()
    query = f"""
        SELECT 
            traductiondictionnaire
        FROM 
            tbldictionnaire 
        WHERE 
            codelangue = %s and
            typedictionnaire = 'tec' and 
            codeappelobjet = %s;
        """

    cursor.execute(query,(code_langue,code_technologie))
    results = cursor.fetchall()
    cursor.close()
    return results[0][0] if results else None