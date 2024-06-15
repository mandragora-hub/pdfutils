from typing import Annotated
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from app import utils;

app = FastAPI()

origins = ["*"]  # allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_index():
    return FileResponse('static/index.html')


@app.get("/metadata/")
def read_item(url: Annotated[str, Query(description="URL where a pdf file is located.", min_length=5, max_length=100)]):
    content = utils.read_file_from_url(url)
    result = utils.extract_pdf_metadata(content)
    return result


app.mount("/static", StaticFiles(directory="static"), name="static")
