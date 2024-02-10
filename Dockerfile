FROM python:3.12-slim
ARG SOURCE_FOLDER
WORKDIR /application

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src
# COPY ./src/app/common ./src/app/common
# COPY ./src/app/$SOURCE_FOLDER ./src/app/$SOURCE_FOLDER

# CMD uvicorn src.app.service_example.api:app --host 0.0.0.0 --port 8000

# ENTRYPOINT ["uvicorn","src.app.service_example.api:app","--host","0.0.0.0","--port","8000"]