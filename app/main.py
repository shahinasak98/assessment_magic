import config as CONFIG
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.views.views import data_read


app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


@app.get(CONFIG.URL, response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post(CONFIG.URL+"/data_upload/")
async def data_upload(
    request: Request,
    column_1: str = Form(...),
    column_2: str = Form(...),
    file: UploadFile = File(...)
):
    response = await data_read(column_1, column_2, file)
    return response
