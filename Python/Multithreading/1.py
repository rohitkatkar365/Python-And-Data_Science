import time
import threading

def square(n):
    for i in range(n):
        time.sleep(0.2)
        print(f"Square Of {i} is :- {i*i}")

def cube(n):
    for i in range(n):
        time.sleep(0.2)
        print(f"Cube Of {i} is :- {i*i*i}")

t = time.time()
# Done in :-  2.0156657695770264
# square(5)
# cube(5)

# Done in :-  1.0150587558746338
t1 = threading.Thread(target=square,args=(5,));
t2 = threading.Thread(target=cube,args=(5,));

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in :- ",time.time()-t)