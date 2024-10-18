def sigma(f, start, end):
    """
    Compute the sigma (summation) of a function f over the range [start, end].

    :param f: Function to apply on each element of the range
    :param start: Starting integer of the range (inclusive)
    :param end: Ending integer of the range (inclusive)
    :return: Summation result
    """
    return sum(f(i) for i in range(start, end + 1))

# Example usage
# Define a simple function to be used within sigma
def square(x):
    return x ** 2

# Calculate the summation of squares from 1 to 5
result = sigma(square, 1, 5)
print("Sigma result (functional):", result)



class SigmaCalculator:
    def __init__(self, func):
        """
        Initialize the SigmaCalculator with a function to be applied in the summation.

        :param func: Function to apply on each element of the range
        """
        self.func = func
    
    def calculate(self, start, end):
        """
        Perform the summation using the provided function over the range [start, end].
        """
        return sum(self.func(i) for i in range(start, end + 1))

# Example usage
# Instantiate SigmaCalculator with the square function
# sigma_calculator = SigmaCalculator(square)
# result_oop = sigma_calculator.calculate(1, 5)
# print("Sigma result (OOP):", result_oop)



# Using lambda function for cube operation
# result_lambda = sigma(lambda x: x ** 3, 1, 5)
# print("Sigma of cubes (lambda):", result_lambda)

# Using SigmaCalculator with a lambda for cube
# sigma_calculator_lambda = SigmaCalculator(lambda x: x ** 3)
# result_oop_lambda = sigma_calculator_lambda.calculate(1, 5)
# print("Sigma of cubes (OOP with lambda):", result_oop_lambda)



# Input validation and error handling
class SigmaCalculator:
    def __init__(self, func):
        self.func = func

    def validate_input(self, start, end):
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Start and end must be integers.")
        if start > end:
            raise ValueError("Start must be less than or equal to end.")
    
    def calculate(self, start, end):
        self.validate_input(start, end)
        return sum(self.func(i) for i in range(start, end + 1))

# Example usage
try:
    sigma_calculator = SigmaCalculator(lambda x: x ** 2)
    result = sigma_calculator.calculate(5, 1)  # Invalid range, will raise an error
except ValueError as e:
    print(e)



# Extending for common math sequences
class SigmaCalculator:
    def __init__(self, func=None):
        self.func = func
    
    def validate_input(self, start, end):
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Start and end must be integers.")
        if start > end:
            raise ValueError("Start must be less than or equal to end.")
    
    def calculate(self, start, end):
        self.validate_input(start, end)
        return sum(self.func(i) for i in range(start, end + 1))
    
    @staticmethod
    def arithmetic_sequence(a1, d, n):
        """
        Calculates the sum of the first n terms of an arithmetic sequence.
        :param a1: The first term
        :param d: The common difference
        :param n: The number of terms
        :return: Sum of the sequence
        """
        return n * (2 * a1 + (n - 1) * d) // 2
    
    @staticmethod
    def geometric_sequence(a1, r, n):
        """
        Calculates the sum of the first n terms of a geometric sequence.
        :param a1: The first term
        :param r: The common ratio
        :param n: The number of terms
        :return: Sum of the sequence
        """
        if r == 1:
            return a1 * n
        return a1 * (1 - r ** n) // (1 - r)

# Example usage
# Arithmetic sequence: a1=1, d=2, n=5 (1, 3, 5, 7, 9)
arithmetic_sum = SigmaCalculator.arithmetic_sequence(1, 2, 5)
print("Arithmetic sequence sum:", arithmetic_sum)

# Geometric sequence: a1=2, r=3, n=4 (2, 6, 18, 54)
geometric_sum = SigmaCalculator.geometric_sequence(2, 3, 4)
print("Geometric sequence sum:", geometric_sum)