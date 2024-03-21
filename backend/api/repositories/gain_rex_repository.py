from api.dependencies import mydb


def get_all_for_one_rex(code_rex):
    # Create cursor object
    cursor = mydb.cursor()

    # Execute the query
    query = f"""
        SELECT tblgainrex.*
        FROM tblgainrex
        WHERE tblgainrex.coderex = {code_rex};
        """
    cursor.execute(query)

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
        SELECT tblgainrex.*
        FROM tblgainrex
        WHERE tblgainrex.codesolution = {code_solution};
        """
    cursor.execute(query)

    # Get the results and column names
    results = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]

    # Combine column names with data using zip
    data_with_columns = [dict(zip(column_names, row)) for row in results]

    # Close the cursor
    cursor.close()

    return data_with_columns
