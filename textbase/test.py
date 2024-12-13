from main import on_message
import textbase
from textbase.message import Message
from textbase import models

if __name__ == "__main__":
    print("### Personalised Medicine RecSys ###\n     ### STARTED ###  ")
    user_prompt = input("\nUser Input: ")
    user_msg = Message(content=user_prompt, role='user')

    chatGPT_res = on_message(list(user_prompt))["choices"][0]["message"]["content"]

    print("\nBot: {chatGPT_res}")