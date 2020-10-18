# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 00:36:26 2020

@author: shaur
"""

class Subarray(object):
    def maxSubArray(self, nums):
        
        if max(nums) < 0:
            return max(nums)
        n=len(nums)
        # print(n)
        
        overall, current = float("-inf"), 0
        
        for i in range(n):
            current=current + nums[i]
            overall=max(overall,current)
            if(current<0):
                current=0
        return overall
            


if __name__ == "__main__":
    print(([-2,1,-3,4,-1,2,1,-5,4]))
    print("Maximum of continous subarray is:")
    print(Subarray().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print("\n")
    
    print([-2,1,-8,3,-3,-1,11,3,-4,11,-6])
    print("Maximum of continous subarray is:")
    print(Subarray().maxSubArray([-2,1,-8,3,-3,-1,11,3,-4,11,-6]))