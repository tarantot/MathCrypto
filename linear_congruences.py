class LinearCongruenceSolver:
    def __init__(self, a, b, m):
        """
        Initialize the linear congruence solver for the equation ax ≡ b (mod m)
        :param a: Coefficient of x
        :param b: Right-hand side constant
        :param m: Modulus
        """
        self.a = a
        self.b = b
        self.m = m
    
    def gcd_extended(self, a, b):
        """
        Extended Euclidean Algorithm to find the greatest common divisor (gcd) and the coefficients of Bezout's identity.
        :param a: First number
        :param b: Second number
        :return: Tuple (gcd, x, y) such that ax + by = gcd(a, b)
        """
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    def mod_inverse(self, a, m):
        """
        Computes the modular inverse of a under modulo m using the extended Euclidean algorithm.
        """
        gcd, x, _ = self.gcd_extended(a, m)
        if gcd != 1:
            return None  # Inverse doesn't exist if gcd(a, m) != 1
        else:
            return x % m
    
    def solve(self):
        """
        Solve the linear congruence equation ax ≡ b (mod m)
        """
        gcd, x, _ = self.gcd_extended(self.a, self.m)
        if self.b % gcd != 0:
            return None 
        
        a_prime = self.a // gcd
        b_prime = self.b // gcd
        m_prime = self.m // gcd
        
        a_inv = self.mod_inverse(a_prime, m_prime)
        if a_inv is None:
            return None 
        
        x0 = (b_prime * a_inv) % m_prime
        
        solutions = [(x0 + i * m_prime) % self.m for i in range(gcd)]
        return solutions

# Example usage:
a = 14
b = 30
m = 100

solver = LinearCongruenceSolver(a, b, m)
solutions = solver.solve()

if solutions:
    print(f"Solutions to {a}x ≡ {b} (mod {m}): {solutions}")
else:
    print(f"No solution exists for {a}x ≡ {b} (mod {m})")
