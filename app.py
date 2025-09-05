import chainlit as cl
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    "max_tokens": 900,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": ["```"],
}
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#print("Key loaded:", os.getenv("OPENAI_API_KEY"))  
@cl.on_chat_start

async def on_start():
    await cl.Message(
        content="Hi, what can I do for you today?!",
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
    stream=client.chat.completions.create(messages=[
        {"role": "user", "content": message.content}],stream=True,**settings)
    msg=await cl.Message(content="").send()
    async for chunk in stream:
        if token := chunk.choices[0].delta.content:
            await msg.stream_token(token)
            
    await msg.update()

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