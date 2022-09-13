import time
import  csv
import pandas as pd 

datas = pd.read_csv('kiwibirddatainfo.csv',usecols=['Weight(kg)'])
datas.to_csv('weight.csv', index=False)#write data in csv file 
datan=pd.read_csv('weight.csv')
BirdWeight=datan.values.tolist()#generate list

#TimeMeasurementFunction
#startTime=time.perf_counter()

#BubbleSortAlgorithm
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
#elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
#print("Unsorted Array is,")
#print(BirdWeight)
bubblesort(BirdWeight)
print("Sorted Array is, ")
print(BirdWeight)
#print ("The time of sorting process used is:", elapsed)

    




