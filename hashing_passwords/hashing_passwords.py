import random;
from Crypto.Hash import SHA256

def task1a(input):
    # Converting input to byteArray
    byteArrayInput = str(input).encode("utf-8")

    # Creating SHA256 objects
    SHA_Input = SHA256.new()

    # Creating output of SHA encryption
    SHA_Output = SHA_Input.update(byteArrayInput)

    # Printing the hexdigest of encryption to the screen
    print("Output of the SHA256 Encryption is", SHA_Input.hexdigest())
    return SHA_Input

def hamming_distance(x,y):
    return bin(x ^ y).count('1')

def task1bc(inputOne,inputTwo):
    # Calcluating the hamming_distance of the two inputs
    hamDistance = hamming_distance(inputOne,inputTwo) 

    # Printing the hamDistance for debugging purposes 
    print("The hamming distance between the two inputs is", hamDistance)

    if hamDistance == 1:
        # Hashing the inputs several times
        hashOne = hash(hash(hash(inputOne)))
        hashTwo = hash(hash(hash(inputTwo)))

        # Taking the first 8 bits of the SHA Output
        byteArrayOne = bytearray(hashOne.digest())
        byteArrayTwo = bytearray(hashTwo.digest())

        truncatedOne = byteArrayOne[:9]
        truncatedTwo = byteArrayTwo[:9]

    else:
        print("Invalid input. Hamming_distance != 1. Hamming_distance == 1 needed")

    