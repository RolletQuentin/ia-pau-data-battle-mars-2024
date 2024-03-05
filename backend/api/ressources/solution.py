from fastapi import APIRouter, HTTPException

from api.dependencies import mydb

router = APIRouter(
    prefix="/solution"
)


@router.get("/get_solutions")
async def get_all_data():
    try:
        # Create cursor object
        cursor = mydb.cursor()

        # Execute the query
        query = """
            SELECT tblsolution.numsolution, tbltechno.fichetechno
            FROM tblsolution
            JOIN tbltechno ON tbltechno.numtechno=tblsolution.codetechno
            LIMIT 100;
        """
        cursor.execute(query)

        # Get the results
        results = cursor.fetchall()

        # Close the cursor
        cursor.close()

        # Make a great JSON
        datas = []
        names = ["numsolution", "fichetechno"]
        for result in results:
            data = {}
            for i in range(len(names)):
                data[names[i]] = result[i]

            datas.append(data)

        # Return datas
        return datas

    except Exception as e:
        # If a problem occurs, return a code 500 error (Internal Server Error)
        raise HTTPException(status_code=500, detail=str(e))
