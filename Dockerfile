FROM python:3.11
WORKDIR  /app

COPY . /app

RUN pip install poetry

# WORKDIR /app/homeworkweb_1

RUN poetry install

EXPOSE 8080
ENV NAME Bot


ENTRYPOINT  ["poetry", "run", "python", "__main__.py"]




