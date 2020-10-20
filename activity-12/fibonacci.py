import time

stored_results = {
    0: 0,
    1: 1
}


def fibonacci_dynamic(num):
    if num in stored_results:
        return stored_results[num]
    else:
        stored_results[num] = fibonacci_dynamic(num - 2) + fibonacci_dynamic(num - 1)
        return stored_results[num]

start_time = time.perf_counter()
print(fibonacci_dynamic(100))
print(time.perf_counter() - start_time, "seconds")
