from api.dependencies import mydb

def get_multiple_solution(solutions, code_langue):
    # Create cursor object
    cursor = mydb.cursor()

    # Prepare the placeholders for the query - one '%s' per solution
    placeholders = ', '.join(['%s'] * len(solutions))

    # Prepare the parameters list, which should include codelangue first followed by all solutions
    parameters = [code_langue] + solutions

    # Execute the query
    query = f"""
        SELECT 
            codeappelobjet, 
            traductiondictionnaire 
        FROM 
            tbldictionnaire 
        WHERE 
            codelangue = %s AND
            typedictionnaire = 'sol' AND 
            indexdictionnaire = 1 AND 
            codeappelobjet IN ({placeholders})   
    """  # Using an f-string to insert placeholders

    cursor.execute(query, parameters)  # Pass the parameters as a single list
    results = cursor.fetchall()
    cursor.close()

    return results


def get_data_solution(code_solution, code_langue):
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
	        codelangue = %s and
	        typedictionnaire = 'sol' and 
            codeappelobjet = %s;
    """

    cursor.execute(query,(code_langue,code_solution))
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