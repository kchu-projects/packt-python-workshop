import functools
import time


def func(x):
    time.sleep(1)
    print(f"Heavy operation for {x}")
    return x * 10


cached_func = functools.lru_cache()(func)

print(f"Cached func returned: {cached_func(1)}")
print(f"Cached func returned: {cached_func(1)}")
print(f"Func returned: {func(1)}")
print(f"Func returned: {func(1)}")
# print(f"Func returned: {func(2)}")
# print(f"Func returned: {func(3)}")
# print(f"Func returned: {func(3)}")
# print(f"Func returned: {func(2)}")
# print(f"Func returned: {func(1)}")
