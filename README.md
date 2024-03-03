# RC4 Encryption and Decryption Tool

## Overview

This project consists of two Python scripts: `RC4.py` and `RC4_attacker.py`. 
The `RC4.py` script implements the RC4 encryption algorithm, while `RC4_attacker.py` 
is used to perform a brute-force attack to decrypt ciphertext encrypted with RC4.

## Requirements

- Python 3.x
- `queue` module
- `threading` module
- `math` module
- `time` module

## Usage

### Encryption (RC4.py)

To encrypt plaintext using RC4, run the `RC4.py` script with Python. The script takes the plaintext 
and encryption key as input and returns the encrypted ciphertext.

check before usage: 
Before running the script, make sure to initialize the `input_bytes` variable with the string you want to encrypt and the `key` variable with the key you want to use.


### Decryption (RC4_attacker.py)

To decrypt ciphertext encrypted with RC4, use the `RC4_attacker.py` script. This script performs 
a brute-force attack to decrypt the ciphertext by trying all possible keys.

Check before usage:
Before running the script, make sure to initialize the `ciphertext` variable in the `main` function with the output generated from `RC4.py`and the key size that used in the `RC4.py`.



## File Descriptions

- `RC4.py`: Contains functions for RC4 encryption.
- `RC4_attacker.py`: Implements a brute-force attack to decrypt RC4-encrypted ciphertext.
- `README.md`: This file, containing information about the project.

## Authors
- Ori Sharaby
- Elroei Avraham


