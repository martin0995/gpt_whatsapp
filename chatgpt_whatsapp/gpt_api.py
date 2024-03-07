import logging
import os
from openai import OpenAI
from utils import format_chat_for_api

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)

def send_prompt(prompt):
    """Send a prompt to the GPT-3.5 API."""

    logging.debug(f"Sending prompt to GPT-3.5: {prompt}")
    formatted_chat = format_chat_for_api(prompt)

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": formatted_chat,
                }
            ],
            model="gpt-3.5-turbo",
        )
    except Exception as e:
        raise e
    
    logging.debug(f"RESPONSE from GPT-3.5: {chat_completion.choices[0].text.strip()}")
    return chat_completion.choices[0].text.strip()
