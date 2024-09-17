import math

'''
if m / (a-b) then a ≡ b * abs(m)
2x + 1 ≡ 5 - congruence

0 ≡ 2 * math.pi ≡ 4 * math.pi

Example with clock:
14 ≡ 2 (mod 12)
20 ≡ 8 (mod 12)
abs(8 - 20 ) ≡ 12

m / (a-b)
'''

class LinearCongruenceSolver:
    def __init__(self, a: int, b: int, n: int):
        self.a = a  # Coefficient of x
        self.b = b  # Right-hand side of the congruence
        self.n = n  # Modulus

    def gcd_extended(self, a: int, b: int):
        """
        Extended Euclidean Algorithm to compute gcd and coefficients.
        Returns gcd, x, y such that a*x + b*y = gcd(a, b)
        """
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    def mod_inverse(self, a: int, n: int):
        """
        Computes the modular inverse of a modulo n using the Extended Euclidean Algorithm.
        The modular inverse of a is x such that a*x ≡ 1 (mod n).
        """
        gcd, x, y = self.gcd_extended(a, n)
        if gcd != 1:
            raise ValueError(f"Modular inverse does not exist for a={a} and n={n}")
        else:
            # x might be negative, so we take it modulo n to ensure it's positive
            return x % n

    def solve(self):
        """
        Solves the linear congruence equation a*x ≡ b (mod n)
        using the method of finding the modular inverse.
        """
        # First, find the gcd of a and n
        gcd, _, _ = self.gcd_extended(self.a, self.n)
        
        # Check if the congruence has a solution
        if self.b % gcd != 0:
            raise ValueError(f"No solutions exist for the congruence {self.a}x ≡ {self.b} (mod {self.n})")

        # Simplify the congruence by dividing a, b, and n by gcd
        a_simplified = self.a // gcd
        b_simplified = self.b // gcd
        n_simplified = self.n // gcd

        # Find the modular inverse of a_simplified mod n_simplified
        inverse_a = self.mod_inverse(a_simplified, n_simplified)

        # The solution to the congruence is x ≡ inverse_a * b_simplified (mod n_simplified)
        x0 = (inverse_a * b_simplified) % n_simplified

        # The general solution to the congruence is x ≡ x0 + k*(n_simplified), for k ∈ Z
        solutions = [x0 + k * n_simplified for k in range(gcd)]

        return solutions

# Example usage:
if __name__ == "__main__":
    # Solving the linear congruence: 14x ≡ 30 (mod 100)
    solver = LinearCongruenceSolver(14, 30, 100)
    solutions = solver.solve()
    print(f"Solutions to the congruence: {solutions}")

    ''' 3x ≡ 6 (mod9) '''
    solver1 = LinearCongruenceSolver(3, 6, 9)
    solutions1 = solver1.solve()
    print(f"Solutions to the congruence 3x ≡ 6 (mod 9): {solutions1}")

    ''' 17x ≡ 1 (mod31) '''
    solver2 = LinearCongruenceSolver(17, 1, 31)
    solutions2 = solver2.solve()
    print(f"Solutions to the congruence 17x ≡ 1 (mod 31): {solutions2}")

    ''' 35x ≡ 10 (mod50) '''
    solver3 = LinearCongruenceSolver(35, 10, 50)
    solutions3 = solver3.solve()
    print(f"Solutions to the congruence 35x ≡ 10 (mod 50): {solutions3}")

    ''' 9x ≡ 15 (mod24) '''
    solver4 = LinearCongruenceSolver(9, 15, 24)
    solutions4 = solver4.solve()
    print(f"Solutions to the congruence 9x ≡ 15 (mod 24): {solutions4}")

    ''' 12x ≡ 20 (mod28) '''
    solver5 = LinearCongruenceSolver(12, 20, 28)
    solutions5 = solver5.solve()
    print(f"Solutions to the congruence 12x ≡ 20 (mod 28): {solutions5}")
