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
                tbltauxmonnaie.*,
                tblcoutrex.*,
                tblgainrex.*,
                -- technoreference.sigletechno AS sigletechnoreference,
                techno1.sigletechno AS sigletechno1,
                techno2.sigletechno AS sigletechno2,
                techno3.sigletechno AS sigletechno3
            FROM tblrex
            JOIN tblreference ON tblreference.numreference = tblrex.codereference
            JOIN tbltauxmonnaie ON tbltauxmonnaie.numtauxmonnaie = tblrex.codetauxmonnaie
            JOIN tblregion ON tblregion.numregion = tblreference.coderegion
            JOIN tblcoutrex ON tblcoutrex.coderex = tblrex.numrex
            JOIN tblgainrex ON tblgainrex.coderex = tblrex.numrex
            -- JOIN tbltechno AS technoreference ON technoreference.numtechno = tblreference.codetechno
            JOIN tbltechno AS techno1 ON techno1.numtechno = tblrex.codeTechno1
            JOIN tbltechno AS techno2 ON techno2.numtechno = tblrex.codeTechno2
            JOIN tbltechno AS techno3 ON techno3.numtechno = tblrex.codeTechno3
            LIMIT 10;
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

def get_all_for_one_solution(code_solution, code_langue):
    cursor = mydb.cursor(dictionary=True)

    query = f"""
        SELECT
            tblcoutrex.coderex,
            tblreference.codesecteur,
            tblreference.datereference,
            tblreference.coderegion,
            tblcoutrex.*,
            tblgainrex.*,
            tblmonnaie.shortmonnaie,
            tbldictionnaireenergie.traductiondictionnairecategories AS nomenergie,
            tbldictionnaireperiodeeconomie.traductiondictionnairecategories AS nomperiodeeconomie,
            tbldictionnaireperiodeenergie.traductiondictionnairecategories AS nomperiodeenergie
        FROM
            tblgainrex
        LEFT JOIN tblrex ON tblrex.numrex = tblgainrex.coderex
        LEFT JOIN tblreference ON tblreference.numreference = tblrex.codereference
        LEFT JOIN tblmonnaie ON tblmonnaie.nummonnaie = tblgainrex.codemonnaiegainrex
        LEFT JOIN tbldictionnairecategories AS tbldictionnaireenergie ON
            tbldictionnaireenergie.codeappelobjet = tblgainrex.uniteenergiegainrex
            AND tbldictionnaireenergie.codelangue = %s
            AND tbldictionnaireenergie.typedictionnairecategories = "uni"
        LEFT JOIN tbldictionnairecategories AS tbldictionnaireperiodeeconomie ON
            tbldictionnaireperiodeeconomie.codeappelobjet = tblgainrex.codeperiodeeconomie
            AND tbldictionnaireperiodeeconomie.codelangue = %s
            AND tbldictionnaireperiodeeconomie.typedictionnairecategories = "per"
        LEFT JOIN tbldictionnairecategories AS tbldictionnaireperiodeenergie ON
            tbldictionnaireperiodeenergie.codeappelobjet = tblgainrex.codeperiodeenergie
            AND tbldictionnaireperiodeenergie.codelangue = %s
            AND tbldictionnaireperiodeenergie.typedictionnairecategories = "per"
        LEFT JOIN tblcoutrex ON tblcoutrex.coderex = tblgainrex.coderex AND tblcoutrex.codesolution = tblgainrex.codesolution
        LEFT JOIN tblreference AS coutrex_reference ON coutrex_reference.numreference = tblrex.codereference
        WHERE 
            tblgainrex.codesolution = %s;

    """

    cursor.execute(query,(code_langue,code_langue,code_langue,code_solution,))
    results = cursor.fetchall()
    cursor.close()
    return results


