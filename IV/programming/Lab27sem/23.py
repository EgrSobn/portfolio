# import asyncio
# import requests

# MAX_CONCURRENT_DOWNLOADS = 3  # Максимальное количество одновременно загружаемых изображений
# semaphore = asyncio.Semaphore(MAX_CONCURRENT_DOWNLOADS)

# async def download_image(url):
#     async with semaphore:
#         response = requests.get(url)
#         filename = f"./downloads/image_{hash(url)}.jpg"
#         with open(filename, 'wb') as file:
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     file.write(chunk)

# async def main():
#     # Список URL-адресов изображений для загрузки
#     image_urls = [
#         "https://dota2.ru//img/esport/player/4572.webp",
#         "https://dota2.ru/img/news/t1695730296.webp",
#         "https://dota2.ru/img/news/t1695386263.webp",
#         "https://cs5.pikabu.ru/post_img/2014/05/12/6/1399881087_856373365.jpg",
#         "https://i.ytimg.com/vi/mBHLHnRjHcE/sddefault.jpg"
#     ]

#     tasks = []
#     for url in image_urls:
#         task = asyncio.create_task(download_image(url))
#         tasks.append(task)

#     await asyncio.gather(*tasks)

# asyncio.run(main())

import asyncio
import aiohttp

async def download_image(session, url):
    async with session.get(url) as response:
        filename = f"./downloads/image_{hash(url)}.jpg"
        with open(filename, "wb") as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)
        print(f"Downloaded {filename}")

async def main():
    urls = [
        "https://dota2.ru//img/esport/player/4572.webp",
         "https://dota2.ru/img/news/t1695730296.webp",
         "https://dota2.ru/img/news/t1695386263.webp",
         "https://cs5.pikabu.ru/post_img/2014/05/12/6/1399881087_856373365.jpg",
         "https://i.ytimg.com/vi/mBHLHnRjHcE/sddefault.jpg"
    ]
    semaphore = asyncio.Semaphore(2) # Ограничение на количество одновременных потоков загрузки

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_image_with_semaphore(semaphore, session, url))
            tasks.append(task)

        await asyncio.gather(*tasks)

async def download_image_with_semaphore(semaphore, session, url):
    async with semaphore:
        await download_image(session, url)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())