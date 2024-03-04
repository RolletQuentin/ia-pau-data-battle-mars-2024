from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myuser",
    password="mypassword",
    database="mydatabase"
)

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello world from FastAPI!"}


@app.get("/get_solutions")
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


@app.get("/get_study_cases")
async def get_all_data():
    try:
        # Create cursor object
        cursor = mydb.cursor()

        # Execute the query
        query = """
            SELECT
                tblrex.numrex,
                tblrex.codemonnaie,
                tblrex.gainfinancierrex,
                tblrex.gainfinancierperioderex,
                tblrex.energierex,
                tblrex.codeuniteenergie,
                tblrex.codeperiodeenergie,
                tblrex.codeenergierex,
                tblrex.gesrex,
                tblrex.ratiogainrex,
                tblrex.trirex,
                tblrex.capexrex,
                tblrex.capexperioderex,
                tblrex.codeTechno1,
                tblrex.codeTechno2,
                tblrex.codeTechno3,
                tblrex.codetravaux,
                tblrex.codereseau,
                tblregion.codepays,
                tblreference.coderegion,
                tblreference.codesecteur,
                tblcoutrex.reelcoutrex,
                tblcoutrex.codemonnaiecoutrex,
                tblcoutrex.codedifficulte,
                tblgainrex.gainfinanciergainrex,
                tblgainrex.codemonnaiegainrex,
                tblgainrex.codeperiodeeconomie,
                tblgainrex.energiegainrex,
                tblgainrex.uniteenergiegainrex,
                tblgainrex.codeperiodeenergie,
                tblgainrex.gesgainrex,
                tblgainrex.trireelgainrex
            FROM tblrex
            JOIN tblreference ON tblreference.numreference = tblrex.codereference
            JOIN tblregion ON tblregion.numregion = tblreference.coderegion
            JOIN tblcoutrex ON tblcoutrex.coderex = tblrex.numrex
            JOIN tblgainrex ON tblgainrex.coderex = tblrex.numrex
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
