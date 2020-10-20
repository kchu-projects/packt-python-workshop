import time

stored_results = {}

def sum_to_n(n):
    start_time = time.perf_counter()
    result = 0
    for i in reversed(range(n)):
        try:
            result += stored_results[i + 1]
        except KeyError:
            result += i + 1
        else:
            break
        # if i + 1 in stored_results:
        #     print('Stopping sum at %s because we have previously computed it' % str(i + 1))
        #     result += stored_results[i + 1]
        #     break
        # else:
        #     result += i + 1
    stored_results[n] = result
    print(time.perf_counter() - start_time, "seconds")
    return result


# print(sum_to_n(5))
# print(sum_to_n(6))
print(sum_to_n(1000000))
