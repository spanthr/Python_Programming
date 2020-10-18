
"""
Created on Sat Sep 26 12:59:27 2020

@author: shaur
"""
import time
ta=time.time()

def solution(list, num): 
    a=0 
    b=0 
    '''type in your solution, find a and b in array that a+b=num'''
    for i in list:
        a=i
        b=num-i
        if b in list:
            print('The numbers for the target',num,'are:')
            return a, b 
    print('No numbers found for the target',num)
  
numbers = [2,7,11,4] 
print(solution(numbers, 13))
print("\n") 
print(solution(numbers, 18))
print("\n") 
print(solution(numbers, 15)) 
print("\n")
print(solution(numbers, 0))   
tb=time.time()
print("Time taken:",tb-ta)