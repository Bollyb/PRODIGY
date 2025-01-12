# PRODIGY


# Task 01
Caesar Cipher Algorithm
Implementation of Caesar Cipher Algorithm Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

# Task 02
Pixel Manipulation
Pixel Manipulation for Image Encryption Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

Here is a simple program of an image encryption tool using pixel manipulation in Python. In this program, basic mathematical operation (XOR) are used to encrypt and decrypt the image. This program uses the Pillow library for image processing. If you haven't installed it yet, you can do so by running "pip install Pillow" on VS Code terminal.

# Task 03
Password Complexity Checker
Password Complexity Checker Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

Here's a simple Python code for a Password Complexity Checker. This code defines a function 'check_password_complexity' that takes a password as input and checks its complexity based on length, uppercase and lowercase letters, digits, and special characters. The 'main' function gets user input for a password and prints the result of the complexity check.

# Task 04
Simple Keylogger

Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. (Note: Ethical considerations and permissions are crucial for projects involving keyloggers.)

Here's a basic keylogger program in Python. This program uses the pynput library to monitor keystrokes and save them to a log file. First, make sure you have the pynput library installed. You can install it using pip.You can do this by running the following command in your terminal of VS Code:

'pip install pynput'

After installing the library, you can run the code. It will start recording your keystrokes and saving them to a file named 'keylog.txt' in the same directory as your Python script.

This program first defines the on_key_press function, which is called whenever a key is pressed. The function gets the current timestamp and writes it to a log file along with the key that was pressed. The main function prints a message to the console indicating that the user can stop logging by pressing Ctrl+C. It then creates a listener using the keyboard.Listener class and passes the on_key_press function as the on_press parameter. This causes the on_key_press function to be called whenever a key is pressed. Finally, the listener is started using the join method.

Note that this program logs all keystrokes, including special keys like Ctrl, Alt, and Shift. It also logs keys that are pressed while the keylogger is running, so it may log unexpected keys if the user interacts with the console while the keylogger is running.

Additionally, it's important to note that creating and using keyloggers can be illegal in some jurisdictions and can be considered a violation of privacy. This code is intended for educational purposes only.

# Task 05
Network Packet Analyzer

Develop a packet sniffer tool that captures and analyzes network packets. Display relevant information such as source and destination IP addresses, protocols, and payload data. Ensure the ethical use of the tool for educational purposes.

Here is a simple packet sniffer tool in Python using the Scapy library. This tool captures network packets and displays relevant information like source and destination IP addresses, protocols, and payload data.

To use this tool, you need to install the Scapy library. You can install it using pip. You can do this by running the following command in your terminal of VS Code:

'pip install scapy'

Please note that this tool is for educational purposes only. Unauthorized packet sniffing or network analysis can be illegal and unethical. Always ensure you have the necessary permissions and authorizations before using such tools.

Also, this tool captures all IPv4 packets. If you want to capture specific types of packets, you can modify the filter parameter in the sniff function. For example, if you want to capture only TCP packets, you can use the filter "tcp". For more information on packet filters, you can refer to the Scapy documentation.

https://scapy.readthedocs.io/en/latest/
