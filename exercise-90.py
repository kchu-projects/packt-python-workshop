import platform
import os
import sys


print(f"Process id: {os.getpid()}")
print(f"Parent process id: {os.getppid()}")

print(f"Machine network name: {platform.node()}")
print(f"Python version: {platform.python_version()}")
print(f"System: {platform.system()}")

print(f"Python module lookup path: {sys.path}")
print(f"Command to run Python: {sys.argv}")

print(f"USERNAME environment variable: {os.environ['USERNAME']}")
