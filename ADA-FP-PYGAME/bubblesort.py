import pandas as pd
import numpy as np
import time
import tracemalloc #for memory

def bubbleSort(x):
    
    st = time.time()
    #starting to count memory
    tracemalloc.start()
    # to transverse the array
    n = len(x)
    for i in range(n):
        for j in range(n - i - 1):
            if x[j] > x[j + 1]:
                # sorting by using simultaneous assignment in python
                x[j], x[j + 1] = x[j + 1], x[j]
    #displaying the memory after calling the  recursion
    print("Memory taken when running the program:", tracemalloc.get_traced_memory())
    #stopping the library
    tracemalloc.stop()
    et = time.time()
    #execution time
    elapsed_time = et - st
    #trying it in milisec
    r = elapsed_time *1000
    print('Insertion sort execution time:', r, 'miliseconds')