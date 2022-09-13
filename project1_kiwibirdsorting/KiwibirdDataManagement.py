# BubbleSort Kiwibird
import time
import  csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#import matplot.ply as mpy


#check the csv file by showing details and select one column to sorting
dataInfo=pd.read_csv('d:/Level6Term3/Project1/kiwibirddatainfo.csv', sep=',')
birdWeight=pd.read_csv('d:/Level6Term3/Project1/KiwiBirdData.csv', sep=',')

#按照列值排序
data=dataInfo.sort_values( by="Weight(kg)" , ascending=True)
#把新的数据写入文件
data.to_csv('sortedData.csv', index=False)

#display the cvs files' content to check if it is right.
print(dataInfo)
print(birdWeight.head())
print(birdWeight.tail())
data = 'sortedData.csv'
dt=pd.read_csv(data)
print (dt)
with open(data) as file:
        #create a reader：pass file to csv.reader
        reader = csv.reader(file)
        #use "next()" function pass the value of reader to next，it return the next line of the file
        header_row = next(reader)        
        for index, column_header in enumerate(header_row):
                print(index, column_header)
#Weight =[]
        #遍历reader的余下的所有行（next读取了第一行，reader每次读取后将返回下一行）
#for row in reader:                
                #Weight.append(row[1])
#print(Weight)
datas = pd.read_csv('kiwibirddatainfo.csv',usecols=['Weight(kg)'])
datas.to_csv('weight.csv', index=False)#write data in csv file 
datan=pd.read_csv('weight.csv')
BirdWeight=datan.values.tolist()#generate list       
csv_file=open("kiwibirddatainfo.csv")    #打开文件  
csv_reader_lines = csv.reader(csv_file)    #用csv.reader读文件  
data_PyList=[]  
for one_line in csv_reader_lines:  
    data_PyList.append(one_line)    #逐行将读到的文件存入python的列表  
data_ndarray = np.array(data_PyList)    #将python列表转化为ndarray  
print (data_ndarray)    #试一下是否成功  

csv_file=open("KiwiBirdData.csv")    #打开文件  
csv_reader_lines = csv.reader(csv_file)    #用csv.reader读文件  
data_PyList=[]  
for one_line in csv_reader_lines:  
    data_PyList.append(one_line)    #逐行将读到的文件存入python的列表  
data_ndarray = np.array(data_PyList)    #将python列表转化为ndarray  
print (data_ndarray)    #试一下是否成功  

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