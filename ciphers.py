class CaesarCipher:
    def __init__(self, message, shift):
        self.message = message
        self.shift = shift

    def encrypt(self):
        encrypted_message = []
        for char in self.message:
            if char.isalpha():
                shift = self.shift % 26
                start = ord("A") if char.isupper() else ord("a")
                encrypted_message.append(chr(start + (ord(char) - start + shift) % 26))
            else:
                encrypted_message.append(char)
        return "".join(encrypted_message)

    def decrypt(self):
        decrypted_message = []
        for char in self.message:
            if char.isalpha():
                shift = self.shift % 26
                start = ord("A") if char.isupper() else ord("a")
                decrypted_message.append(chr(start + (ord(char) - start - shift) % 26))
            else:
                decrypted_message.append(char)
        return "".join(decrypted_message)


class VigenereCipher:
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def _extend_key(self):
        """Extend the key to match the length of the message."""
        key = self.key
        if len(self.key) < len(self.message):
            key = (self.key * (len(self.message) // len(self.key) + 1))[
                : len(self.message)
            ]
        return key

    def encrypt(self):
        key = self._extend_key()
        encrypted_message = []
        for m, k in zip(self.message, key):
            if m.isalpha():
                offset = ord("A") if m.isupper() else ord("a")
                encrypted_char = chr(
                    (ord(m) - offset + ord(k.upper()) - ord("A")) % 26 + offset
                )
                encrypted_message.append(encrypted_char)
            else:
                encrypted_message.append(m)
        return "".join(encrypted_message)

    def decrypt(self):
        key = self._extend_key()
        decrypted_message = []
        for m, k in zip(self.message, key):
            if m.isalpha():
                offset = ord("A") if m.isupper() else ord("a")
                decrypted_char = chr(
                    (ord(m) - offset - (ord(k.upper()) - ord("A")) + 26) % 26 + offset
                )
                decrypted_message.append(decrypted_char)
            else:
                decrypted_message.append(m)
        return "".join(decrypted_message)


class SubstitutionCipher:
    def __init__(self, message, key):
        self.message = message
        self.key = key.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.substitution_dict = dict(zip(self.alphabet, self.key))

    def encrypt(self):
        encrypted_message = []
        for char in self.message:
            if char.isalpha():
                encrypted_message.append(self.substitution_dict.get(char.upper(), char))
            else:
                encrypted_message.append(char)
        return "".join(encrypted_message)

    def decrypt(self):
        reversed_dict = {v: k for k, v in self.substitution_dict.items()}
        decrypted_message = []
        for char in self.message:
            if char.isalpha():
                decrypted_message.append(reversed_dict.get(char.upper(), char))
            else:
                decrypted_message.append(char)
        return "".join(decrypted_message)


class AffineCipher:
    def __init__(self, message, shift):
        self.message = message
        self.shift = shift
        self.a = 5  # Multiplier (must be coprime with 26)
        self.b = shift  # Shift value

    def encrypt(self):
        encrypted_message = []
        for char in self.message:
            if char.isalpha():
                shift = self.shift % 26
                a = self.a % 26
                start = ord("A") if char.isupper() else ord("a")
                encrypted_message.append(
                    chr(start + (a * (ord(char) - start) + shift) % 26)
                )
            else:
                encrypted_message.append(char)
        return "".join(encrypted_message)

    def decrypt(self):
        decrypted_message = []
        a_inv = pow(self.a, -1, 26)  # Modular inverse of a
        shift = self.shift % 26
        for char in self.message:
            if char.isalpha():
                start = ord("A") if char.isupper() else ord("a")
                decrypted_message.append(
                    chr(start + a_inv * ((ord(char) - start - shift + 26) % 26))
                )
            else:
                decrypted_message.append(char)
        return "".join(decrypted_message)


class TranspositionCipher:
    def __init__(self, message, key):
        self.message = message
        self.key = len(key)  # Use the length of the key word as the number of columns

    def encrypt(self):
        # Pad the message to make sure it fits evenly into columns
        padded_length = (len(self.message) + self.key - 1) // self.key * self.key
        padded_message = self.message.ljust(padded_length)
        encrypted_message = [""] * self.key
        for column in range(self.key):
            index = column
            while index < len(padded_message):
                encrypted_message[column] += padded_message[index]
                index += self.key
        return "".join(encrypted_message)

    def decrypt(self):
        num_of_columns = len(self.message) // self.key
        num_of_rows = self.key
        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(self.message)
        decrypted_message = [""] * num_of_columns
        column, row = 0, 0
        for symbol in self.message:
            decrypted_message[column] += symbol
            column += 1
            if (column == num_of_columns) or (
                column == num_of_columns - 1
                and row >= num_of_rows - num_of_shaded_boxes
            ):
                column = 0
                row += 1
        return "".join(decrypted_message)


class AtbashCipher:
    def __init__(self, message):
        self.message = message
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.atbash_dict = dict(zip(self.alphabet, reversed(self.alphabet)))

    def encrypt(self):
        encrypted_message = []
        for char in self.message.upper():
            if char in self.atbash_dict:
                encrypted_message.append(self.atbash_dict[char])
            else:
                encrypted_message.append(char)
        return "".join(encrypted_message)

    def decrypt(self):
        return self.encrypt()  # Atbash cipher is symmetric


class MorseCodeCipher:
    MORSE_CODE_DICT = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": " ",
    }

    @staticmethod
    def encode(message):
        encoded_message = []
        for char in message.upper():
            if char in MorseCodeCipher.MORSE_CODE_DICT:
                encoded_message.append(MorseCodeCipher.MORSE_CODE_DICT[char])
            else:
                encoded_message.append(
                    "?"
                )  # Handle characters not in Morse code dictionary
        return " ".join(encoded_message)

    @staticmethod
    def decode(morse_code):
        reversed_dict = {v: k for k, v in MorseCodeCipher.MORSE_CODE_DICT.items()}
        decoded_message = []
        for code in morse_code.split(" "):
            if code in reversed_dict:
                decoded_message.append(reversed_dict[code])
            else:
                decoded_message.append("?")  # Handle unknown Morse code
        return "".join(decoded_message)
