import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

EMAIL = os.getenv("ATLASSIAN_EMAIL")
API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN")
MCP_URL = os.getenv("MCP_URL")

# Safety check
if not EMAIL or not API_TOKEN or not MCP_URL:
    raise ValueError("Missing required environment variables. Check your .env file.")

response = requests.get(
    MCP_URL,
    auth=HTTPBasicAuth(EMAIL, API_TOKEN),
    headers={"Accept": "text/event-stream"},
    stream=True
)

if response.status_code == 200:
    print("Connected to Atlassian MCP successfully.")
else:
    print("Connection failed:", response.status_code)