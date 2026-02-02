from dotenv import load_dotenv
import os

# Load env vars
loaded = load_dotenv(verbose=True)
print(f"load_dotenv() returned: {loaded}")

# Check specific keys
grok_key = os.getenv("GROK_API_KEY")
xai_key = os.getenv("XAI_API_KEY")

print(f"GROK_API_KEY: {grok_key if grok_key else 'Not Found'}")
print(f"XAI_API_KEY: {xai_key[:5] + '...' if xai_key else 'Not Found'}")

# Check current working directory to ensure we are where we think we are
print(f"CWD: {os.getcwd()}")
print(f"File exists .env: {os.path.exists('.env')}")
