import time 
from insertSort_test import lst
from insertSort_test import insertSort
import pytest

averagecase = lst
#print(averagecase)
bestcase = sorted(averagecase)
#print(bestcase)
worstcase = sorted(averagecase, reverse = True)
#print(worstcase)
@pytest.fixture()
def set_up_fixture():
    time.sleep(0.1)
    yield
    time.sleep(0.2)

def test_01(set_up_fixture):
    print("test_insertBest")
    time.sleep(1.0)

def test_02(set_up_fixture):
    print("test_insertWorst")
    time.sleep(0.6)

def test_03(set_up_fixture):
    print("test_insertAverage")
    time.sleep(1.2)
    
def test_insertWorst():
    startTime=time.perf_counter()      
    assert insertSort(worstcase)== bestcase 
    elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
    print ("The time of sorting process used is:", elapsed)    
     
def test_insertBest():
     start=time.time()     
     assert insertSort(bestcase)== bestcase   
     print(time.time()-start)
     
def test_insertAverage():
     start=time.time()  
     assert insertSort(averagecase) == bestcase
     print(time.time()-start)