from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure the image is in RGB mode
        
        # Convert the image to a NumPy array
        img_array = np.array(img)

        # Generate a random key with the same shape as the image
        if key is None:
            key = np.random.randint(0, 256, img_array.shape, dtype=np.uint8)
        elif key.shape != img_array.shape:
            raise ValueError("Key shape must match image shape.")

        # Encrypt each pixel using XOR with the key
        encrypted_array = np.bitwise_xor(img_array, key)

        # Convert the encrypted array back to an image
        encrypted_img = Image.fromarray(encrypted_array)

        # Save the encrypted image
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully.")
        return key
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(encrypted_image_path, key):
    try:
        # Open the encrypted image
        encrypted_img = Image.open(encrypted_image_path)
        encrypted_img = encrypted_img.convert("RGB")  # Ensure it matches RGB mode

        # Convert the encrypted image to a NumPy array
        encrypted_array = np.array(encrypted_img)

        # Ensure key shape matches the encrypted image shape
        if key.shape != encrypted_array.shape:
            raise ValueError("Key shape must match encrypted image shape.")

        # Decrypt each pixel using XOR with the key
        decrypted_array = np.bitwise_xor(encrypted_array, key)

        # Convert the decrypted array back to an image
        decrypted_img = Image.fromarray(decrypted_array)

        # Save the decrypted image
        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully.")
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    print("Image Encryption and Decryption using Pixel Manipulation")
    image_path = input("Enter the path to the image file: ")

    # Check if the file exists
    if not os.path.exists(image_path):
        print("Error: The specified image file does not exist.")
        return

    # Generate a random key
    key = None

    # Encrypt the image
    key = encrypt_image(image_path, key)

    if key is not None:
        # Decrypt the image
        decrypt_image("encrypted_image.png", key)

if __name__ == "__main__":
    main()
