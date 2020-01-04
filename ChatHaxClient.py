from addons.py_websocket import WSClient
from hata import *
from addons import asyncio

client = WSClient(KOKORO,'wss://ChatHax-Server.proxneon.repl.co')

data = 'test'

async def test(data):
    client.send(data.encode())
    client.close()

asyncio.run(test(data))