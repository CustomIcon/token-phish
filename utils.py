import base64
import binascii
import re
import aiohttp


def validate(token: str) -> bool:
    t = token.partition(":")
    try:
        decode = base64.urlsafe_b64decode(f"{t[-1]}====")
    except binascii.Error:
        return False
    return all((t[0].isdecimal(), decode[:2].startswith(b"\x00\x01"), len(decode)))


def check(token: str) -> bool:
    token = re.findall(r"[0-9]{10}:[a-zA-Z0-9_-]{35}", token)
    if len(token) == 0:
        return False, False
    else:
        return True, token[0]


async def request(token):
    async with aiohttp.ClientSession() as ses:
        async with ses.get("https://api.telegram.org/bot{}/getMe".format(token)) as resp:
            validate = await resp.json()
    if validate['ok']:
        return validate["result"]
    else:
        return False
