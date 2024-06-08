import io
import urllib3
import readtime
from typing import Annotated
from fastapi import FastAPI, Query, HTTPException
from pypdf import PdfReader
from starlette.responses import FileResponse


def read_file_from_url(url: str):
    try:
        http = urllib3.PoolManager()
        response = http.request("GET", url)
        return io.BytesIO(response.data)
    except:
        raise HTTPException(status_code=400, detail="Error fetching url.")


def extract_pdf_metadata(content):
    try:
        reader = PdfReader(content)
        metadata = reader.metadata
        number_of_pages = len(reader.pages)

        text = ""
        for i in range(number_of_pages):
            page = reader.pages[i]
            text += page.extract_text()

        readtime_millisecond = readtime.of_text(text).seconds * 1000
        word_count = len(text.split())
    except:
        raise HTTPException(status_code=400, detail="Error reading pdf  .")

    return {"pages": number_of_pages,
            "wordCount": word_count,
            "readTime": readtime_millisecond,
            "metadata": {
                "author": metadata.author,
                "creationDate": metadata.creation_date,
                "keywords": metadata.get("/Keywords"),
                "modificationDate": metadata.modification_date,
                "creator": metadata.creator,
                "producer": metadata.producer,
                "subject": metadata.subject,
                "title": metadata.title}}


app = FastAPI()


@app.get("/")
async def read_index():
    return FileResponse('static/index.html')


@app.get("/metadata/")
def read_item(url: Annotated[str, Query(description="URL where a pdf file is located.", min_length=5, max_length=100)]):
    content = read_file_from_url(url)
    result = extract_pdf_metadata(content)
    return result
