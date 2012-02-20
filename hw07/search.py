#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

def sort(nums):
    last = -1

    N=len(nums)
    for x in range(N):
        p=x
        
        for i in range(x+1,N):
            if nums[i] < nums[p]:
                p=i  

        if not (last == -1):
            t2 = nums[last]
            nums[last] = nums[p2]
            nums[p2] = t2
              
        t = nums[x]
        nums[x] = nums[p]
        nums[p] = t

    return nums

nums=input_nums()
nums = sort(nums)
print "I have sorted your numbers"
print nums
x=raw_input("Which number should I find: ")
x = int(x)
m=0
M=len(nums) - 1
found = 0

while M>=m:
    md=(M+m)/2
    if (nums[md] == x):
       found = 1
    elif (nums[md] < x):
       m=md+1
    else:
       M=md-1

    if found == 1:
        break
    
if nums[md] == x:
    print "Found", x, "at", md
else:
    print "Could not find", x
