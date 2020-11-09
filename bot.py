from telethon import TelegramClient, events

# получить надо на my.telegram.org
api_id = 1231231 # api_id
api_hash = "API_HASH"


mode = True

def to_fence(s):
    return ''.join([s[i].upper() if i%2 == 0 else s[i].lower() for i in range(len(s))])

@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    global mode
    if event.raw_text == "/switch":
        mode = False if mode else True
    elif event.raw_text != '' and mode:
        msg = to_fence(event.raw_text)
        await client.edit_message(event.chat_id, event._message_id, msg)

def main():
    client = TelegramClient('session', api_id, api_hash)
    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()