import asyncio
import datetime
from termcolor import colored
from pynput import keyboard

async def print_time():
    while True:
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(colored(f"\r{date_time}", "green"), end="")
        await asyncio.sleep(1)

async def main():
    try:
        await print_time()
    except asyncio.CancelledError:
        pass

def on_esc_press(key):
    if key == keyboard.Key.esc:
        asyncio.get_running_loop().stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        listener = keyboard.Listener(on_press=on_esc_press)
        listener.start()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        listener.stop()
        listener.join()
        loop.close()
