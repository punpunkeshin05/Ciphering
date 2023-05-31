# Caesar and Vigenère Cipher

This repository contains Python code for two classic encryption algorithms: the Caesar cipher and the Vigenère cipher. These ciphers are historically significant and have been widely used for centuries to encrypt and decrypt secret messages.

## Caesar Cipher

The Caesar cipher is a simple substitution cipher that shifts each letter in the plaintext by a fixed number of positions in the alphabet. In this code, the user can specify the shift value (also known as the key) to encode or decode a message. The Caesar cipher operates on individual letters, preserving the case and other non-alphabetic characters.

## Vigenère Cipher

The Vigenère cipher is a more complex polyalphabetic substitution cipher that uses a keyword to determine the shifting pattern for each letter in the plaintext. The keyword is repeated until it matches the length of the plaintext. This code allows the user to encode or decode a message using the Vigenère cipher by providing a keyword.

Both ciphers support encoding and decoding functionality. The provided code ensures that the resulting ciphertext can be properly deciphered back to the original plaintext using the same key or keyword.

## Usage

To use the code, follow these steps:

1. Clone or download the repository to your local machine.
2. Open the Python file for the desired cipher (`caesar_cipher.py` or `vigenere_cipher.py`) in your preferred Python development environment.
3. Modify the input variables (such as the message, shift value, or keyword) within the code according to your needs.
4. Run the script to see the encoded or decoded message.

Feel free to explore, experiment, and integrate this code into your own projects or educational exercises related to cryptography or encryption algorithms.




