import pandas as pd
import numpy as np
import time
import random
import tracemalloc #for memory

# Sorts array a[0..n-1] using Bogo sort
def bogoSort(a):
    st = time.time()
    #starting to count memory
    tracemalloc.start()
    n = len(a)
    while (is_sorted(a)== False):
        shuffle(a)
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
 
# To check if array is sorted or not
def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True
 
# To generate permutation of the array
def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]
 

