"# keylogger_basic" 

# Keylogger

This Python script implements a keylogger that captures keyboard and mouse events and logs them to a text file. The keylogger is built using asyncio for asynchronous processing and utilizes the pynput library to monitor input devices.

## Installation

1. Make sure you have Python installed on your system. If not, you can download and install it from [Python's official website](https://www.python.org/downloads/).

2. Install the required dependencies using pip:

```bash
pip install pynput
Usage
Clone or download the repository to your local machine.

Navigate to the directory containing the keylogger script (keylogger.py) using the terminal or command prompt.

Run the script by executing the following command:

bash
Copy code
python keylogger.py
The keylogger will start capturing keyboard and mouse events in the background. To stop the keylogger, press Ctrl+C in the terminal or command prompt.
Code Explanation
Keylogger Class
The Keylogger class encapsulates the functionality of the keylogger.
It initializes the log file path, creates the necessary folder structure, and opens a file handle for logging.
create_folder_tree Method
The create_folder_tree method is responsible for creating the folder structure required for logging.
It ensures that the logs and instructions folders are created if they don't already exist.
on_press and on_click Methods
The on_press method is called when a key is pressed, and it logs the pressed key to the log file.
The on_click method is called when a mouse button is clicked, and it logs the mouse click event to the log file.
start_logging Method
The start_logging method starts the asynchronous logging process.
It asynchronously listens for keyboard and mouse events using pynput's Listener objects.
stop_logging Method
The stop_logging method closes the log file handle when logging is stopped.
main Function
The main function creates an instance of the Keylogger class and starts the logging process asynchronously.
Execution
The script is executed using asyncio's run function, which runs the main function asynchronously.
Security Considerations
Use Responsibly: Keyloggers can be misused for unethical purposes. Only use this keylogger on systems and devices where you have explicit permission to monitor activity.
Privacy: Be mindful of user privacy and legal regulations regarding monitoring and logging user activity. Avoid logging sensitive information such as passwords and personal data.