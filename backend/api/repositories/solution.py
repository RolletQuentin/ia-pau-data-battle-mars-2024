def query_get_all_technologie():
    query = """
        SELECT numsolution,codetechno 
        FROM mydatabase.tblsolution;
        """
    return query