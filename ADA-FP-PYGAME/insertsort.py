import pandas as pd
import numpy as np
import time
import tracemalloc #for memory

def insertionSort(x):
    st = time.time()
    #starting to count memory
    tracemalloc.start()
    # to transverse the array
    for i in range(1,len(x)):
        key=x[i]
        j=i-1
        while j>=0 and key<x[j]:
            x[j+1]=x[j]
            j=j-1
        x[j+1]=key
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
