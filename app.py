import chainlit as cl
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#print("Key loaded:", os.getenv("OPENAI_API_KEY"))  

@cl.on_message
async def main(message: str):
    await cl.Message(comtent=f"Received:{message.content}",).send()

