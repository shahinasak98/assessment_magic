import csv
import config as CONFIG
from io import TextIOWrapper, BytesIO
from sqlalchemy import select
from app.models.users import users, database


async def data_read(
    column_1,
    column_2,
    file
):
    """Function to read data from CSV and
    choose age and name column id given by user
    """
    try:
        if file.content_type != "text/csv":
            return {
                "response": CONFIG.FILE_RESPONSE
            }
        file_content = await file.read()
        text = TextIOWrapper(
            BytesIO(file_content), encoding="utf-8", line_buffering=True
        )
        sheet = list(csv.DictReader(text))
        keys = list(sheet[0].keys())
        if "Name" not in keys or "Age" not in keys:
            return {
                "response": CONFIG.NAME_AGE_RESPONSE
            }
        if (int(column_1) not in range(1, len(keys)+1)) or (
            int(column_2) not in range(1, len(keys)+1)
        ):
            return {
                "response": CONFIG.COLUMN_ID_RESPONSE
            }
        if keys[int(column_1)-1] != "Name" or keys[int(column_2)-1] != "Age":
            name = keys.index("Name")
            age = keys.index("Age")
            return {
                "response": (
                    CONFIG.MAPPING_RESPONSE + (
                        f".Indexes found at {name+1} and {age+1} in the CSV")
                )
            }
        repeat_check = "0"
        for row in sheet:
            query = select(users).where(
                users.c.name == row[keys[int(column_1)-1]] and (
                    users.c.age == row[keys[int(column_2)-1]]
                )
            )
            result = await database.fetch_all(query)
            if not result:
                query = users.insert().values(
                    name=row[keys[int(column_1)-1]],
                    age=row[keys[int(column_2)-1]]
                )
                await database.execute(query)
            else:
                repeat_check = "1"
        response = {
            "response": (
                CONFIG.SUCCESS_RESPONSE +
                CONFIG.REDUNDANT_RESPONSE[repeat_check]
            )}
        return response
    except FileNotFoundError as error:
        return {
            "response": f"Missing file .{str(error)}"
        }
    except IndexError as error:
        return {
            "response": f"An Index error has occured .{str(error)}"
        }
    except Exception as error:
        return {
            "response": f"An exception has occured due to {str(error)}"
        }

