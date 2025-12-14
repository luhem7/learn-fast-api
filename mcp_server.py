import httpx
from fastmcp import FastMCP
import asyncio # For an async function to get the spec if needed

# 1. Define the base URL of your running FastAPI API
API_BASE_URL = "http://127.0.0.1:8000" 
OPENAPI_URL = f"{API_BASE_URL}/openapi.json"

# 2. Create an HTTP client that the MCP server will use to call your API
# You can configure authentication headers here if your API requires them.
api_client = httpx.AsyncClient(base_url=API_BASE_URL)

# 3. Load the OpenAPI spec (This would ideally be done at startup)
# For a real-world scenario, you might want to load this from a local file 
# or a remote service during server initialization.
try:
    openapi_spec = httpx.get(OPENAPI_URL).json()
except Exception as e:
    print(f"Error loading OpenAPI spec: {e}")
    exit(1)

# 4. Create the MCP server from the spec and client
mcp_server = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=api_client,
    name="MyFastAPIMCP",
    # Optional: Add global tags to categorize the tools
    tags={"fastapi", "generated-api"},
)

if __name__ == "__main__":
    # Runs the MCP server (e.g., on a different port than your main API)
    mcp_server.run()