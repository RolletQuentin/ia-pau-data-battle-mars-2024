from fastapi import APIRouter, HTTPException

from api.dependencies import mydb

from api.models.Rex import Rex

router = APIRouter(
    prefix="/rex"
)


@router.get("/get_all")
async def get_all_data():
    try:
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
            LIMIT 100;
        """
        cursor.execute(query)

        # Get the results and column names
        results = cursor.fetchall()
        column_names = [column[0] for column in cursor.description]

        # Combine column names with data using zip
        data_with_columns = [dict(zip(column_names, row)) for row in results]

        # Close the cursor
        cursor.close()

        return {"data": "test"}

    except Exception as e:
        # If a problem occurs, return a code 500 error (Internal Server Error)
        raise HTTPException(status_code=500, detail=str(e))
