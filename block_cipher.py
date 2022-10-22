import sys

def encrypt_ecb():
    pass

def encrypt_cbc():
    pass
 
# Read the content of the plaintext file
plaintext_file_name = sys.argv[1]
plaintext_file = open(plaintext_file_name)
lines = ""
for line in plaintext_file:
    lines += line
plaintext_file.close()

# Create output file
ciphertext_file = open('new-file.txt', 'x')
ciphertext_file.write()
ciphertext_file.close()
