# Get input from the user
n = int(input("Enter a positive integer: "))

# Check if the input is a non-negative integer
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    # Initialize a variable to store the factorial
    factorial = 1
    
    # Loop from 1 to n and multiply each number to the factorial
    for i in range(1, n + 1):
        factorial *= i
        
    # Print the result
    print(f"The factorial of {n} is {factorial}.")
