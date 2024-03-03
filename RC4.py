def initialize_sbox(sbox, key, key_length):
    # Initialize the S-box with values from 0 to 255
    for i in range(256):
        sbox[i] = i

    # Use the key to shuffle the S-box values
    j = 0
    for i in range(256):
        j = (j + sbox[i] + key[i % key_length]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        
   
def rc4_encrypt(input_bytes, key):
    # Initialize the S-box using the provided key
    sbox = list(range(256))
    key_length = len(key)
    initialize_sbox(sbox, key, key_length)

    i = 0
    j = 0
    output = bytearray()

    # Generate the keystream and perform XOR with the input to get the ciphertext
    for byte in input_bytes:
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
       
        t = (sbox[i] + sbox[j]) % 256
        output.append(byte ^ sbox[t])

    return output


input_bytes = b'This is a sample plaintext For RC4 hope that you could encrypt me'  # Example input
# key = b'ORIS'  # Example key
key = b'OR'  # Example key

encrypted_data = rc4_encrypt(input_bytes, key)

print(encrypted_data)
print(1)
print(encrypted_data.hex())
print(1)