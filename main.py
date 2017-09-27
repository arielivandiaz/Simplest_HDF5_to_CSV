#!/usr/bin/env python

__author__ = "Ariel Ivan Diaz"
__copyright__ = "Copyright 2017"

__license__ = "GPL"
__version__ = "1.0"
__email__ = "arielivandiaz@gmail.com"



import h5py
import pandas as panda
import tables
import os
import csv 
import numpy as np
import matplotlib.pyplot as plt

#/*********************************************************************************************    

def csv_to_matrix(file):

    file= file + '.csv'
   
    output = np.array(list(csv.reader(open(file, "rb"), delimiter="\t")))
    
    return output

#/*********************************************************************************************    

def matrix_to_csv(file, matrix):

    file = file +'.csv'

    df=panda.DataFrame(matrix)

    df.to_csv(file, sep='\t', encoding='utf-8', index=False,header=False)


#/*********************************************************************************************    

def create_random_csv(rows,cols,file):
    
    size=cols*rows

    
    data_frame = panda.DataFrame(np.random.rand(rows,cols))

    file = file + '.csv'
    

    data_frame.to_csv(file, sep='\t', encoding='utf-8', index=False, header=False)

#/*********************************************************************************************    


def matrix_to_h5(matrix, file):


    output=file+ '.hdf5'


    h5file = tables.open_file(output, "w", driver="H5FD_CORE")
   
    a = h5file.create_array(h5file.root, file, matrix)
    h5file.close()


#/*********************************************************************************************

def h5_to_matrix(file,value):

    file = file +'.hdf5'

    h5f = h5py.File(file,'r')
    b = h5f[value][:]
    
    h5f.close()


#/*********************************************************************************************
        


if __name__ == '__main__':


    file_name_in= 'test_in_test'
    file_name_out='test_out_test'

    ROWS=120
    COLS=32

    print '1- Create a random matrix %d ROWS x %d COLS', ROWS, COLS

    create_random_csv(ROWS,COLS,file_name_in)

    print '2- Read the CSV like a matrix'

    matrix =  csv_to_matrix(file_name_in)

    print '3- Write the matrix in a CSV'

    matrix_to_csv(file_name_out,matrix)

    print '4- Write the matrix in a HDF5'

    matrix_to_h5(matrix,file_name_out)

    print '5- Read the HDF5 file like a matrix'

    matrix_2=h5_to_matrix(file_name_out,file_name_out)

    print 'THE END'



