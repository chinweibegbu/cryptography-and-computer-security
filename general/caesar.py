def caesar_encrypt(text):
    result = ""

    # Go through each character of the text in this for loop
    for i in range(len(text)):

        # Obtain the ASCII value using ord
        char_position = ord(text[i])

        # Substract 97 to have a character from 1 to 26
        char_position = char_position - 97

        # Add 3 to the position, as caesar does
        new_char_position = char_position + 3

        # Make sure that the position does not surpass 26 (we wrap around)
        new_char_position = new_char_position % 26

        # Convert back to ASCII values
        new_char_position = new_char_position + 97

        # Convert ASCII value to character and concatenate it to final result
        result = result + chr(new_char_position)

        print(result)
    return result

def caesar_decrypt(cipher_text):
    result = ""

    # Go through each character of the text in this for loop
    for i in range(len(cipher_text)):

        # Obtain the ASCII value using ord
        char_position = ord(cipher_text[i])

        # Substract 97 to have a character from 1 to 26
        char_position = char_position - 97

        # Substract 3 to the position, to get back original position
        new_char_position = char_position - 3

        # Make sure that the position does not surpass 26 (we wrap around)
        new_char_position = new_char_position % 26

        # Convert back to ASCII values
        new_char_position = new_char_position + 97

        # Convert ASCII value to character and concatenate it to final result
        result = result + chr(new_char_position)

        print(result)
    return result

text = "picoctf"
print(f"Plain Text: {text}")
cipher_text = caesar_encrypt(text)
print(f"Encrypted: {cipher_text}")
print(f"Decrypted: {caesar_decrypt(cipher_text)}")