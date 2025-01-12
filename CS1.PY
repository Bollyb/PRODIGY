def Encryption(Plaintext,Shifts):
    Output = ""

    for x in range(len(Output)):
        chracter = [x]

        if chracter == " ":
            output += " "
        elif (chracter.isupper()):
            output += chr((ord(chracter) + Shifts - 65) % 26 + 65)
        else:
            output += chr((ord(chracter) + Shifts - 97) % 26 + 97)

    return Output

def Decryption(Plaintext, Shifts):
    return Encryption(Plaintext, -Shifts)

Plaintext = input("Enter your confidential Message: ")
Shifts = int(input("Enter the shift key in Integer Number: "))


Encrypted_Message = Encryption(Plaintext, Shifts)
Decrypted_Message = Decryption(Plaintext, Shifts)

print("\nEncrypted Plaintext", Encrypted_Message)
print("\nDecrypted Ciphertext", Decrypted_Message)
print("\n\n")
