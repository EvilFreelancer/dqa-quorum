import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

PROMPT_TEMPLATE = os.getenv("PROMPT_TEMPLATE")

MAX_TOKENS_INPUT = int(os.getenv("MAX_TOKENS_INPUT", 4000))
MAX_TOKENS_OUTPUT = int(os.getenv("MAX_TOKENS_OUTPUT", 10))
