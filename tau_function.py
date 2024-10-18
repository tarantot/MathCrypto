class NumberTheory:
    def __init__(self, number):
        """
        Initialize with the number for which compute the Tau function.
        """
        self.number = number

    def tau_function(self):
        """
        Method to calculate the Tau (divisor) function.
        Counts the number of divisors of a given number.
        """
        if self.number <= 0:
            raise ValueError("Tau function is only defined for positive integers.")
        
        divisors_count = 0
        for i in range(1, self.number + 1):
            if self.number % i == 0:
                divisors_count += 1
        return divisors_count

    def display_divisors(self):
        """
        Method to display all the divisors of the number.
        """
        divisors = [i for i in range(1, self.number + 1) if self.number % i == 0]
        return divisors

# Example usage:
if __name__ == "__main__":
    number = 36
    tau_calculator = NumberTheory(number)
    
    print(f"The divisors of {number} are: {tau_calculator.display_divisors()}")
    print(f"The Tau function value for {number} is: {tau_calculator.tau_function()}")
