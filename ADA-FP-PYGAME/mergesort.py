import pandas as pd
import numpy as np
import time
import tracemalloc #for memory

def merge(left, right):
    result = []
    x, y = 0, 0
    for k in range(0, len(left) + len(right)):
        if x == len(left): # if at the end of 1st half,
            result.append(right[y]) # add all values of 2nd half
            y += 1
        elif y == len(right): # if at the end of 2nd half,
            result.append(left[x]) # add all values of 1st half
            x += 1
        elif right[y] < left[x]:
            result.append(right[y])
            y += 1
        else:
            result.append(left[x])
            x += 1
    return result

def mergeSort(ar_list):
    st = time.time()
    #starting to count memory
    tracemalloc.start()
    length = len(ar_list)
    size = 1
    while size < length:
        size+=size # initializes at 2 as described
        for pos in range(0, length, size):
            start = pos
            mid = pos + int(size / 2)
            end = pos + size
            left = ar_list[ start : mid ]
            right = ar_list[ mid : end ]
            ar_list[start:end] = merge(left, right)
    #displaying the memory after calling the  recursion
    print("Memory taken when running the program:", tracemalloc.get_traced_memory())
    #stopping the library
    tracemalloc.stop()
    et = time.time()
    #execution time
    elapsed_time = et - st
    #trying it in milisec
    r = elapsed_time *1000
    print('Merge sort execution time:', r, 'miliseconds')
    print(ar_list)
    return ar_list