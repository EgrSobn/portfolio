import asyncio
import datetime

async def show_time():
    while True:
        print(datetime.datetime.now())
        await asyncio.sleep(1)

asyncio.run(show_time())
