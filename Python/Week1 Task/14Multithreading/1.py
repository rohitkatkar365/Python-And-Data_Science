# <!-- ## Exercise: Multithreading

# 1. Create any multithreaded code using for loop for creating multithreads

# ```
# for i in range(10):
#     th = Thread(target=func_name, args=(i, ))
    
# ```
# 2. print total active threads in multithreaded code using threading.active_count()

import threading

def task(n):
    print(n)

threads = []  # List to hold all thread references

# Create and start all threads
for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()  # Start the thread
    threads.append(t)  # Add the thread to the list
    # print(f"Total Active Thread {threading.active_count()}")

# Wait for all threads to complete
for t in threads:
    t.join()
    

print("All threads have finished.")
