from api.dependencies import mydb

def get_pays_from_coderegion(code_region, code_langue):
       # Create cursor object
    cursor = mydb.cursor()
    query = f"""
        SELECT 
            distinct tbldictionnairecategories.traductiondictionnairecategories
        FROM 
            tblreference 
            JOIN tblregion ON tblreference.coderegion = numregion
            JOIN tbldictionnairecategories ON tblregion.codepays = tbldictionnairecategories.codeappelobjet
        Where 
            tbldictionnairecategories.codelangue = %s
            and tbldictionnairecategories.typedictionnairecategories = 'pay' 
            and tblreference.coderegion = %s;
        """

    cursor.execute(query,(code_langue,code_region))
    results = cursor.fetchall()
    cursor.close()
    return results[0][0] if results else None
