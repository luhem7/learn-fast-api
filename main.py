from fastapi import FastAPI
from typing import Dict

app = FastAPI(
    title="Learn FastAPI",
    description="A simple FastAPI application to demonstrate basic endpoints and Swagger documentation",
    version="1.0.0",
    license_info={
        "name": "GPL v3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
)


@app.get(
    "/hello",
    response_model=Dict[str, str],
    summary="Hello World Endpoint",
    description="Returns a simple Hello World message in JSON format",
    response_description="A JSON object containing a greeting message",
    tags=["greetings"]
)
async def hello_world():
    """
    Simple GET endpoint that returns Hello World as JSON.
    
    This endpoint demonstrates basic FastAPI functionality and returns
    a standardized JSON response with a greeting message.
    
    Returns:
        Dict[str, str]: A dictionary containing a "message" key with "Hello World" value
    """
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)