def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(3))
print(fibonacci_recursive(10))
