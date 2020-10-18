# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:09:29 2020

@author: shaur
"""

import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = None

class Solution(object):
    def addTwoNumbers(self,l1: ListNode, l2: ListNode) -> ListNode:
        ext = ListNode(0) 
        # print(ListNode(0).val)
        current, carryover = ext, 0
        while l1 or l2:
            val = carryover
            if l1:
                val = val+l1.val
                l1 = l1.next
            if l2:
                val = val+ l2.val
                l2 = l2.next
            carryover= math.floor(val / 10)
            val=val % 10
            current.next = ListNode(val)
            current = current.next
        if carryover == 1:
            current.next = ListNode(1)
        return ext.next
    
# Main Function
if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    print("input1",a.val,"->", a.next.val,"->", a.next.next.val)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    print("input2",b.val,"->", b.next.val,"->", b.next.next.val)
    result = Solution().addTwoNumbers(a, b)
    print ("Output",result.val, "->", result.next.val, "->", result.next.next.val,"\n")
    
    
    a, a.next, a.next.next = ListNode(9), ListNode(9), ListNode(3)
    print("input1",a.val,"->", a.next.val,"->", a.next.next.val)
    b, b.next, b.next.next = ListNode(9), ListNode(9), ListNode(2)
    print("input2",b.val,"->", b.next.val,"->", b.next.next.val)
    result = Solution().addTwoNumbers(a, b)
    print ("Output",result.val, "->", result.next.val, "->", result.next.next.val,"\n")