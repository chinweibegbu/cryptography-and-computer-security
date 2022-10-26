from pydoc import plain
import sys, os
import urllib.parse as url_encode
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

 # Create key and initialisation vector of size 128 bits
key = os.urandom(16)
iv = os.urandom(16)

# AES Decryptor and Encryptor
AES_algorithm = algorithms.AES128(key)
cipher = Cipher(AES_algorithm, mode=modes.CBC(iv))
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()

def encrypt_ecb():
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
        if i > 0:
            iv = cipher_text
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

# encrypt_ecb()


def submit():

    # Getting the user input and making it an array
    userInput = input("Please give me a string: \n")
    letters = [*userInput]

    # Encoding each ';' and '=' in the userInput
    for i in range(len(letters)):
        if letters[i] == ';' or letters[i] == '=':
            urlEncoded = url_encode.quote(letters[i])
            letters[i] = urlEncoded

    # Putting the characters back together into one variable
    encodedUserInput = ""
    for i in letters:
        encodedUserInput += i

    # Adding the appropriate prepend and appent to the encoded userInput
    prepend = "userid=456;userdata="
    append = ";session-id=31337" 
    full_text = prepend + encodedUserInput  + append;

    # Printing the output of the full_text
    print("Full configured text: ", full_text, "\n") 

    # Converting full_text to bytes
    textInBytes = str.encode(full_text)

    # Padding the full_text
    padder = padding.PKCS7(128).padder()
    paddedText = padder.update(textInBytes) + padder.finalize()
    
    # Printing the padded text
    print("Padded text: ", paddedText, "\n")

    # Encrypting padded text to AES-128-CBC
    cipher_text = encryptor.update(paddedText) + encryptor.finalize()

    # Printing the cipher_text in bytes...
    print("AES Encrypted cipher text is: \n", cipher_text, "\n" )

    return(cipher_text)

def verify(cipher_text):
    plain_text = decryptor.update(cipher_text) + decryptor.finalize()
    plain_text = plain_text.decode("utf-8") 
    print("The plain text is: \n", plain_text)
    index = plain_text.find(";admin=true;")
    if index > -1:
        return True
    else:
        return False
     
ct = submit()
result = verify(ct)
print("\nOutcome:", result)