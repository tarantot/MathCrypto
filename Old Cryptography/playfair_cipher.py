import string

class PlayfairCipher:
    def __init__(self, key):
        """
        Initialize the Playfair Cipher with a keyword.
        The key is used to generate a 5x5 cipher matrix.
        """
        self.key = key.upper().replace("J", "I")  # Convert key to uppercase and replace 'J' with 'I'
        self.matrix = self._generate_cipher_matrix(self.key)

    def _generate_cipher_matrix(self, key):
        """
        Generate a 5x5 matrix for the Playfair cipher based on the provided key.
        """
        key = "".join(sorted(set(key), key=key.index))  # Remove duplicates, preserving order
        alphabet = string.ascii_uppercase.replace('J', '')
        combined = key + ''.join([c for c in alphabet if c not in key])

        matrix = []
        for i in range(5):
            row = list(combined[i * 5:(i + 1) * 5])
            matrix.append(row)
        return matrix

    def _find_position(self, letter):
        """
        Find the row and column of a letter in the cipher matrix.
        """
        for row_idx, row in enumerate(self.matrix):
            if letter in row:
                return row_idx, row.index(letter)
        return None

    def _preprocess_text(self, text):
        """
        Preprocess text for encryption or decryption, 
        handling issues like repeating letters in digraphs.
        """
        text = text.upper().replace('J', 'I')  # Replace J with I
        digraphs = []
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i + 1] if (i + 1) < len(text) else 'X'
            if a == b:
                digraphs.append(a + 'X')
                i += 1
            else:
                digraphs.append(a + b)
                i += 2
        if len(digraphs[-1]) == 1:
            digraphs[-1] += 'X'  # Pad the last pair if necessary
        return digraphs

    def encrypt(self, plaintext):
        """
        Encrypt the plaintext using the Playfair cipher.
        """
        digraphs = self._preprocess_text(plaintext)
        ciphertext = []

        for digraph in digraphs:
            row1, col1 = self._find_position(digraph[0])
            row2, col2 = self._find_position(digraph[1])

            if row1 == row2:
                ciphertext.append(self.matrix[row1][(col1 + 1) % 5])
                ciphertext.append(self.matrix[row2][(col2 + 1) % 5])
            elif col1 == col2:
                ciphertext.append(self.matrix[(row1 + 1) % 5][col1])
                ciphertext.append(self.matrix[(row2 + 1) % 5][col2])
            else:
                ciphertext.append(self.matrix[row1][col2])
                ciphertext.append(self.matrix[row2][col1])

        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext using the Playfair cipher.
        """
        digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        plaintext = []

        for digraph in digraphs:
            row1, col1 = self._find_position(digraph[0])
            row2, col2 = self._find_position(digraph[1])

            if row1 == row2:
                plaintext.append(self.matrix[row1][(col1 - 1) % 5])
                plaintext.append(self.matrix[row2][(col2 - 1) % 5])
            elif col1 == col2:
                plaintext.append(self.matrix[(row1 - 1) % 5][col1])
                plaintext.append(self.matrix[(row2 - 1) % 5][col2])
            else:
                plaintext.append(self.matrix[row1][col2])
                plaintext.append(self.matrix[row2][col1])

        return ''.join(plaintext)

# Example usage:
if __name__ == "__main__":
    key = "PLAYFAIR"
    cipher = PlayfairCipher(key)

    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print(f"Original: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
