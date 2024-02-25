from fastapi import FastAPI
from src.app.service_example.controller.exemple_controller import router as ExampleRouter
from src.app.common.security.security_middleware import SecurityMiddleware

security_middleware = SecurityMiddleware()

app = FastAPI()

# Add middleware with basic config
app.add_middleware(
    security_middleware.middleware,
    keycloak_configuration=security_middleware.config,
    exclude_patterns=security_middleware.excluded_routes
)

app.include_router(ExampleRouter, tags=['Example'], prefix='/example')

@app.get('/', tags=['Root'])
async def home():
    return {'API':'Example Service'}