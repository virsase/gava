from pyrogram import Client
from pyrogram import types, filters
import time
import random

delay = 1
comments = ['Первый нах!!!!']

api_id = 123456789
api_hash = "123abcdefg"


app = Client(
    "bio",
    api_id=api_id,
    api_hash=api_hash
)


@app.on_message(filters=filters.forwarded)
def my_handler(client, message):
    comment=random.choice(comments)
    print(f'NEW POST :: {message.sender_chat.title}')
    time.sleep(delay)
    app.send_message(
        chat_id=message.chat.id,
        text=comment,
        reply_to_message_id=message.id
        )

app.run()