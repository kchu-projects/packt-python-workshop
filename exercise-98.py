import sys
import functools

print("Hello stderr", file=sys.stderr)

print_stderr = functools.partial(print, file=sys.stderr)
print_stderr("Hello stderr")
