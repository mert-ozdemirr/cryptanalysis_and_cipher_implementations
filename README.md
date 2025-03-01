# Cryptanalysis and Cipher Implementation: Caesar, Affine, and Monoalphabetic Ciphers

This project focuses on the "raw" implementation and cryptanalysis of classical encryption techniques, including the Caesar Cipher, Affine Cipher, and Monoalphabetic Cipher. It consists of two Python scripts:

ciphers.py: Implements encryption and decryption functions for the three ciphers, allowing users to encrypt/decrypt messages via command-line arguments.
break.py: Performs cryptanalysis to break the ciphers using techniques such as brute force, frequency analysis, and dictionary-based attacks to recover plaintext from ciphertext.

## Key Features:
1. Cipher Implementation – Encryption and decryption functions for:
  Caesar Cipher (Shift-based substitution)
  Affine Cipher (Multiplicative and additive transformation)
  Monoalphabetic Cipher (Key-based letter substitution)
2. Cryptanalysis Techniques – Automated decryption without knowing the key:
  Brute force attacks for the Caesar Cipher and Affine Cipher
  Frequency analysis /Dictionary-based attacks for the Monoalphabetic Cipher
3. Command-Line Interface (CLI) – Users can specify cipher type, mode (encryption/decryption), and parameters through command-line arguments.

## Usage Examples:

Encrypt a message using the Caesar Cipher with a shift of 3:
```sh
python ciphers.py caesar input.txt e -s 3
```

Encrypt a message using the Affine Cipher with keys a=5, b=8:
```sh
python ciphers.py affine input.txt e -a 5 -b 8
```

Encrypt a message using a Monoalphabetic Cipher with a custom key:
```sh
python ciphers.py mono input.txt e -k "QWERTYUIOPASDFGHJKLZXCVBNM"
```

Decrypt a Caesar Cipher message (Shift: 3):
```sh
python ciphers.py caesar input.txt d -s 3
```

Decrypt an Affine Cipher message (Keys: a=5, b=8):
```sh
ppython ciphers.py affine input.txt d -a 5 -b 8
```

Decrypt a Monoalphabetic Cipher message using a known key:
```sh
python ciphers.py mono input.txt d -k "QWERTYUIOPASDFGHJKLZXCVBNM"
```

Break a Caesar Cipher-encrypted message:
```sh
python break.py caesar ciphertext.txt
```

Break an Affine Cipher-encrypted message:
```sh
python break.py affine ciphertext.txt
```

Break a Monoalphabetic Cipher-encrypted message using frequency analysis:
```sh
python break.py mono ciphertext.txt
```

**Note:** You can find test files under test folder.





