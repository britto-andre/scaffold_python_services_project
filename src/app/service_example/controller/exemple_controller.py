from fastapi import APIRouter, HTTPException, Body
from src.app.service_example.service.example_service import ExampleService
from src.app.service_example.entity.example import Example

router = APIRouter()
service = ExampleService()

@router.post('/')
async def create(obj: Example = Body(...)):
    id = service.create(obj)
    return {'message': 'Example Created', '_id': str(id)}

@router.get('/{id}')
async def find_on_by_id(id):
    return service.find_one_by_id(id)

@router.get('/')
async def list():
    list = service.list()
    return {'list': list}

@router.delete('/{id}')
async def delete(id):
    result = service.request_delete(id)
    if not result:
        raise HTTPException(status_code= 404, detail= {'message': 'Example not found', '_id': id})
    return {'message': 'Delete requested', '_id': id}