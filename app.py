import chainlit as cl
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#print("Key loaded:", os.getenv("OPENAI_API_KEY"))  
@cl.on_chat_start

async def on_start():
    await cl.Message(content="Hi, what can I do for you today?!").send() #THis code snippet will be executed when the chat starts
    await cl.Message(
        content="Here’s the demo GIF 👇",
        elements=[
            cl.Image(
                name="demo",
                display="inline",
                url="https://raw.githubusercontent.com/AtulAravindDas/OpenAI-Chat-App-Chainlit/main/Hi.gif"
                # or: url="https://github.com/AtulAravindDas/OpenAI-Chat-App-Chainlit/blob/main/assets/Hi.gif?raw=1"
            )
        ],
    ).send()
@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"Received: {message.content}").send()

'''@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Morning routine ideation",
            message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
            icon="/public/idea.svg",
        ),

        cl.Starter(
            label="Explain superconductors",
            message="Explain superconductors like I'm five years old.",
            icon="/public/learn.svg",
        ),
        cl.Starter(
            label="Python script for daily email reports",
            message="Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
            icon="/public/terminal.svg",
            command="code",
        ),
        cl.Starter(
            label="Text inviting friend to wedding",
            message="Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.",
            icon="/public/write.svg",
        )
    ]'''