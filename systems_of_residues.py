class ResidueSystem:
    def __init__(self, value: int, modulus: int):
        self.value = value % modulus 
        self.modulus = modulus 

    def __add__(self, other):
        if isinstance(other, ResidueSystem) and self.modulus == other.modulus:
            return ResidueSystem(self.value + other.value, self.modulus)
        else:
            raise ValueError("Moduli must be the same for addition.")

    def __mul__(self, other):
        if isinstance(other, ResidueSystem) and self.modulus == other.modulus:
            return ResidueSystem(self.value * other.value, self.modulus)
        else:
            raise ValueError("Moduli must be the same for multiplication.")

    def inverse(self):
        # Using Extended Euclidean Algorithm to find the multiplicative inverse
        g, x, y = self.extended_gcd(self.value, self.modulus)
        if g != 1:
            raise ValueError(f"No inverse exists for {self.value} modulo {self.modulus}.")
        else:
            return ResidueSystem(x % self.modulus, self.modulus)

    def exp(self, exponent: int):
        # Fast modular exponentiation
        base = self.value
        result = 1
        modulus = self.modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            base = (base * base) % modulus
            exponent //= 2
        return ResidueSystem(result, modulus)

    @staticmethod
    def extended_gcd(a: int, b: int):
        """Returns (g, x, y) such that a * x + b * y = g = gcd(a, b)"""
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0

    def __str__(self):
        return f"{self.value} (mod {self.modulus})"

# Example Usage:
modulus = 17  # Example modulus
a = ResidueSystem(15, modulus)
b = ResidueSystem(10, modulus)

# Add two residues
sum_residue = a + b
print(f"Sum: {sum_residue}")  # Should print 8 (mod 17)

# Multiply two residues
prod_residue = a * b
print(f"Product: {prod_residue}")  # Should print 14 (mod 17)

# Find inverse
inverse_a = a.inverse()
print(f"Inverse of a: {inverse_a}")  # Should print the inverse of 15 mod 17

# Exponentiation
exp_result = a.exp(3)
print(f"a^3 mod 17: {exp_result}")  # Should print (15^3 mod 17)