import csv
from io import TextIOWrapper, BytesIO
from sqlalchemy import select
from app.models.users import users, database
import config as CONFIG

async def data_read(
    column_1,
    column_2,
    file
):
    try:
        if file.content_type!="text/csv":
            return{
                "response": CONFIG.FILE_RESPONSE
            }
        file_content = await file.read()
        text = TextIOWrapper(BytesIO(file_content), encoding="utf-8", line_buffering=True)
        sheet = list(csv.DictReader(text))
        keys = list(sheet[0].keys())
        if "Name" not in keys or "Age" not in keys:
            return{
                "response": CONFIG.NAME_AGE_RESPONSE
            }
        if int(column_1) not in range(1, len(keys)+1) or int(column_2) not in range(1, len(keys)+1):
            return{
                "response": CONFIG.COLUMN_ID_RESPONSE
            }
        if keys[int(column_1)-1] != "Name" or keys[int(column_2)-1] != "Age":
            return{
                "response": CONFIG.MAPPING_RESPONSE
            }
        for row in sheet:
            query = select(users).where(users.c.name == row[keys[int(column_1)-1]] and users.c.age == row[keys[int(column_2)-1]])
            result = await database.fetch_all(query)
            if not result:
                query = users.insert().values(name=row[keys[int(column_1)-1]], age=row[keys[int(column_2)-1]])
                await database.execute(query)
        return {
            "response": CONFIG.SUCCESS_RESPONSE
        }
    except Exception as error:
        return {
            "response": f"An exception has occured due to {str(error)}"
        }




