from api.dependencies import mydb


def get_short_monnaie(code_monnaie):
    # Create cursor object
    cursor = mydb.cursor()

    # Execute the query
    query = f"""
        SELECT * FROM mydatabase.tblmonnaie
        JOIN tbltauxmonnaie ON tbltauxmonnaie.codemonnaie = tblmonnaie.nummonnaie
        WHERE tblmonnaie.nummonnaie = %s;
        """
    cursor.execute(query, (code_monnaie,))

    # Get the results and column names
    results = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]

    # Combine column names with data using zip
    data_with_columns = [dict(zip(column_names, row)) for row in results]

    # Close the cursor
    cursor.close()

    return data_with_columns[0]
