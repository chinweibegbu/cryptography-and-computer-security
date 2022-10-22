import sys
import os
from cryptography.hazmat.primitives import padding
# import cryptography

def encrypt_ecb():
    pass

def encrypt_cbc():
    pass

# Create key and initialisation vector of size 128 bits
key = os.urandom(16)
iv = os.urandom(16)

# Read the content of the plaintext file
plaintext_file_name = sys.argv[1]
plaintext_file = open(plaintext_file_name, mode='rb')
lines = bytearray()
padded_lined = bytearray()
for line in plaintext_file:
    lines += line

# Display plaintext and number of blocks
# print(lines)
bit_length = lines[0].bit_length()
total_bit_length = len(lines)*8
num_blocks = total_bit_length/128

print("\nBit length:", str(bit_length))
print("Total bit length:", str(total_bit_length))
print("Number of blocks:", str(num_blocks), "\n")

plaintext_file.close()

# Pad plaintext if necessary
if(total_bit_length%128 != 0):
    padder = padding.PKCS7(128).padder()
    padded_lines = padder.update(lines) + padder.finalize()

    # Print unpadded and padded versions
    new_total_bit_length = len(padded_lines)*8
    new_num_blocks = new_total_bit_length/128

    print("New total bit length:", str(new_total_bit_length))
    print("New number of blocks:", str(new_num_blocks), "\n")

    # Update the lines variable
    lines = padded_lines

else:
    print("Sufficient bits originally available")



# Create output file
# ciphertext_file = open('new-file', 'xb')
# ciphertext_file.write()
# ciphertext_file.close()
