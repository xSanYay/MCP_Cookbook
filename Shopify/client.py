#  this is a very simple shopify MCP client
import requests
import json

# Basic setup for Storefront MCP server requests
store_domain = 'your-store.myshopify.com'
mcp_endpoint = f'https://{store_domain}/api/mcp'

# Example request using the endpoint
headers = {
    'Content-Type': 'application/json'
}

payload = {
    'jsonrpc': '2.0',
    'method': 'tools/call',
    'id': 1,
    'params': {
        'name': 'search_shop_catalog',
        'arguments': {'query': 'coffee', 
                      'context':''}
    }
}

response = requests.post(
    url=mcp_endpoint,
    headers=headers,
    json=payload
)

# Print the response
print(response.json())



