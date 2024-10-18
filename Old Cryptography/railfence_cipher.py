class RailFenceCipher:
    def __init__(self, num_rails):
        """
        Initialize the Rail Fence Cipher with a specified number of rails.
        """
        if num_rails <= 1:
            raise ValueError("Number of rails must be greater than 1")
        self.num_rails = num_rails

    def _create_rails(self, length):
        """
        Create an empty structure for rails.
        """
        return [['\n' for _ in range(length)] for _ in range(self.num_rails)]

    def encrypt(self, plaintext):
        """
        Encrypt the plaintext using the Rail Fence Cipher.
        """
        rails = self._create_rails(len(plaintext))
        row, step = 0, 1

        # Place characters in the rails
        for i, char in enumerate(plaintext):
            rails[row][i] = char
            if row == 0:
                step = 1  # Move down
            elif row == self.num_rails - 1:
                step = -1  # Move up
            row += step

        # Read the rails row by row
        ciphertext = []
        for rail in rails:
            ciphertext.append(''.join([char for char in rail if char != '\n']))
        
        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext using the Rail Fence Cipher.
        """
        rails = self._create_rails(len(ciphertext))
        row, step = 0, 1

        # Mark positions where characters will be placed
        for i in range(len(ciphertext)):
            rails[row][i] = '*'
            if row == 0:
                step = 1
            elif row == self.num_rails - 1:
                step = -1
            row += step

        # Place ciphertext characters in the marked positions
        index = 0
        for r in range(self.num_rails):
            for c in range(len(ciphertext)):
                if rails[r][c] == '*' and index < len(ciphertext):
                    rails[r][c] = ciphertext[index]
                    index += 1

        # Read the characters in a zigzag pattern
        row, step = 0, 1
        plaintext = []
        for i in range(len(ciphertext)):
            plaintext.append(rails[row][i])
            if row == 0:
                step = 1
            elif row == self.num_rails - 1:
                step = -1
            row += step

        return ''.join(plaintext)
    
    def visualize_rails(self, plaintext):
        """
        Visualize how the characters are arranged in the rails.
        """
        plaintext = ''.join(filter(str.isalnum, plaintext))  # Keep only alphanumeric characters
        plaintext = plaintext.upper()  # Handle text in uppercase for simplicity
        rails = self._create_rails(len(plaintext))
        row, step = 0, 1

        # Place characters in the rails
        for i, char in enumerate(plaintext):
            rails[row][i] = char
            if row == 0:
                step = 1
            elif row == self.num_rails - 1:
                step = -1
            row += step

        # Print the visualized rails
        for rail in rails:
            print(''.join(rail))


# Example usage:
if __name__ == "__main__":
    # Create an instance of the RailFenceCipher with 3 rails
    cipher = RailFenceCipher(3)

    # Example encryption and decryption
    plaintext = "HELLOWORLDTOYOU"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print(f"Original: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

    print("\nVisualizing Rails:")
    cipher.visualize_rails(plaintext)
