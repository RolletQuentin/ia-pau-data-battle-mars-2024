from api.dependencies import mydb


def get_technologie(code_technologie):
       # Create cursor object
    cursor = mydb.cursor()
    query = f"""
        SELECT 
            traductiondictionnaire
        FROM 
            tbldictionnaire 
        WHERE 
            codelangue = 2 and
            typedictionnaire = 'tec' and 
            codeappelobjet = %s;
        """

    cursor.execute(query,(code_technologie,))
    results = cursor.fetchall()
    cursor.close()
    return results[0][0] if results else None