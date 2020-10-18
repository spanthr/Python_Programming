# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 01:29:25 2020

@author: shaur
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists( lists) -> ListNode:
        def mergeTwoLists(list1, list2):
            current = duplicate = ListNode(0)
            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            current.next = list1 or list2
            return duplicate.next

        if not lists:
            return None
        left, right = 0, len(lists) - 1;
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]
        
        
        
        
if __name__ == '__main__':
    list1,list1.next,list1.next.next = ListNode(1),ListNode(4),ListNode(5)
    list2,list2.next,list2.next.next = ListNode(1),ListNode(3),ListNode(4)
    
    list3,list3.next=ListNode(2),ListNode(6)
    
    List=ListNode()
    # List=[list1,list2]
    List=[list1,list2,list3]   #uncomment to do for 3 lists
    print("First List",list1.val,list1.next.val,list1.next.next.val)
    print("second List",list2.val,list2.next.val,list2.next.next.val)
    print("Third List",list3.val,list3.next.val)
    new=(Solution.mergeKLists(List))
    
    print("Solution:",new.val,new.next.val,new.next.next.val,new.next.next.next.val,new.next.next.next.next.val,new.next.next.next.next.next.val,new.next.next.next.next.next.next.val,new.next.next.next.next.next.next.next.val)
    # print(new.val)
    # Another solution
    list1,list1.next,list1.next.next = ListNode(1),ListNode(1),ListNode(2)
    list2,list2.next,list2.next.next = ListNode(2),ListNode(3),ListNode(5)
    list3,list3.next=ListNode(3),ListNode(6)
    List=ListNode()
    # List=[list1,list2]
    List=[list1,list2,list3]   #uncomment to do for 3 lists
    print("First List",list1.val,list1.next.val,list1.next.next.val)
    print("second List",list2.val,list2.next.val,list2.next.next.val)
    print("Third List",list3.val,list3.next.val)
    new=(Solution.mergeKLists(List))
    
    print("Solution:",new.val,new.next.val,new.next.next.val,new.next.next.next.val,new.next.next.next.next.val,new.next.next.next.next.next.val,new.next.next.next.next.next.next.val,new.next.next.next.next.next.next.next.val)