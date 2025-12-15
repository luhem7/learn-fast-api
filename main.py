from fastapi import FastAPI, Query, HTTPException
from typing import Dict, Optional, List
from pydantic import BaseModel

app = FastAPI(
    title="Learn FastAPI",
    description="A simple FastAPI application to demonstrate basic endpoints and Swagger documentation",
    version="1.0.0",
    license_info={
        "name": "GPL v3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
)


class StockPrice(BaseModel):
    ticker: str
    price: float


class BuyStockRequest(BaseModel):
    ticker: str
    quantity: int


class BuyStockResponse(BaseModel):
    ticker: str
    quantity: int
    price_per_share: float
    total_cost: float
    remaining_volume: int


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


@app.get(
    "/stocks/{ticker}/price",
    response_model=StockPrice,
    summary="Get Stock Price",
    description="Returns the latest price of a stock given its ticker symbol",
    response_description="A JSON object containing the stock price information",
    tags=["stocks"]
)
async def get_stock_price(ticker: str):
    """
    Get the latest price of a stock by ticker symbol.
    
    This endpoint fetches the current price of a stock from the FICTIONAL_STOCK_DATA
    dictionary using the provided ticker symbol.
    
    Args:
        ticker: The stock ticker symbol (e.g., AAPL, GOOGL, MSFT)
    
    Returns:
        StockPrice: An object containing:
            - ticker: The stock ticker symbol
            - price: The current price of the stock
    
    Raises:
        HTTPException: 401 error if the ticker is not available for trading
    """
    # Convert ticker to uppercase for case-insensitive matching
    ticker_upper = ticker.upper()
    
    # Check if the ticker exists in our fictional stock data
    if ticker_upper not in FICTIONAL_STOCK_DATA:
        raise HTTPException(
            status_code=401, 
            detail=f"Stock ticker '{ticker}' is not available for trading"
        )
    
    stock_info = FICTIONAL_STOCK_DATA[ticker_upper]
    
    return StockPrice(
        ticker=ticker_upper,
        price=stock_info["price"]
    )


@app.post(
    "/stocks/buy",
    response_model=BuyStockResponse,
    summary="Buy Stock Shares",
    description="Buy a specified quantity of shares for a given stock ticker",
    response_description="A JSON object containing the purchase details",
    tags=["stocks"]
)
async def buy_stock(request: BuyStockRequest):
    """
    Buy shares of a stock.
    
    This endpoint allows purchasing a specified quantity of shares for a given stock.
    It validates that the stock exists and that sufficient shares are available.
    
    Args:
        request: BuyStockRequest containing ticker and quantity to buy
    
    Returns:
        BuyStockResponse: An object containing:
            - ticker: The stock ticker symbol
            - quantity: Number of shares purchased
            - price_per_share: Price per individual share
            - total_cost: Total cost of the purchase
            - remaining_volume: Remaining shares available after purchase
    
    Raises:
        HTTPException: 401 error if ticker doesn't exist or insufficient shares available
    """
    # Convert ticker to uppercase for case-insensitive matching
    ticker_upper = request.ticker.upper()
    
    # Check if the ticker exists in our fictional stock data
    if ticker_upper not in FICTIONAL_STOCK_DATA:
        raise HTTPException(
            status_code=401,
            detail=f"Stock ticker '{request.ticker}' is not available for trading"
        )
    
    stock_info = FICTIONAL_STOCK_DATA[ticker_upper]
    
    # Check if sufficient shares are available
    if request.quantity > stock_info["volume"]:
        raise HTTPException(
            status_code=401,
            detail=f"Insufficient shares available. Requested: {request.quantity}, Available: {stock_info['volume']}"
        )
    
    # Validate quantity is positive
    if request.quantity <= 0:
        raise HTTPException(
            status_code=401,
            detail="Quantity must be a positive number"
        )
    
    # Calculate purchase details
    price_per_share = stock_info["price"]
    total_cost = price_per_share * request.quantity
    new_volume = stock_info["volume"] - request.quantity
    
    # Update the available volume (simulate the purchase)
    FICTIONAL_STOCK_DATA[ticker_upper]["volume"] = new_volume
    
    return BuyStockResponse(
        ticker=ticker_upper,
        quantity=request.quantity,
        price_per_share=price_per_share,
        total_cost=total_cost,
        remaining_volume=new_volume
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)