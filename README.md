# assessment_magic
Steps to run the code

    Clone the repository and switch to branch --> feature/csv-processing
    Create a virtual env and activate
    Execute --> pip/pip3 install -r requirements.txt
    In the shell give the command --> uvicorn app.main:app --reload
    Ideally , an html page to upload CSV and to give inputs to Name and Age column will be at --> http://localhost:8000/assessment
    Upload a CSV file with keys.
    Give inputs as ids where Name and Age columns are placed in CSV
    Upon your input you will be navigated to --> http://localhost:8000/assessment/data_upload/
    For swagger doc , navigate to http://localhost:8000/docs/
