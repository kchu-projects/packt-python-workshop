import random
import math
random.seed(0)


def estimate_pi():
    limit_points = 10000
    num_points = 0

    for total_points in range(1, limit_points + 1):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x ** 2 + y ** 2)
        if distance < 1:
            num_points += 1
        if total_points % 1000 == 0:
            yield 4 * num_points / total_points


for cur, estimate in enumerate(estimate_pi()):
    print(f"Estimate {cur + 1}: {estimate}")
    print(f"Difference from pi: {math.pi - estimate}")
