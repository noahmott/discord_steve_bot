import os
from dotenv import load_dotenv

# Only load .env file if it exists (local development)
if os.path.exists('.env'):
    load_dotenv()

# Get environment variables with fallbacks
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Validate required environment variables
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable is required")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required") 