import chainlit as cl
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#print("Key loaded:", os.getenv("OPENAI_API_KEY"))  

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"Received: {message.content}").send()