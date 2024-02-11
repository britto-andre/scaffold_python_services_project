from fastapi import FastAPI
from src.app.service_example.controller.exemple_controller import router as ExampleRouter

app = FastAPI()
app.include_router(ExampleRouter, tags=['Example'], prefix='/example')

@app.get('/', tags=['Root'])
async def home():
    return {'API':'Example Service'}