import numpy as np
from numpy.linalg import LinAlgError


class HillCipher:
    def __init__(self, key_matrix, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        """
        Initialize the HillCipher with a square key matrix.
        The matrix must be invertible modulo 26.
        """
        self.key_matrix = np.array(key_matrix)
        self.mod = len(alphabet)

        if not self._is_invertible():
            raise ValueError("Key matrix is not invertible mod 26.")
        
    def _is_invertible(self):
        """
        Check if the key matrix is invertible under mod 26.
        """
        determinant = int(round(np.linalg.det(self.key_matrix))) % self.mod
        return np.gcd(determinant, self.mod) == 1

    def _char_to_int(self, char):
        """
        Convert a character to its integer representation (A=0, B=1, ..., Z=25).
        """
        return ord(char.upper()) - ord('A')

    def _int_to_char(self, num):
        """
        Convert an integer back to its character representation.
        """
        return chr((num % self.mod) + ord('A'))

    def _process_text(self, text, size):
        """
        Prepare the text: remove non-letters, pad to fit block size, and convert to integers.
        """
        text = ''.join([char.upper() for char in text if char.isalpha()])
        padding_length = (size - len(text) % size) % size
        text += 'X' * padding_length  # Pad with 'X' if necessary
        return [self._char_to_int(char) for char in text]

    def encrypt(self, plaintext):
        """
        Encrypt and split plaintext into blocks of the same size as the key matrix.
        """
        size = self.key_matrix.shape[0]
        plaintext_vector = self._process_text(plaintext, size)
        ciphertext = []

        # Encrypt each block
        for i in range(0, len(plaintext_vector), size):
            block = plaintext_vector[i:i+size]
            encrypted_block = np.dot(self.key_matrix, block) % self.mod
            ciphertext.extend(encrypted_block)

        return ''.join([self._int_to_char(num) for num in ciphertext])

    def decrypt(self, ciphertext):
        """
        Decrypt using the inverse of the key matrix for decryption.
        """
        size = self.key_matrix.shape[0]
        ciphertext_vector = [self._char_to_int(char) for char in ciphertext]
        inverse_key_matrix = np.linalg.inv(self.key_matrix).astype(int) % self.mod

        plaintext = []

        # Decrypt each block
        for i in range(0, len(ciphertext_vector), size):
            block = ciphertext_vector[i:i+size]
            decrypted_block = np.dot(inverse_key_matrix, block) % self.mod
            plaintext.extend(decrypted_block)

        return ''.join([self._int_to_char(num) for num in plaintext])

# Example usage
if __name__ == "__main__":
    # Key matrix (should be invertible in mod 26)
    key_matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    
    cipher = HillCipher(key_matrix)
    plaintext = "HELLOFROMTHEHILL"
    encrypted_text = cipher.encrypt(plaintext)
    decrypted_text = cipher.decrypt(encrypted_text)

    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
