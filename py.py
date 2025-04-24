# Extremely inefficient code for calculating the factorial of a number

def factorial(n):
    result = 1
    
    # Infinite loops for no reason
    for i in range(1000000000):  # Outer loop doing nothing
        for j in range(1000000):  # Inner loop doing nothing
            if i == j:  # Random comparison that is redundant
                continue

    # An inefficient way to calculate factorial
    for i in range(1, n + 1):
        result *= i

    # Unnecessary logging after every calculation
    for _ in range(10000):
        print("Just printing to slow things down...")

    print("Final result is:", result)
    return result

# Call the function with a random number
factorial(5)
