class VigenereCipher:
    def __init__(self, key, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        """
        Initializes the VigenereCipher with the provided key.
        The key is repeated to match the length of the plaintext during encryption or decryption.
        """
        self.key = ''.join([char for char in key.upper() if char.isalpha()])
        self.alphabet = alphabet

    def _format_key(self, text):
        """
        Formats the key to match the length of the text by repeating or truncating.
        """
        key = self.key
        if len(key) < len(text):
            key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
        return key

    def _shift_character(self, char, shift, encrypt=True):
        """
        Shifts a character by the given amount. If encrypt is True, it shifts forward;
        if False, it shifts backward (for decryption).
        """
        base = ord('A')
        char_value = ord(char) - base
        if encrypt:
            return chr((char_value + shift) % len(self.alphabet) + base)
        else:
            return chr((char_value - shift) % len(self.alphabet) + base)

    def encrypt(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere Cipher and the provided key.
        """
        plaintext = plaintext.upper().replace(" ", "")  # Simplify the text by removing spaces
        key = self._format_key(plaintext)
        ciphertext = []
        key_index = 0

        for char in plaintext:
            if char.isalpha():
                shift = ord(key[key_index]) - ord('A')
                encrypted_char = self._shift_character(char, shift, encrypt=True)
                key_index += 1
            else:
                encrypted_char = char
            
            ciphertext.append(encrypted_char)

        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        """
        Decrypts the ciphertext using the Vigenere Cipher and the provided key.
        """
        ciphertext = ciphertext.upper()
        key = self._format_key(ciphertext)
        plaintext = []

        for char in ciphertext:
            if char.isalpha():
                shift = ord(key[key_index]) - ord('A')
                decrypted_char = self._shift_character(char, shift, encrypt=False)
                key_index += 1
            else:
                decrypted_char = char
            
            plaintext.append(decrypted_char)

        return ''.join(plaintext)

# Example usage:
if __name__ == "__main__":
    key = "KEYWORD"
    vigenere = VigenereCipher(key)

    plaintext = "HELLO VIGENERE"
    encrypted = vigenere.encrypt(plaintext)
    decrypted = vigenere.decrypt(encrypted)

    print(f"Original Text: {plaintext}")
    print(f"Encrypted Text: {encrypted}")
    print(f"Decrypted Text: {decrypted}")
