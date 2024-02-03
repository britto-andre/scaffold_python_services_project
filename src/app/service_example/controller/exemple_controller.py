from fastapi import APIRouter, HTTPException, Body
from src.app.service_example.service.example_service import ExampleService
from src.app.service_example.entity.example import Example

router = APIRouter()
service = ExampleService()


@router.post('/')
async def create(obj: Example = Body(...)):
    service.create(obj)
    return {'message': 'Example Created'}


# @app.delete("/example/{id}", response_description="Delete a example")
# async def delete_example(id: str):
#     # delete_result = await student_collection.delete_one({"_id": ObjectId(id)})

#     # if delete_result.deleted_count == 1:
#     #     return Response(status_code=status.HTTP_204_NO_CONTENT)

#     raise HTTPException(status_code=404, detail=f"Example {id} not found")