import time 
from selectionSort_test import list
from selectionSort_test import selectionSort
import pytest
import unittest
import time
from unittest import TextTestResult as _TestTestResult, TextTestRunner as _TextTestRunner

class CTextTestResult(_TestTestResult):
    
 def __init__(self,*args, **kwargs):
    super(CTextTestResult,self).__init__(*args, **kwargs)
    self.times = [] # 用于记录测试时间  

averagecase = list
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
    print("test_selectBest")
    time.sleep(1.0)

def test_02(set_up_fixture):
    print("test_selectWorst")
    time.sleep(0.6)

def test_03(set_up_fixture):
    print("test_selectAverage")
    time.sleep(1.2)
    
def startTest(self, test: unittest.case.TestCase) -> None:
    # 测试开始执行之前调用
    self.start_time = time.time() 
    super(CTextTestResult,self).startTest(test) 
    
def test_selectWorst():   
    startTime=time.perf_counter()      
    assert selectionSort(worstcase)== bestcase 
    elapsed=(time.perf_counter())-startTime #ReturnTimeConsumed
    print ("The time of sorting process used is:", elapsed)  
      
def addSuccess(self, test: unittest.case.TestCase) -> None:
    # 测试完成时调用
    total_time = time.time() - self.start_time
    test_name = self.getDescription(test)
    self.times.append((test_name,total_time))
    super(CTextTestResult,self).addSuccess(test)  
    
def startTest(self, test: unittest.case.TestCase) -> None:
    # 测试开始执行之前调用
    self.start_time = time.time() 
    super(CTextTestResult,self).startTest(test)        
def test_selectBest():
     start=time.time()     
     assert selectionSort(bestcase)== bestcase   
     print(time.time()-start)
def addSuccess(self, test: unittest.case.TestCase) -> None:
    # 测试完成时调用
    total_time = time.time() - self.start_time
    test_name = self.getDescription(test)
    self.times.append((test_name,total_time))
    super(CTextTestResult,self).addSuccess(test)
    
def startTest(self, test: unittest.case.TestCase) -> None:
    # 测试开始执行之前调用
    self.start_time = time.time() 
    super(CTextTestResult,self).startTest(test)          
def test_selectAverage():
     start=time.time()     
     selectionSort(averagecase) 
     assert list== bestcase
     print(time.time()-start)
def addSuccess(self, test: unittest.case.TestCase) -> None:
    # 测试完成时调用
    total_time = time.time() - self.start_time
    test_name = self.getDescription(test)
    self.times.append((test_name,total_time))
    super(CTextTestResult,self).addSuccess(test)
            
def getTestTimeing(self):
    # 返回记录的所有用例的时间
    return self.times
class CTextTestRunner(_TextTestRunner):
    def run(self, test):
        result = super(CTextTestRunner,self).run(test)
        for test_name, total_time in result.getTestTimeing():
            print("({:.10}s) {}".format(format(total_time, 'f'), test_name))
        return result
