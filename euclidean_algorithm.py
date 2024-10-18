class EuclideanAlgorithm:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def compute_gcd(self) -> int:
        """
        Compute the greatest common divisor (GCD) using the Euclidean algorithm.
        :return: The GCD of self.a and self.b
        """
        a, b = self.a, self.b
        while b != 0:
            a, b = b, a % b
        return a

# Example of usage:
# if __name__ == "__main__":
#     gcd_solver = EuclideanAlgorithm(48, 18)
#     print(f"The GCD of 48 and 18 is: {gcd_solver.compute_gcd()}")



def euclidean_algorithm(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) using the Euclidean algorithm.
    
    :param a: First number
    :param b: Second number
    :return: The GCD of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a

# Example of usage:
# if __name__ == "__main__":
#     print(f"The GCD of 48 and 18 is: {euclidean_algorithm(48, 18)}")


def extended_euclidean(a, b):
    """
    Function to compute the gcd of a and b, as well as the Bézout coefficients.
    Returns: gcd, x, y such that ax + by = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0 
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Example usage
# a, b = 56, 15
# gcd, x, y = extended_euclidean(a, b)
# print(f"GCD: {gcd}, Coefficients: x = {x}, y = {y}")


class ExtendedEuclidean:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.gcd, self.x, self.y = self._compute_gcd()

    def _compute_gcd(self):
        """
        Internal method to compute gcd and coefficients using recursion.
        """
        return self._extended_euclidean(self.a, self.b)

    @staticmethod
    def _extended_euclidean(a, b):
        """
        Static method to recursively calculate gcd and Bézout coefficients.
        """
        if b == 0:
            return a, 1, 0  # Base case: gcd is 'a'
        else:
            gcd, x1, y1 = ExtendedEuclidean._extended_euclidean(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return gcd, x, y

    def get_gcd(self):

        return self.gcd

    def get_coefficients(self):
        return self.x, self.y

# Example usage
# a, b = 56, 15
# ext_euclid = ExtendedEuclidean(a, b)
# print(f"OOP GCD: {ext_euclid.get_gcd()}, Coefficients: x = {ext_euclid.get_coefficients()[0]}, y = {ext_euclid.get_coefficients()[1]}")