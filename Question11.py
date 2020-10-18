# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 01:32:39 2020

@author: shaur
"""
import numpy as np
# x = np.array([[0, 10, 20], [20, 30, 40]])
def find_indexof(x):
    print("Original array: ")
    print(x)
    print("\n")
    row,column=x.shape[0],x.shape[1]    
    list1=[]
    index1=[]
    
    for r in range(row):
        for c in range(column):
            if(x[r][c]>10):
                # print(x[r][c])
                # print(r,c)
                list1.append(x[r][c])
                index1.append([r,c])
                
    print(list1)
    print(index1)

x = np.array([[0, 10, 20], [20, 30, 40]])
    
x1 = np.array([[0, 10, 20], [20, 1, 40],[22, 0, 11]])
find_indexof(x)
print("\n")
find_indexof(x1)