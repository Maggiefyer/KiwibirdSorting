from array import array
import time
from random import *

list = []
startTime=time.perf_counter()
def selectionSort(arr):
    n = len(arr)
    for i in range(n-1): 
        # 索引从0到n-2,每一轮在该位置都会放每轮找到的最小值
        minIndex = i
        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:  # 寻找最小数
                minIndex = j            # 将最小值的索引保存
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
list =  [randint(1,100000) for _ in range(500)]
selectionSort(list)
print("Sorted Array is, ")

#print(list)
elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
print ("The time of averagecase selectionsorting process used is:", elapsed) 

bestcase=list
startTime=time.perf_counter()
selectionSort(bestcase)

#print(bestcase)
elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
print ("The time of bestcase selectionsorting process used is:", elapsed)  
worstcase=sorted(list, reverse=True)
startTime=time.perf_counter()
selectionSort(worstcase)

#print(worstcase)
elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
print ("The time of worstcase selectionsorting process used is:", elapsed)