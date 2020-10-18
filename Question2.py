# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:06:46 2020

@author: shaur
"""
import time
ta=time.time()

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def solution(root):
    if root is None:
        return 0
    else:
        Depthl=solution(root.left)
        Depthr=solution(root.right)
        depth=1+max(Depthl,Depthr)
    '''type in your solution'''
    return depth

a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20

print('The maximum depth is',solution(a3))

print("\n")  
tb=time.time()
print("Time taken:",tb-ta)