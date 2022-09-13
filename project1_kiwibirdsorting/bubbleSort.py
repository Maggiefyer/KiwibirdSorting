#bubbleSort
from array import array
import time 
import pandas as pd
import numpy as np
from random import randint, random

startTime=time.perf_counter()
print ("bubbleSortTestingCase")
#print ( "the array need be sorted is:" )
array=[randint(1,100000) for _ in range(500)] 
#array =input()
#birdWeight=pd.read_csv('d:/Level6Term3/Project1/KiwiBirdData.csv', sep=',')
#array =birdWeight
#print (array)
#element=array.split(',') 
#arr=list(map(int,element)) 
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
        return arr
        
    return(arr)
elapsed=(time.perf_counter())-startTime
print ("The time of sorting process used is:", elapsed)
print("Unsorted Array is,")
print(array)
bubblesort(array)
print("Sorted Array is:")
print(array)


