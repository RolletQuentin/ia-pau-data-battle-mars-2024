from api.dependencies import mydb

def get_multiple_solution(solutions):
    # Create cursor object
    cursor = mydb.cursor()
    # Prepare the placeholders for the query - one '%s' per solution
    placeholders = ', '.join(['%s'] * len(solutions))

    # Execute the query
    query = """
        SELECT 
            codeappelobjet, 
            traductiondictionnaire 
        FROM 
            tbldictionnaire 
        WHERE 
            codelangue = 2 and
            typedictionnaire = 'sol' and 
            indexdictionnaire = 1 and 
            codeappelobjet IN ({})   
        """.format(placeholders)  # Using .format() to insert placeholders

    cursor.execute(query, tuple(solutions))
    results = cursor.fetchall()

    print(results)

    cursor.close()


    return results