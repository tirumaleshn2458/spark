#test_transform
from pyspark.pandas.spark import transform
from pyspark import pandas as pd
import warnings
warnings.filterwarnings('ignore')


from os import listdir

def testing_transform(path):
    def find_csv_filenames( path_to_dir, suffix=".csv" ):
        filenames = listdir(path_to_dir)
        return [ filename for filename in filenames if filename.endswith( suffix ) ]


    #path=''
    files_list=find_csv_filenames(path)


    def encoding(test_data):
        return transform.strd_to_numd(test_data)[0]

    def null_replace(test_data):
        return transform.fill_null_data(test_data)

    def mani(test_data):
        non_null_data=null_replace(test_data)
        return encoding(non_null_data)

    def test_case(file):
        print('------------------------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------------------------')
        print('File name:',file)
        print('-------------------------------------')
        test_data=pd.read_csv(path+file)
        test1=encoding(test_data)
        #test1.to_csv(path+'encoding'+'_'+file)
        del test1
        print('test 1 success')
        test2=null_replace(test_data)
        #test2.to_csv(path+'null_replace'+'_'+file)
        del test2
        print('test 2 success')
        test3=mani(test_data)
        #test3.to_csv(path+'mani_comb'+'_'+file)
        del test3
        print('test 3 success')


    for i in range(len(files_list)):
        file=files_list[i]
        try:
            test_case(file)
        except:
            print("Couldn't test for the file: ",file)


path_input=input('Enter the path: ')
testing_transform(path_input)
