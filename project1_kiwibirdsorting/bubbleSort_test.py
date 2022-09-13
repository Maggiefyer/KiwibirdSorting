from array import array
from re import T
import time
from random import *
from time import *
import timeit
import time
import pytest
  
list = [randint(1,100000) for _ in range(500)] 
startTime=time.perf_counter()
def bubblesort(arr):    
    swapped = False
    # Looping back to index[0]
    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                arr[i], arr[i + 1] = arr[i + 1], arr[i]       
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return 
    return arr
bubblesort(list)
print("Sorted Array is, ")
#print(list)
elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
print ("The time of averagecase Bubblesorting process used is:", elapsed) 

bestcase=list
startTime=time.perf_counter() 
bubblesort(bestcase)
#print(bestcase)
elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
print ("The time of bestcase Bubblesorting process used is:", elapsed) 
 
worstcase=sorted(list, reverse=True)

startTime=time.perf_counter()
bubblesort(worstcase)
#print(worstcase)
elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
print ("The time of worstcase Bubblesorting process used is:", elapsed)