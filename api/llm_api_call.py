from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  # Add your own API KEY during development. (recommended: create a .env file and add your groq api key here https://console.groq.com/keys)
)


def chat(content):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content" : "you are a great tech support expert, you clear all the doubts related to tech in only few words, of some one asks other then tech doubts, you wont give them answer, bellow a user has a doubt check wether it is tech related and if so clear it"
            },
            {
                "role": "user",
                "content": content
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content
