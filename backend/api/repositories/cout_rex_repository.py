from api.dependencies import mydb


def get_all_for_one_rex(code_rex):
    # Create cursor object
    cursor = mydb.cursor()

    # Execute the query
    query = f"""
        SELECT tblcoutrex.*
        FROM tblcoutrex
        WHERE tblcoutrex.coderex = %s;
        """
    cursor.execute(query, (code_rex,))

    # Get the results and column names
    results = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]

    # Combine column names with data using zip
    data_with_columns = [dict(zip(column_names, row)) for row in results]

    # Close the cursor
    cursor.close()

    return data_with_columns


def get_all_for_one_solution(code_solution):
    # Create cursor object
    cursor = mydb.cursor()

    # Execute the query
    query = f"""
        SELECT tblcoutrex.*, tblreference.codesecteur FROM mydatabase.tblcoutrex
        JOIN tblrex ON tblrex.numrex = tblcoutrex.coderex
        JOIN tblreference ON tblreference.numreference = tblrex.codereference
        WHERE tblcoutrex.codesolution = %s;
        """

    cursor.execute(query, (code_solution,))

    # Get the results and column names
    results = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]

    # Combine column names with data using zip
    data_with_columns = [dict(zip(column_names, row)) for row in results]

    # Close the cursor
    cursor.close()

    return data_with_columns

def get_text(code, code_langue):
    
    cursor = mydb.cursor()

    query = """
        SELECT 
            traductiondictionnaire
        FROM 
            tbldictionnaire
        WHERE
            codelangue = %s AND 
            typedictionnaire = 'rexcout' AND
            codeappelobjet = %s;
    """
    
    cursor.execute(query, (code_langue, code)) 
    results = cursor.fetchall()
    cursor.close()
    
    return results[0][0] if results else None
