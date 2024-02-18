from fastapi import APIRouter, HTTPException, status
from src.app.service_event_store.service.event_service import EventService

router = APIRouter()
service = EventService()

@router.get('/{aggregate_type}/{aggregate_id}')
async def list_by_aggregate(aggregate_type: str, aggregate_id: str):
        list = service.list_by_aggregate(aggregate_type, aggregate_id)
        return {'list': list}

# @app.delete("/example/{id}", response_description="Delete a example")
# async def delete_example(id: str):
#     # delete_result = await student_collection.delete_one({"_id": ObjectId(id)})

#     # if delete_result.deleted_count == 1:
#     #     return Response(status_code=status.HTTP_204_NO_CONTENT)

#     raise HTTPException(status_code=404, detail=f"Example {id} not found")