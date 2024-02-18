from fastapi import FastAPI
from src.app.service_event_store.controller.event_controller import router as EventRouter

app = FastAPI()
app.include_router(EventRouter, tags=['Event'], prefix='/event')

@app.get('/', tags=['Root'])
async def home():
    return {'API':'Event Service'}