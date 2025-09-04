import chainlit as cl
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print("Key loaded:", os.getenv("OPENAI_API_KEY"))  # just for testing
