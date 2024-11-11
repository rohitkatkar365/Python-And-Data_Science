import threading

balance = 0
lock = threading.Lock()

def deposit(amount):
    global balance
    with lock:  # Acquire the lock before modifying shared data
        balance += amount

threads = []
for i in range(10):
    t = threading.Thread(target=deposit, args=(100,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Final balance: {balance}")