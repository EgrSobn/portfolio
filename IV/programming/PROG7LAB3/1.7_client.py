import aiohttp
import asyncio

async def send_message(session, message):
    async with session.post('https://localhost:8080', data=message) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        try:
            while True:
                message = input("Enter a message to send to the server (type 'exit' to quit): ")
                if message.lower() == 'exit':
                    break

                response = await send_message(session, message)
                print(f"Received from server: {response}")

        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    asyncio.run(main())