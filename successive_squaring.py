import time

class SuccessiveSquaring:
    def __init__(self, base, exponent, modulus):
        """
        Initializes the SuccessiveSquaring object with base, exponent, and modulus.
        """
        self.base = base
        self.exponent = exponent
        self.modulus = modulus

    def compute(self):
        """
        Computes (base^exponent) % modulus using successive squaring.
        :return: The result of the modular exponentiation.
        """
        result = 1
        base = self.base % self.modulus
        exponent = self.exponent

        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % self.modulus

            base = (base * base) % self.modulus
            exponent = exponent // 2

        return result

    def __str__(self):
        """
        String representation of the class result.
        """
        return f"{self.base}^{self.exponent} % {self.modulus} = {self.compute()}"


# Example usage:
# mod_exp = SuccessiveSquaring(5, 117, 19)
# print(mod_exp)  # Output: 5^117 % 19 = 1



# Functional implementation
def successive_squaring(base, exponent, modulus):
    """
    Computes (base^exponent) % modulus using successive squaring.
    :return: The result of (base^exponent) % modulus.
    """
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # If exponent is odd, multiply base with result
        if exponent % 2 == 1:
            result = (result * base) % modulus
            
        # Square the base and reduce the exponent by half
        base = (base * base) % modulus
        exponent = exponent // 2
    
    return result

# Example computation
# print(successive_squaring(5, 117, 19))



# Extended OOP Version with input validation and error-handling

class SuccessiveSquaring:
    def __init__(self, base, exponent, modulus):
        if not isinstance(base, int) or not isinstance(exponent, int) or not isinstance(modulus, int):
            raise ValueError("Base, exponent, and modulus must be integers.")
        if modulus <= 0:
            raise ValueError("Modulus must be a positive integer.")
        self.base = base
        self.exponent = exponent
        self.modulus = modulus

    def compute(self):
        try:
            result = 1
            base = self.base % self.modulus
            exponent = self.exponent

            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % self.modulus

                base = (base * base) % self.modulus
                exponent = exponent // 2

            return result
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def __str__(self):
        return f"{self.base}^{self.exponent} % {self.modulus} = {self.compute()}"

# Example usage:
# try:
#     mod_exp = SuccessiveSquaring(5, 117, 19)
#     print(mod_exp)  # Output: 5^117 % 19 = 1
# except ValueError as e:
#     print(e)



# Adding benchmarking for performance analysis
class SuccessiveSquaringBenchmark(SuccessiveSquaring):
    def benchmark(self):
        start_time = time.time()
        result = self.compute()
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time

# Example usage with benchmarking:
mod_exp_benchmark = SuccessiveSquaringBenchmark(5, 117, 19)
result, exec_time = mod_exp_benchmark.benchmark()
print(f"Result: {result}, Execution Time: {exec_time:.6f} seconds")