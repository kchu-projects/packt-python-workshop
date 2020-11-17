import threading
import queue

in_queue = queue.Queue()
out_queue = queue.Queue()

def square_threading():
    while True:
        n = in_queue.get()
        if n == "STOP":
            return
        n_squared = n ** 2
        out_queue.put(n_squared)


thread = threading.Thread(target=square_threading)
thread.start()

for i in range(10):
    in_queue.put(i)
    i_squared = out_queue.get()
    print(f"{i} squared is {i_squared}")

in_queue.put("STOP")
thread.join()
