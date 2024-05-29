import asyncio
import datetime
from termcolor import colored
from pynput import keyboard

async def show_time():
    while True:
        now = datetime.datetime.now()
        date_string = now.strftime("%Y-%m-%d")
        time_string = now.strftime("%H:%M:%S")
        colored_date = colored(date_string, "green")
        colored_time = colored(time_string, "yellow")
        print(f"\r{colored_date} {colored_time}", end="")
        await asyncio.sleep(1)

async def exit_on_escape():
    def on_press(key):
        if key == keyboard.Key.esc:
            loop.stop()
    with keyboard.Listener(on_press=on_press) as listener:
        loop.run_forever()

loop = asyncio.get_event_loop()
tasks = asyncio.gather(show_time(), exit_on_escape())
loop.run_until_complete(tasks)