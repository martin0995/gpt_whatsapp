# This module will handle the interaction with ChatGPT
from gpt_api import send_prompt

def chat_with_gpt(message):
    """Initiate a conversation with ChatGPT."""
    # You can customize the prompt structure based on your use case
    prompt = f"{message}"
    try:
        response = send_prompt(prompt)
    except Exception as e:
        response = f"An error occurred while processing the message: {str(e)}"
        
    return response
