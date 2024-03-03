# Function to generate README content
def generate_readme():
    readme_content = """# RC4 Encryption and Decryption Tool

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

Example usage: python RC4.py



### Decryption (RC4_attacker.py)

To decrypt ciphertext encrypted with RC4, use the `RC4_attacker.py` script. This script performs 
a brute-force attack to decrypt the ciphertext by trying all possible keys.

Example usage: python RC4_attacker.py


## File Descriptions

- `RC4.py`: Contains functions for RC4 encryption.
- `RC4_attacker.py`: Implements a brute-force attack to decrypt RC4-encrypted ciphertext.
- `README.md`: This file, containing information about the project.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details."""
    
    # Write README content to a file
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

# Call the function to generate README content
generate_readme()
