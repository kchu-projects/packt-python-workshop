def primes_below(bound):
    candidates = list(range(2, bound))
    while len(candidates) > 0:
        yield candidates[0]
        candidates = [c for c in candidates if c % candidates[0] != 0]


print([prime for prime in primes_below(100)])
