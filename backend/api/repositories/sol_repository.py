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
    cursor.close()

    return results


def get_data_solution(code_solution):
    # Create cursor object
    cursor = mydb.cursor(dictionary=True)
    query = f"""
        SELECT 
	        indexdictionnaire,
            codeappelobjet as numSolution,
            traductiondictionnaire
        FROM 
	        tbldictionnaire 
        WHERE 
	        codelangue = 2 and
	        typedictionnaire = 'sol' and 
            codeappelobjet = %s;
    """

    cursor.execute(query,(code_solution,))
    results = cursor.fetchall()
    cursor.close()
    return results


def get_codes_solution(code_solution):
       # Create cursor object
    cursor = mydb.cursor(dictionary=True)
    query = f"""
        SELECT 
	        codetechno as codeTechnologie, 
            codeparentsolution as codeParent, 
            
            jaugecoutsolution as jaugeCout,
            reglepouceminicoutsolution as minRDP,
            reglepoucemaxicoutsolution as maxRDP,
            
            jaugegainsolution as jaugeGain, 
            economiemingainsolution as minGain, 
            economiemaxgainsolution as maxGain  
        FROM 
            mydatabase.tblsolution 
        where 
            numsolution = %s;
        """

    cursor.execute(query,(code_solution,))
    results = cursor.fetchall()
    cursor.close()
    return results[0] 