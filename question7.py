# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 01:57:57 2020

@author: shaur
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # No sub roots and the target is also 0
        if root is None:
            # sum=0 # Should return a boolean value
            return False
        else:
            # flag=0
            s_sum=sum-root.val
            if(s_sum==0 and root.right==None and root.left==None):
                return True
            return self.hasPathSum(root.left, s_sum) or self.hasPathSum(root.right, s_sum)
        
                
if __name__ == "__main__":                
    #            5
    #       4         8
    #   11         13      4
    # 7    2          1 
    # 
    root = TreeNode(5)  # Root
    root.left = TreeNode(4) 
    root.left.left = TreeNode(11) 
    root.left.left.left = TreeNode(7) 
    root.left.left.right =TreeNode(2)
    root.right = TreeNode(8) 
    root.right.right=TreeNode(4)
    root.right.left=TreeNode(13) 
    root.right.left.right=TreeNode(1)
    #  Result
    print ("For 22: Values of path are equal to sum?",Solution().hasPathSum(root, 22))  # Target is equal to root--> left,left,right
    print ("For 0: Values of path are equal to sum?",Solution().hasPathSum(root, 0))  
    print ("For 9: Values of path are equal to sum?",Solution().hasPathSum(root, 9))  # when target is met but sub root is not a leaf
    print ("For 27: Values of path are equal to sum?",Solution().hasPathSum(root, 27))   # Target is equal to root--> right,left,right
    print("\n")
    root1 = TreeNode()  # Root
    print ("For empty tree and sum=01: Values of path are equal?",Solution().hasPathSum(root1, 1))  # Empty binary tree