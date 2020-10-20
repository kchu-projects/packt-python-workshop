def fibonacci_iterative(num):
    fib1 = fib2 = fib3 = 1

    for _ in range(num - 2):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3

    return fib3


print(fibonacci_iterative(2))
print(fibonacci_iterative(3))
print(fibonacci_iterative(100))
