# Scaffold Python Services Project

Basic commands to start python projects

Enviroment and Requirement

 - python -m venv venv
 - .\venv\Scripts\activate
 - pip install -r requirement.txt


 Documentation [https://www.mkdocs.org/getting-started/]

 - mkdocs serve


 Run APIs [https://fastapi.tiangolo.com/] + [https://www.uvicorn.org/]

 - uvicorn src.app.service_example.api:app --reload

 Start Containers

 - docker-compose -f .\container\rabbitmq\docker-compose.yaml up