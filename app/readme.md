																																	CSV Assessement
Steps to  run the code
1) Clone the repository and switch to branch  --> feature/csv-processing
2) Create a virtual env and activate 
3) Execute --> pip/pip3 install -r requirements.txt
4) In the shell give the command -->  uvicorn app.main:app --reload
5) Ideally , an html page to upload CSV and to give inputs to Name and Age column will be at  --> http://localhost:8000/assessment
6) Upload a CSV file with keys. 
7) Give inputs as ids where Name and Age columns are placed in CSV
8) Upon your input you will be navigated to  --> http://localhost:8000/assessment/data_upload/
   
