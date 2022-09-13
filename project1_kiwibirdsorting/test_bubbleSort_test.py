
from bubbleSort_test import bubblesort
from bubbleSort_test import list
from time import *
import timeit
import time
import pytest

averagecase = list
#print(averagecase)
bestcase = sorted(averagecase)
#print(bestcase)
worstcase = sorted(averagecase, reverse = True)
#print(worstcase)


def TestBubbleSortAveragecase():
    startTime=time.perf_counter()
    #print("Sorted Array is, ")
    #print(list)
    assert bubblesort(averagecase)==bestcase
    elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
    print ("The time of averagecase sorting process used is:", elapsed) 

def TestBubbleSortBestcase():
    startTime=time.perf_counter()    
    #print(bestcase)
    assert bubblesort(bestcase)==bestcase
    elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
    print ("The time of bestcase sorting process used is:", elapsed) 
    
def TestBubbleSorWorstcase(): 
    startTime=time.perf_counter()
    assert bubblesort(worstcase)==bestcase
    #print(worstcase)
    elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
    print ("The time of worstcase sorting process used is:", elapsed)