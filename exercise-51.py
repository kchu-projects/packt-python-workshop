def factorial_iterative(n):
    result = 1
    for i in range(n):
        result *= i+1
    return result

print(factorial_iterative(5))


def factorial_recursive(n):
    if n == 1 or n == 0:  # not defined for negative values of n
        return 1
    else:
        return n * factorial_recursive(n-1)
