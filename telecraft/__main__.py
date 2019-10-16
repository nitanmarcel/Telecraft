from . import client, mc, loop, CHAT
from telethon import events


# Capture all the new messages from a group and display them in Minecraft's chat
@client.on(events.NewMessage(incoming=True, outgoing=True, chats=CHAT))
async def capture(event):
    sender = await event.get_sender()
    from_user = '<tg: {}{}>'.format(sender.first_name, sender.last_name or '')
    if event.text:
        mc.postToChat('{} {}'.format(from_user, event.text))
        print('{} {}'.format(from_user, event.text))
    elif event.media:
        mc.postToChat(
            '{} {}'.format(
                from_user, str(
                    event.media.__class__.__name__)))


# Capture all the new messages from Minecraft and send them to a telegram chat
def send(*args, **kwargs):
    while True:
        mc_chat_event = mc.events.pollChatPosts()
        if mc_chat_event:
            loop.create_task(
                client.send_message(
                    CHAT, mc_chat_event[0].message))

# Start the client
async def start():
    await client.start()
    client.loop.run_in_executor(None, send)
    await client.run_until_disconnected()


if __name__ == "__main__":
    client.loop.run_until_complete(start())
