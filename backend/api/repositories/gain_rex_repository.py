from api.dependencies import mydb


def get_all_for_one_rex(code_rex):
    # Create cursor object
    cursor = mydb.cursor()

    # Execute the query
    query = f"""
        SELECT
            tblgainrex.*,
            tblreference.codesecteur,
            tblreference.datereference,
            tblmonnaie.shortmonnaie,
            tbldictionnaireenergie.traductiondictionnairecategories AS nomenergie,
            tbldictionnaireperiodeeconomie.traductiondictionnairecategories AS nomperiodeeconomie,
            tbldictionnaireperiodeenergie.traductiondictionnairecategories AS nomperiodeenergie
        FROM
            tblgainrex
        LEFT JOIN tblrex ON tblrex.numrex = tblgainrex.coderex
        LEFT JOIN tblreference ON tblreference.numreference = tblrex.codereference
        LEFT JOIN tblmonnaie ON tblmonnaie.nummonnaie = tblgainrex.codemonnaiegainrex
        JOIN tbldictionnairecategories AS tbldictionnaireenergie ON
            tbldictionnaireenergie.codeappelobjet = tblgainrex.uniteenergiegainrex
            AND tbldictionnaireenergie.codelangue = 2
            AND tbldictionnaireenergie.typedictionnairecategories = "uni"
        LEFT JOIN tbldictionnairecategories AS tbldictionnaireperiodeeconomie ON
            tbldictionnaireperiodeeconomie.codeappelobjet = tblgainrex.codeperiodeeconomie
            AND tbldictionnaireperiodeeconomie.codelangue = 2
            AND tbldictionnaireperiodeeconomie.typedictionnairecategories = "per"
        LEFT JOIN tbldictionnairecategories AS tbldictionnaireperiodeenergie ON
            tbldictionnaireperiodeenergie.codeappelobjet = tblgainrex.codeperiodeenergie
            AND tbldictionnaireperiodeenergie.codelangue = 2
            AND tbldictionnaireperiodeenergie.typedictionnairecategories = "per"
        WHERE tblgainrex.coderex = %s;
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


def get_all_for_one_solution(code_solution, code_secteur):
    # Create cursor object
    cursor = mydb.cursor()

    # Execute the query
    query = f"""
        SELECT
            tblgainrex.*,
            tblreference.codesecteur,
            tblreference.datereference,
            tblmonnaie.shortmonnaie,
            tbldictionnaireenergie.traductiondictionnairecategories AS nomenergie,
            tbldictionnaireperiodeeconomie.traductiondictionnairecategories AS nomperiodeeconomie,
            tbldictionnaireperiodeenergie.traductiondictionnairecategories AS nomperiodeenergie
        FROM
            tblgainrex
        LEFT JOIN tblrex ON tblrex.numrex = tblgainrex.coderex
        LEFT JOIN tblreference ON tblreference.numreference = tblrex.codereference
        LEFT JOIN tblmonnaie ON tblmonnaie.nummonnaie = tblgainrex.codemonnaiegainrex
        JOIN tbldictionnairecategories AS tbldictionnaireenergie ON
            tbldictionnaireenergie.codeappelobjet = tblgainrex.uniteenergiegainrex
            AND tbldictionnaireenergie.codelangue = 2
            AND tbldictionnaireenergie.typedictionnairecategories = "uni"
        LEFT JOIN tbldictionnairecategories AS tbldictionnaireperiodeeconomie ON
            tbldictionnaireperiodeeconomie.codeappelobjet = tblgainrex.codeperiodeeconomie
            AND tbldictionnaireperiodeeconomie.codelangue = 2
            AND tbldictionnaireperiodeeconomie.typedictionnairecategories = "per"
        LEFT JOIN tbldictionnairecategories AS tbldictionnaireperiodeenergie ON
            tbldictionnaireperiodeenergie.codeappelobjet = tblgainrex.codeperiodeenergie
            AND tbldictionnaireperiodeenergie.codelangue = 2
            AND tbldictionnaireperiodeenergie.typedictionnairecategories = "per"
        WHERE tblgainrex.codesolution = %s
          AND tblreference.codesecteur = %s;
        """
    cursor.execute(query, (code_solution, code_secteur,))

    # Get the results and column names
    results = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]

    # Combine column names with data using zip
    data_with_columns = [dict(zip(column_names, row)) for row in results]

    # Close the cursor
    cursor.close()

    return data_with_columns
