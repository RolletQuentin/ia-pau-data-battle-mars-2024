from api.dependencies import mydb


def get_all():
    # Create cursor object
    cursor = mydb.cursor()

    # Execute the query
    query = """
            SELECT
                tblrex.*,
                tblregion.*,
                tblreference.*,
                tblcoutrex.*,
                tblgainrex.*
            FROM tblrex
            JOIN tblreference ON tblreference.numreference = tblrex.codereference
            JOIN tblregion ON tblregion.numregion = tblreference.coderegion
            JOIN tblcoutrex ON tblcoutrex.coderex = tblrex.numrex
            JOIN tblgainrex ON tblgainrex.coderex = tblrex.numrex
            LIMIT 1;
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
