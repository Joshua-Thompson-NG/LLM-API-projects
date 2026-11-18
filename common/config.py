import os
from pathlib import Path
from dotenv import load_dotenv

# Automatically locate and load .env from the project root
ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

# API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def validate_env():
    if not GEMINI_API_KEY:
        raise ValueError("Environment variable GEMINI_API_KEY not set.")

model_name = "gemini-3.5-flash-lite"
MODEL_NAME = model_name

# default generation settings
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_OUTPUT_TOKENS = 1024