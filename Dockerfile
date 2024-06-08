FROM python:3.10

# Use this image  
# FROM gcr.io/distroless/python3-debian12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./static /code/static

EXPOSE 3000

CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "3000"]