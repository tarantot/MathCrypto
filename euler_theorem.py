from math import gcd
from mathutils import euler_totient

# Helper function to calculate Euler's Totient function φ(n)
def euler_totient(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count

# Implementing Euler's Theorem
class EulerTheorem:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.phi_n = euler_totient(n)

    # Method to check if two numbers are coprime (gcd == 1)
    def is_coprime(self):
        return gcd(self.a, self.n) == 1

    # Method to compute a^phi(n) % n
    def euler_theorem(self):
        if self.is_coprime():
            # Fermat's/Euler's theorem: a^phi(n) ≡ 1 (mod n)
            result = pow(self.a, self.phi_n, self.n)
            return result
        else:
            raise ValueError("a and n are not coprime!")

# Example usage:
if __name__ == "__main__":
    a = 7  # Base number
    n = 10  # Modulus number
    
    # Create an instance of EulerTheorem
    theorem = EulerTheorem(a, n)
    
    if theorem.is_coprime():
        print(f"a^phi(n) ≡ {theorem.euler_theorem()} (mod {n})")
    else:
        print(f"{a} and {n} are not coprime!")



# def euler_totient(n):
#     """
#     Calculates Euler's Totient function φ(n).
#     :param n: The modulus number
#     :return: The count of integers less than n that are coprime with n
#     """
#     count = 0
#     for i in range(1, n):
#         if gcd(i, n) == 1:
#             count += 1
#     return count



# class EulerTheorem:
#     def __init__(self, a, n):
#         self.a = a
#         self.n = n
#         self.phi_n = euler_totient(n)

#     def is_coprime(self):
#         """
#         Checks if two numbers are coprime.
#         :return: True if gcd(a, n) == 1, else False
#         """
#         return gcd(self.a, self.n) == 1

#     def euler_theorem(self):
#         """
#         Computes a^phi(n) % n using Euler's Theorem.
#         :return: Result of the computation
#         :raises: ValueError if a and n are not coprime
#         """
#         if self.is_coprime():
#             return pow(self.a, self.phi_n, self.n)
#         else:
#             raise ValueError("a and n are not coprime!")
        


# def main():
#     a = int(input("Enter base (a): "))
#     n = int(input("Enter modulus (n): "))

#     theorem = EulerTheorem(a, n)
    
#     try:
#         result = theorem.euler_theorem()
#         print(f"{a}^phi({n}) ≡ {result} (mod {n})")
#     except ValueError as e:
#         print(e)

# if __name__ == "__main__":
#     main()