# Cipher GUI Application

This project is an interactive **Graphical User Interface (GUI)** that allows users to encode and decode messages using several classic cipher techniques. It’s developed in **Python** using the `Tkinter` library for the GUI, and supports multiple cipher algorithms such as Caesar, Vigenere, Substitution, and more.

## Features

- **User-friendly GUI:** An intuitive interface for selecting and interacting with various cipher methods.
- **Classic Cipher Algorithms:** Supports multiple ciphers including:
  - Caesar Cipher
  - Vigenere Cipher
  - Substitution Cipher
  - Affine Cipher
  - Transposition Cipher
  - Morse Code
- **Dynamic Inputs:** The GUI adapts to the specific cipher chosen, prompting for appropriate keys or shifts.
- **Encryption & Decryption:** Easily toggle between encryption and decryption with a simple button click.

## Prerequisites

Ensure you have the following installed before running the application:

- Python 3.x
- The following Python libraries:
  - `tkinter`
  - `PIL (Python Imaging Library)`
  - `os` and `sys` (for handling paths)

You can install any missing libraries using `pip`:

```bash
  pip install tkinter Pillow
```
## How to Run
 - Clone this repository or download the code.

 - Ensure the images folder (containing the necessary background and button images) is in the same directory as the script.

## Run the Python script:

```bash
  python cipher_gui.py
```
 - Select the cipher you wish to use, enter your message, and the corresponding key or shift (if applicable).
 - Press Encrypt or Decrypt to see the results.

## File Structure:
.
├── cipher_gui.py               # Main script for running the GUI application
├── ciphers.py                  # Script containing implementations of cipher algorithms
├── images                      # Folder containing images for the GUI background and buttons
│   ├── CIpherCat.png
│   ├── CIpherCat1.png
│   └── back_button_image.png
│   └── exit.png
└── README.md                   # Project documentation


## Supported Ciphers
 - Caesar Cipher: Shift-based cipher where letters are shifted by a certain number.
 - Vigenere Cipher: Uses a keyword to shift each letter based on its corresponding character.
 - Substitution Cipher: Replaces each letter with another letter in the alphabet.
 - Affine Cipher: Combines multiplication and addition operations for encoding.
 - Transposition Cipher: Rearranges the characters in a message based on a key.
 - Morse Code: Converts each letter into Morse code for encryption.


## Screenshots
 - Not yet included.



## Future Improvements
 - Add support for additional ciphers such as Playfair and Hill ciphers.
 - Implement a save feature for encrypted and decrypted messages.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or contributions, feel free to reach out:

 - Email: mahrufhossain97@gmail.com
 - GitHub: [MahrufHossain[(https://github.com/MahrufHossain)
