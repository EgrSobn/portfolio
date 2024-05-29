import asyncio

def write_data():
    try:
        with open("data.txt", "w") as file:
            file.write("Hello, World!")
        return "Data written successfully"
    except Exception as e:
        return str(e)

def read_data():
    try:
        with open("data.txt", "r") as file:
            content = file.read()
        return content
    except Exception as e:
        return str(e)

async def main():
    write_result = await loop.run_in_executor(None, write_data)
    print(write_result)

    read_result = await loop.run_in_executor(None, read_data)
    print("File content: ", read_result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()