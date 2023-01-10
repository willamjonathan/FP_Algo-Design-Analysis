import pandas as pd
import numpy as np
import time
import tracemalloc #for memory

def selectionSort(x):
    st = time.time()
    #starting to count memory
    tracemalloc.start()
    # to transverse the array
    # One by one move boundary of unsorted subarray
    n = len(x)
    for i in range(n):
        min_index = i
        min_str = x[i]
         
        # Find the minimum element in unsorted subarray
        for j in range(i+1,n):
             
            # If min_str is greater than x[j]
            if min_str>x[j]:
                 
                # Make x[j] as min_str and update min_index as j
                min_str = x[j]
                min_index = j
                 
        # Swap the found minimum element with the first element      
        if min_index != i:
             
            # Store the first element in temp
            temp = x[i]
             
            # Place the min element at the first position
            x[i] = x[min_index]
             
            # place the element in temp at min_index
            x[min_index] = temp
    print("Memory taken when running the program:", tracemalloc.get_traced_memory())
    #displaying the memory after calling the  recursion
    tracemalloc.stop()
    et = time.time()
    #execution time
    elapsed_time = et - st
    #trying it in milisec
    r = elapsed_time *1000
    print('Selection sort execution time:', r, 'miliseconds')
    return x