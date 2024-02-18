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