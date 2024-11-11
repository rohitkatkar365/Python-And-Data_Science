import time
import multiprocessing

def square(n):
    for i in range(n):
        time.sleep(0.2)
        print(f"Square Of {i} is :- {i*i}")

def cube(n):
    for i in range(n):
        time.sleep(0.2)
        print(f"Cube Of {i} is :- {i*i*i}")

if __name__ ==  "__main__":
    t = time.time()

    # Correcting the args by making sure it's a tuple
    t1 = multiprocessing.Process(target=square, args=(5,))
    t2 = multiprocessing.Process(target=cube, args=(5,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done in :- ", time.time() - t)
