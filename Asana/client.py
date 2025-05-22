# install mcp cli before running this
# pip install "mcp[cli]"

import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    # Define the Asana MCP server URL
    server_url = "https://mcp.asana.com/sse"
    
    # Add authentication headers
    access_token = "YOUR_ACCESS_TOKEN"  # Replace with your actual token
    headers = {"Authorization": f"Bearer {access_token}"}

    # Connect to the MCP server using SSE with authentication headers
    async with sse_client(server_url, headers=headers) as (read, write):
        # Initialize the client session
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("Available Tools:")
            for tool in tools:
                print(f"- {tool.name}: {tool.description}")

            # Example: Call a tool (e.g., list incomplete tasks)
            result = await session.call_tool("list-incomplete-tasks", arguments={"assignee": "me"})
            print("Result:", result)

# Run the main function
asyncio.run(main())

