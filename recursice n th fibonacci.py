def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = int(input("Enter the value of n: "))
result = fibonacci_recursive(n)
print(f"The {n}th Fibonacci number is: {result}")
