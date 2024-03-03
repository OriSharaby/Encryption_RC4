import threading
import queue
import math
from ctypes import c_ubyte
import time

KEY_LENGTH = 4
MAX_QUEUE_SIZE = math.pow(2,KEY_LENGTH * 8)
NUM_THREADS = 4  # Example, adjust based on your environment


def initialize_sbox(sbox, key, key_length):
    # Initialize the S-box with values from 0 to 255
    for i in range(256):
        sbox[i] = i

    # Use the key to shuffle the S-box values
    j = 0
    for i in range(256):
        j = (j + sbox[i] + key[i % key_length]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        

# RC4 decryption function
def rc4_decrypt(input_bytes, key):
    bytes_result = bytes.fromhex(input_bytes)
    sbox = list(range(256))
    key_length = len(key)
    initialize_sbox(sbox, key, key_length)
    output = []
    
    # PRGA Phase
    i = j = 0
    for char in bytes_result:
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        output.append(char ^ sbox[(sbox[i] + sbox[j]) % 256])

    return bytes(output)

# Function to convert a long integer to a byte array
def long_to_bytes(num):
    return num.to_bytes(KEY_LENGTH, 'little')

# Thread worker function
def brute_force_thread(queue, ciphertext):
    while True:
        num = queue.get()
        if num == -1:
            break  # Exit condition

        key = num.to_bytes(KEY_LENGTH, 'little')
        decrypted_text = rc4_decrypt(ciphertext, key)

        if all(32 <= c < 127 for c in decrypted_text):
            if (decrypted_text == b"This is a sample plaintext For RC4 hope that you could encrypt me" or decrypted_text.decode() == "This is a sample plaintext For RC4 hope that you could encrypt me"):  # Check if printable
                print(f"Decrypted text with key {key}: {decrypted_text.decode()}")
                end_time = time.time()
                print("Time in seconds:", end_time -start_time)


        queue.task_done()

# Main function to set up threads and process the decryption
def main():
    global start_time
    start_time = time.time()
    print("im starting")
    # Example ciphertext (as bytes for simplicity)
    ciphertext = "31276b406c5c8afaaf1db2f082833c3d470920c7e0100d7431871f30efc9dde4cd2e3c56801991239f8dd5ad1d7392bdfb868a69b2e6745adfad7d0821ff4f5770"  # Example, replace with actual ciphertext
    # ciphertext ="d535dad713cccc977c5775ea2301654d270b9aaee2814627f1c4da117febaa2abd44fcb449f80e4b9ac2a0836ff0473ec0bf17b622fa7d4f1387f8d66759c0997b"
    # Setting up queue
    q = queue.Queue(maxsize=MAX_QUEUE_SIZE)
    print(11)
    # Starting worker threads
    threads = []
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=brute_force_thread, args=(q, ciphertext))
        t.start()
        threads.append(t)
    print(111)
    # Enqueue tasks
    bits = 8 * KEY_LENGTH
    print(KEY_LENGTH)
    limit =int(math.pow(2, bits))
    print(limit)
    counter = 100000000
    count = 150000
    for num in range(limit):
        q.put(num)
        if(count == num):
            print("im working")
        if(num == counter):
            print(counter)
            counter += 100000000
    
    print(1231231)

    # Signal no more tasks
    for _ in range(NUM_THREADS):
        q.put(-1)
    print(123412314)

    # Wait for all tasks to be completed
    q.join()
    print(12345123145)

    # Wait for all threads to finish
    for t in threads:
        t.join()
    print(123456123456)

if __name__ == "__main__":
    main()