from pyspark.pandas import transform
from pyspark import pandas as pd
import warnings
import os
warnings.filterwarnings('ignore')
from pydataset import data
datasets=data

def encoding(test_data):
    return transform.strd_to_numd(test_data)[0]

def null_replace(test_data):
    return transform.fill_null_data(test_data)

def mani(test_data):
    non_null_data=null_replace(test_data)
    return encoding(non_null_data)

try:
    os.mkdir('test_case_output_for_transform')
except:
    pass

cwd=os.getcwd()
def test_case(data,name):
    print('------------------------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------------------------')
    print('Dataset name:',name)
    print('-------------------------------------')
    test_data=data
    test1=encoding(test_data)

    del test1
    print('test 1 success')
    test2=null_replace(test_data)

    del test2
    print('test 2 success')
    test3=mani(test_data)

    del test3
    print('test 3 success')

for dataset in datasets()['dataset_id']:
    test_case(datasets(dataset),dataset)
