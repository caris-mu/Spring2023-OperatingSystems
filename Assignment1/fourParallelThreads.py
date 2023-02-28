import threading
import time

def demo(num):
    print(f"Thread {num + 1} is running")
    time.sleep(3)
    print(f"Thread {num + 1} finished")

threads = []
for i in range(4):
    # Initiate new thread
    t = threading.Thread(target=demo, args=(i,))
    threads.append(t)
    # Run demo(i) on that new thread
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads finished")

