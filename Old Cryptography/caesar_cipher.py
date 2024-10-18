from collections import Counter


class CaesarCipher:
    def __init__(self, shift, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        """
        Initializes the CaesarCipher with a given shift value and alphabet.
        """
        self.shift = shift % len(alphabet)  # Mod the shift with alphabet length
        self.alphabet = alphabet
        self.alphabet_length = len(alphabet)
    
    def encrypt(self, plaintext):
        """
        Encrypts the given plaintext using Caesar Cipher technique.
        
        :param plaintext: The text to be encrypted
        :return: The encrypted ciphertext
        """
        return self._transform_text(plaintext, self.shift)
    
    def decrypt(self, ciphertext):
        """
        Decrypts the given ciphertext using Caesar Cipher technique.
        """
        return self._transform_text(ciphertext, -self.shift)
    
    def brute_force_decrypt(self, ciphertext):
        """
        Attempts to decrypt the ciphertext by trying all possible shifts.
        """
        possibilities = {}
        for shift_value in range(self.alphabet_length):
            possible_plaintext = self._transform_text(ciphertext, -shift_value)
            possibilities[shift_value] = possible_plaintext
        return possibilities
    
    def frequency_analysis(self, ciphertext):
        """
        Frequency analysis of the ciphertext, which helps in identifying
        the most common letters and potentially assisting in decryption.
        """
        # Normalize the ciphertext by removing non-alphabetic characters
        normalized_text = [char.upper() for char in ciphertext if char.upper() in self.alphabet]
        frequency = Counter(normalized_text)
        return dict(frequency)

    def _transform_text(self, text, shift):
        """
        Helper method to shift the text by a given amount. Works for both encryption
        and decryption based on the value of shift.
        """
        transformed_text = []
        
        for char in text:
            if char.isalpha():
                # Determine if the character is uppercase or lowercase
                base = ord('A') if char.isupper() else ord('a')
                
                # Shift character within the alphabet and wrap around using mod 26
                shifted_char = chr((ord(char) - base + shift) % self.alphabet_length + base)
                transformed_text.append(shifted_char)
            else:
                # Non-alphabetic characters are not encrypted/decrypted
                transformed_text.append(char)
        
        return ''.join(transformed_text)
    
    def set_shift(self, new_shift):
        """
        Updates the shift value dynamically.
        """
        self.shift = new_shift % self.alphabet_length  # Ensure shift is always within valid range

# Example usage:
if __name__ == "__main__":
    cipher = CaesarCipher(shift=3)
    
    plaintext = "Hello, World!"
    ciphertext = cipher.encrypt(plaintext)
    
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    
    decrypted_text = cipher.decrypt(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")

    brute_force_attempts = cipher.brute_force_decrypt(ciphertext)
    print("\nBrute-force decryption attempts:")
    for shift, result in brute_force_attempts.items():
        print(f"Shift {shift}: {result}")

    freq_analysis = cipher.frequency_analysis(ciphertext)
    print("\nFrequency Analysis of Ciphertext:")
    print(freq_analysis)