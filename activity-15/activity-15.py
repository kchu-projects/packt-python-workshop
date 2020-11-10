import time
import random


time_start = time.time_ns()
my_list = [random.randint(1, 999) for _ in range(10 * 3)]
time_end = time.time_ns()
print(time_end - time_start)
