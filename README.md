# Scaffold Python Services Project

Basic commands to start python projects

Enviroment and Requirement

```console
 python -m venv venv
 .\venv\Scripts\activate
 pip install -r requirements.txt
```

 Documentation [https://www.mkdocs.org/getting-started/]

```console
 mkdocs serve
```

 Run APIs [https://fastapi.tiangolo.com/] + [https://www.uvicorn.org/]

```console
uvicorn src.app.service_example.api:app --reload
```

Run workers

```console
python worker.py service_event_store
```

 Start Containers

```console
 docker-compose -f .\container\rabbitmq\docker-compose.yaml up
 ```
