import asyncio
import aiohttp

all_data = []
async def get_data(session, id):
  url = f"http://5.182.86.225/{id}"
  async with session.get(url) as res:
    file = url.split('/')[-1] + '.html'
    resp_text = await res.text()
    all_data.append(resp_text)
    with open(file, 'w') as f:
      f.write(resp_text)
    return resp_text

async def load_data():
  id_list = [
      '6',
      '7'
  ]
  async with aiohttp.ClientSession() as session:
    tasks = [
        asyncio.create_task(get_data(session, id))
        for id in id_list
    ]
    await asyncio.gather(*tasks)

asyncio.run(load_data())