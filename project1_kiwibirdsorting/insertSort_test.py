from array import array
import time
from random import *
lst=[]
startTime=time.perf_counter()
def insertSort(list):
    # 从第二个位置下标为1的位置开始插入
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if list[j]<list[j-1]:
                list[j],list[j-1]=list[j-1],list[j]
    return list
if __name__=='__main__':
 lst =  [randint(1,100000) for _ in range(500)]      
value=insertSort(lst)
      #print(value
elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
print ("The time of averagecase insertSorting process used is:", elapsed) 
bestcase=value
startTime=time.perf_counter()
insertSort(bestcase)
#print(bestcase)
elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
print ("The time of bestcase insertSorting process used is:", elapsed)  
worstcase=sorted(value, reverse=True)
startTime=time.perf_counter()
#print(worstcase)
insertSort(worstcase)
elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
print ("The time of worstcase insertSorting process used is:", elapsed)