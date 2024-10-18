import string
from math import gcd

class AffineCipher:
    def __init__(self, a, b, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        """
        Initialize with keys a and b.
        'a' must be coprime with the alphabet size (26).
        """
        self.a = a
        self.b = b
        self.alphabet = alphabet or string.ascii_lowercase
        self.m = len(self.alphabet)
        
        if gcd(self.a, self.m) != 1:
            raise ValueError(f"'a' must be coprime with the size of the alphabet ({self.m}) for the cipher to work.")
        
    def mod_inverse(self, a, m):
        """
        Find the modular inverse of a under modulo m using the Extended Euclidean Algorithm.
        """
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError("Modular inverse does not exist.")

    def _transform_char(self, char, is_encrypt=True):
        """
        Transform a single character using the affine cipher formula.
        """
        if char.isalpha():
            alphabet = string.ascii_lowercase if char.islower() else string.ascii_uppercase
            x = alphabet.index(char)
            if is_encrypt:
                transformed_char = (self.a * x + self.b) % self.m
            else:
                a_inv = self.mod_inverse(self.a, self.m)
                transformed_char = (a_inv * (x - self.b)) % self.m
            return alphabet[transformed_char]
        return char
    
    def encrypt(self, plaintext):
        """
        Encrypt the plaintext using the affine cipher.
        """
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                char = char.lower()
                x = string.ascii_lowercase.index(char)  # Convert letter to number
                encrypted_char = (self.a * x + self.b) % self.m
                ciphertext += string.ascii_lowercase[encrypted_char]  # Convert back to letter
            else:
                ciphertext += char  # Keep non-alphabet characters unchanged
        return ciphertext

    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext using the affine cipher.
        """
        plaintext = ''
        a_inv = self.mod_inverse(self.a, self.m)
        for char in ciphertext:
            if char.isalpha():
                char = char.lower()
                y = string.ascii_lowercase.index(char)  # Convert letter to number
                decrypted_char = (a_inv * (y - self.b)) % self.m
                plaintext += string.ascii_lowercase[decrypted_char]  # Convert back to letter
            else:
                plaintext += char  # Keep non-alphabet characters unchanged
        return plaintext

# Example usage:
if __name__ == "__main__":
    a = 5  # Must be coprime with 26
    b = 8
    cipher = AffineCipher(a, b)
    
    plaintext = "Affine Cipher !!! 123"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
