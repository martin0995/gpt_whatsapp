from config import AI_ROLE

def format_chat_for_api(prompt):
    formatted_chat = [
        {"role": "system", "content": AI_ROLE},
    ]
    formatted_chat.append({"role": "user", "content": prompt})

    return formatted_chat