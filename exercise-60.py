from datetime import datetime
import time

with open("log.txt", "w") as f:
    for i in range(0, 10):
        print(datetime.now().strftime("%Y%m%d_%H:%M:%S - "), i)
        f.write(datetime.now().strftime("%Y%m%d_%H:%M:%S - "))
        time.sleep(1)
        f.write(f"{i}\n")
