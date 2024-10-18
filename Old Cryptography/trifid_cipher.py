import random
import hashlib
import string

class TrifidCipher:
    def __init__(self, key_square=None, alphabet=None):
        """
        Initialize the Trifid Cipher with a given key square (3x3x3).
        The key_square is a 3D array of the alphabet typically arranged in a random order.
        """
        if alphabet is None:
            self.alphabet = string.ascii_lowercase + string.digits + " .,!"
        else:
            self.alphabet = alphabet
        
        self.key_square = key_square if key_square else self._generate_key_square()
        self.alphabet_map = self._create_alphabet_map()

    def _generate_key_square(self):
        """
        Generate a random 3x3x3 key square from the alphabet.
        """
        shuffled_alphabet = random.sample(self.alphabet, len(self.alphabet))
        key_square = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]

        idx = 0
        for z in range(3):
            for y in range(3):
                for x in range(3):
                    if idx < len(shuffled_alphabet):
                        key_square[z][y][x] = shuffled_alphabet[idx]
                        idx += 1
        return key_square
    
    def _create_alphabet_map(self):
        """
        Create a mapping of each letter to its 3D coordinates in the key square.
        Returns a dictionary where each letter maps to its (x, y, z) position.
        """
        alphabet_map = {}
        for z, plane in enumerate(self.key_square):
            for y, row in enumerate(plane):
                for x, char in enumerate(row):
                    alphabet_map[char] = (x + 1, y + 1, z + 1)
        return alphabet_map

    def encrypt(self, plaintext, period=5):
        """
        Encrypt the given plaintext using the Trifid Cipher with a specified period 
        which determines how many characters are encrypted in a single batch.
        """
        plaintext = plaintext.lower().replace(" ", "")
        numeric_coords = []

        # Convert plaintext into coordinates
        for char in plaintext:
            if char in self.alphabet_map:
                numeric_coords.extend(self.alphabet_map[char])

        # Split the numeric coordinates into three groups (x, y, z)
        x_coords = []
        y_coords = []
        z_coords = []
        for i in range(0, len(numeric_coords), 3):
            x_coords.append(numeric_coords[i])
            y_coords.append(numeric_coords[i+1])
            z_coords.append(numeric_coords[i+2])

        # Reassemble in blocks of size 'period'
        combined_coords = []
        for i in range(0, len(x_coords), period):
            combined_coords.extend(x_coords[i:i+period])
            combined_coords.extend(y_coords[i:i+period])
            combined_coords.extend(z_coords[i:i+period])

        # Convert combined numeric coordinates back to letters
        ciphertext = ''
        for i in range(0, len(combined_coords), 3):
            x, y, z = combined_coords[i] - 1, combined_coords[i+1] - 1, combined_coords[i+2] - 1
            ciphertext += self.key_square[z][y][x]

        return ciphertext.upper()

    def decrypt(self, ciphertext, period=5):
        """
        Decrypt the given ciphertext with a specified period 
        which determines how many characters are decrypted in a single batch.
        """
        # ciphertext = ciphertext.lower().replace(" ", "")
        ciphertext = self._sanitize_input(ciphertext)
        numeric_coords = []

        # Convert ciphertext into coordinates
        for char in ciphertext:
            if char in self.alphabet_map:
                numeric_coords.extend(self.alphabet_map[char])

        # Split into batches of period * 3
        coords_per_period = period * 3
        combined_coords = []
        for i in range(0, len(numeric_coords), coords_per_period):
            block = numeric_coords[i:i + coords_per_period]
            x_coords = block[:len(block)//3]
            y_coords = block[len(block)//3:2*len(block)//3]
            z_coords = block[2*len(block)//3:]

            # Reassemble the coordinates
            for j in range(len(x_coords)):
                combined_coords.append((x_coords[j], y_coords[j], z_coords[j]))

        # Convert coordinates back to letters
        plaintext = ''
        for x, y, z in combined_coords:
            plaintext += self.key_square[z-1][y-1][x-1]

        return plaintext.lower()
    
    def _sanitize_input(self, input_text):
        """
        Remove characters from the input that are not in the alphabet.
        """
        return ''.join([char.lower() for char in input_text if char.lower() in self.alphabet])

    def hash_key(self):
        """
        SHA-256 hash the key square for secure transmission or integrity verification 
        as a hexadecimal string.
        """
        key_str = ''.join([''.join(row) for plane in self.key_square for row in plane])
        return hashlib.sha256(key_str.encode()).hexdigest()

    def display_key(self):
        """
        Display the key square for debugging or verification purposes.
        """
        for plane in self.key_square:
            for row in plane:
                print(row)
            print()

# Example usage
key_square = [
    [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
    [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']],
    [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', '.']]
]

cipher = TrifidCipher(key_square)

# Encrypting a message
plaintext = "TRIFID CYPHER EXTREME COMPLICATEDDDD"
ciphertext = cipher.encrypt(plaintext, period=5)
print(f"Ciphertext: {ciphertext}")

# Decrypting the message
decrypted_text = cipher.decrypt(ciphertext, period=5)
print(f"Decrypted Text: {decrypted_text}")

# Display the key and its hash
cipher.display_key()
print(f"Key Hash: {cipher.hash_key()}")