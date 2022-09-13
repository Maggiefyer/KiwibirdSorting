#test_kiwibird_BubbleSortModule_test
from kiwibird_BubbleSortModule_test import bubblesort
from kiwibird_BubbleSortModule_test import BirdWeight
from time import *
import timeit
import time
import  csv
import pandas as pd 
import pytest

averagecase = BirdWeight
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
    print("test_BubbleBest")
    time.sleep(1.0)

def test_02(set_up_fixture):
    print("BubbleWorst")
    time.sleep(0.6)

def test_03(set_up_fixture):
    print("test_BubbleAverage")
    time.sleep(1.2)
    
def test_BubbleWorst():
    bubblesort(worstcase)
    assert BirdWeight== bestcase     
     
def test_BubbleBest():
     bubblesort(bestcase)
     assert BirdWeight== bestcase   
       
def test_BubbleAverage():  
     bubblesort(averagecase) 
     assert BirdWeight== bestcase
    

