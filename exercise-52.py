stored_results = {}

def sum_to_n(n):
    result = 0
    for i in reversed(range(n)):
        try:
            result += stored_results[i + 1]
        except KeyError:
            result += i + 1
        else:
            break
    stored_results[n] = result
    return result


print(sum_to_n(5))
print(sum_to_n(6))
