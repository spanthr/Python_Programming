# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:39:05 2020

@author: shaur
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        long, first, flag= 0, 0, [False for _ in range(256)]
        for i, char in enumerate(s):
            
            
            if flag[ord(char)]:
                while char != s[first]:
                    
                    
                    flag[ord(s[first])] = False
                    first += 1
                first += 1
            else:
                flag[ord(char)] = True
            long = max(long, i - first + 1)
            
        return long

if __name__ == "__main__":
    print (" The longest substring in abcabcbb",Solution().lengthOfLongestSubstring("abcabcbbd"))
    print ("  The longest substring in abcdeff",Solution().lengthOfLongestSubstring("abcdeff"))