from fastapi import FastAPI, Query
from typing import Dict, Optional, List

app = FastAPI(
    title="Learn FastAPI",
    description="A simple FastAPI application to demonstrate basic endpoints and Swagger documentation",
    version="1.0.0",
    license_info={
        "name": "GPL v3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
)


FICTIONAL_STOCK_DATA = {
    "AAPL": {"name": "Apple", "price": 150.12, "volume": 10},
    "GOOGL": {"name": "Google", "price": 2750.65, "volume": 50},
    "MSFT": {"name": "Microsoft", "price": 299.87, "volume": 75},
}


@app.get(
    "/hello",
    response_model=Dict[str, str],
    summary="Hello World Endpoint",
    description="Returns a personalized greeting message in JSON format",
    response_description="A JSON object containing a greeting message",
    tags=["greetings"]
)
async def hello_world(name: Optional[str] = Query(None, description="Optional name for personalized greeting")):
    """
    Simple GET endpoint that returns a greeting as JSON.
    
    This endpoint demonstrates basic FastAPI functionality and returns
    a standardized JSON response with a greeting message. If a name
    parameter is provided, it returns a personalized greeting.
    
    Args:
        name: Optional name parameter for personalized greeting
    
    Returns:
        Dict[str, str]: A dictionary containing a "message" key with greeting value
    """
    if name:
        return {"message": f"Hello {name}!"}
    else:
        return {"message": "Hello World!"}


@app.get(
    "/stocks",
    response_model=List[Dict[str, str]],
    summary="Get Available Stocks",
    description="Returns a list of fictional stocks available for trading",
    response_description="A list of stock objects with ticker and name information",
    tags=["stocks"]
)
async def get_stocks():
    """
    Get the list of fictional stocks available to trade.
    
    This endpoint returns all available fictional stocks from the FICTIONAL_STOCK_DATA
    dictionary, providing both the ticker symbol and the common name of each stock.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries, each containing:
            - ticker: The stock ticker symbol
            - name: The common name of the stock
    """
    stocks = []
    for ticker, stock_info in FICTIONAL_STOCK_DATA.items():
        stocks.append({
            "ticker": ticker,
            "name": stock_info["name"]
        })
    return stocks


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)