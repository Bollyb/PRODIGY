'''
Task-01
Implement Ceasar Cipher
Create a python program that can encrypt and decrypt text using the Ceasar Cipher algorithm. 
Allow users to input a message and a shift value to perform encryption and decryption.

'''

#Encryption Function
def Encryption(Plaintext,Shifts):
    Output = ""
# Perform the iteratation on the given message
    for x in range(len(Output)):
        chracter = [x]

# Check when there is space in the message, and then add it.
        if chracter == " ":
            output += " "
        elif (chracter.isupper()):
            output += chr((ord(chracter) + Shifts - 65) % 26 + 65)
        else:
            output += chr((ord(chracter) + Shifts - 97) % 26 + 97)

    return Output

#Decryption Function
def Decryption(Plaintext, Shifts):
    return Encryption(Plaintext, -Shifts)

Plaintext = input("Enter your confidential Message: ")
Shifts = int(input("Enter the shift key in Integer Number: "))

#main function
Encrypted_Message = Encryption(Plaintext, Shifts)
Decrypted_Message = Decryption(Plaintext, Shifts)

print("\nEncrypted Plaintext", Encrypted_Message)
print("\nDecrypted Ciphertext", Decrypted_Message)
print("\n\n")
