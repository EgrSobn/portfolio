import aiohttp
import asyncio


async def download_image(url, semaphore):
  async with semaphore:
    async with aiohttp.ClientSession() as session:
      async with session.get(url) as response:
        if response.status == 200:
          image_data = await response.read()
          filename = url.split('/')[-1]
          with open(filename, 'wb') as f:
            f.write(image_data)


async def main():
  urls = [
      "https://dota2.ru//img/esport/player/4572.webp",
       "https://dota2.ru/img/news/t1695730296.webp",
       "https://dota2.ru/img/news/t1695386263.webp",
       "https://cs5.pikabu.ru/post_img/2014/05/12/6/1399881087_856373365.jpg",
       "https://i.ytimg.com/vi/mBHLHnRjHcE/sddefault.jpg"
  ]

  semaphore = asyncio.Semaphore(2)

  tasks = [download_image(url, semaphore) for url in urls]
  await asyncio.gather(*tasks)


asyncio.run(main())