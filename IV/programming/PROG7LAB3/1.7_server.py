import asyncio
from aiohttp import web

async def handle(request):
    data = await request.text()
    print(f"Received from client: {data}")
    return web.Response(text=data)

async def main():
    app = web.Application()
    app.router.add_post('/', handle)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, 'localhost', 8080, ssl_context=None)
    await site.start()

    print("Server started on https://localhost:8080")

    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        pass
    finally:
        await runner.cleanup()

if __name__ == '__main__':
    asyncio.run(main())

