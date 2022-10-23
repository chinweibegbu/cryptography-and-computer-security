import sys
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from numpy import byte

def prepFile():
    pass

def encrypt_ecb():
    key = os.urandom(16)
    plaintext_file_name = sys.argv[1]
    plaintext_file = open(plaintext_file_name, mode='rb')
    plaintext_data = bytearray()
    for line in plaintext_file:
        plaintext_data += line

    # Display plaintext and number of blocks
    # print(lines)
    bit_length = plaintext_data[0].bit_length()
    total_bit_length = len(plaintext_data)*8
    num_blocks = total_bit_length/128

    print("\nBit length:", str(bit_length))
    print("Total bit length:", str(total_bit_length))
    print("Number of blocks:", str(num_blocks), "\n")

    plaintext_file.close()

    # Pad plaintext if necessary
    if(total_bit_length%128 != 0):
        padder = padding.PKCS7(128).padder()
        padded_lines = padder.update(plaintext_data) + padder.finalize()

        # Print unpadded and padded versions
        new_total_bit_length = len(padded_lines)*8
        new_num_blocks = new_total_bit_length/128

        print("New total bit length:", str(new_total_bit_length))
        print("New number of blocks:", str(new_num_blocks), "\n")

        # Update the lines variable
        lines = padded_lines
        total_bit_length = new_total_bit_length
        num_blocks = new_num_blocks

    else:
        print("Sufficient bits originally available")


    # Create array to contain cipher text in binary
    ciphertext_data = bytearray()

    # Encrypt the file
    for i in range(0, int(num_blocks)):
        first_byte_index = i*16
        last_byte_index = i*16 + 16
        
        current_block = lines[first_byte_index:last_byte_index]
        AES_algorithm = algorithms.AES128(key)
        cipher = Cipher(AES_algorithm, mode=modes.ECB())
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(current_block)
        # print(cipher_text)
        ciphertext_data += cipher_text
    
    ciphertext_file = open('ecb_encrypted', 'xb')
    ciphertext_file.write(ciphertext_data)
    ciphertext_file.close()

    return 0





def encrypt_cbc():
        # Create key and initialisation vector of size 128 bits
    key = os.urandom(16)
    iv = os.urandom(16)

    # Read the content of the plaintext file
    plaintext_file_name = sys.argv[1]
    plaintext_file = open(plaintext_file_name, mode='rb')
    plaintext_data = bytearray()
    for line in plaintext_file:
        plaintext_data += line

    # Display plaintext and number of blocks
    # print(lines)
    bit_length = plaintext_data[0].bit_length()
    total_bit_length = len(plaintext_data)*8
    num_blocks = total_bit_length/128

    print("\nBit length:", str(bit_length))
    print("Total bit length:", str(total_bit_length))
    print("Number of blocks:", str(num_blocks), "\n")

    plaintext_file.close()

    # Pad plaintext if necessary
    if(total_bit_length%128 != 0):
        padder = padding.PKCS7(128).padder()
        padded_lines = padder.update(plaintext_data) + padder.finalize()

        # Print unpadded and padded versions
        new_total_bit_length = len(padded_lines)*8
        new_num_blocks = new_total_bit_length/128

        print("New total bit length:", str(new_total_bit_length))
        print("New number of blocks:", str(new_num_blocks), "\n")

        # Update the lines variable
        lines = padded_lines
        total_bit_length = new_total_bit_length
        num_blocks = new_num_blocks

    else:
        print("Sufficient bits originally available")


    # Create array to contain cipher text in binary
    ciphertext_data = bytearray()

    # Encrypt the file
    for i in range(0, int(num_blocks)):
        first_byte_index = i*16
        last_byte_index = i*16 + 16
        
        current_block = lines[first_byte_index:last_byte_index]
        AES_algorithm = algorithms.AES128(key)
        cipher = Cipher(AES_algorithm, mode=modes.CBC(iv))
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(current_block)
        # print(cipher_text)
        ciphertext_data += cipher_text

    # Create output file
    ciphertext_file = open('cbc_encrypted', 'xb')
    ciphertext_file.write(ciphertext_data)
    ciphertext_file.close()


    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext_data)

    # plaintext_file = open('plaintext', 'xb')
    # plaintext_file.write(decrypted_data)
    # plaintext_file.close()
    return 1

encrypt_ecb()


