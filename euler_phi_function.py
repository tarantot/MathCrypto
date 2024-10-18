import json

class EulerPhi:
    def __init__(self, n):
        """
        Initializes the EulerPhi object with the integer n.
        """
        self.n = n

    def gcd(self, a, b):
        """
        Calculates the greatest common divisor (GCD) of two numbers a and b using the Euclidean algorithm.
        """
        while b != 0:
            a, b = b, a % b
        return a

    def is_coprime(self, a, b):
        """
        Determines if two numbers a and b are coprime.
        """
        return self.gcd(a, b) == 1

    def phi_bruteforce(self):
        """
        Calculates the Euler-Phi function of n using a brute-force method.
        Check for each number less than n whether it is coprime with n.
        """
        count = 0
        for i in range(1, self.n):
            if self.is_coprime(i, self.n):
                count += 1
        return count

    def prime_factors(self):
        """
        Determines the prime factors of the number n.
        """
        factors = set()
        num = self.n
        # Check for number of 2's that divide n
        if num % 2 == 0:
            factors.add(2)
        while num % 2 == 0:
            num //= 2
        # Check for other primes
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                factors.add(i)
                num //= i
        if num > 2:
            factors.add(num)
        return factors

    def phi_optimized(self):
        """
        Optimized calculation using prime factorization and the formula:
        φ(n) = n * Π(1 - 1/p) where p are the distinct prime factors of n.
        """
        result = self.n
        prime_factors = self.prime_factors()
        for p in prime_factors:
            result *= (1 - 1 / p)
        return int(result)

# Example usage
# n = 36
# euler_phi = EulerPhi(n)

# Brute-force approach
# print(f"Euler's Totient function (brute-force) of {n} is: {euler_phi.phi_bruteforce()}")

# Optimized approach using prime factorization
# print(f"Euler's Totient function (optimized) of {n} is: {euler_phi.phi_optimized()}")



# Code with memoization and utility methods

class EulerPhiMemoized:
    def __init__(self):
        self.memo = {}

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def prime_factors(self, n):
        factors = set()
        num = n
        if num % 2 == 0:
            factors.add(2)
        while num % 2 == 0:
            num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                factors.add(i)
                num //= i
        if num > 2:
            factors.add(num)
        return factors

    def phi_optimized(self, n):
        if n in self.memo:
            return self.memo[n]

        result = n
        prime_factors = self.prime_factors(n)
        for p in prime_factors:
            result *= (1 - 1 / p)
        self.memo[n] = int(result)
        return self.memo[n]

    def to_json(self, n):
        result = {"n": n, "phi": self.phi_optimized(n)}
        return json.dumps(result, indent=4)

# Example usage
# phi_calc = EulerPhiMemoized()
# n = 36
# print(phi_calc.to_json(n))
