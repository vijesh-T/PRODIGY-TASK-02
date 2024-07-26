from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Encrypt the image by adding the key to each pixel
    encrypted_array = (img_array + key) % 256
    
    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Decrypt the image by subtracting the key from each pixel
    decrypted_array = (img_array - key) % 256
    
    # Convert back to image and save
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)

# Example usage
encrypt_image('input_image.png', 'encrypted_image.png', key=123)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key=123)
