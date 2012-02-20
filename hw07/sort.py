#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums
last = -1

N=len(nums)
for x in range(N):
    p=x
    for i in range(x+1,N):
        if nums[i] > nums[p]:
            p=i  

    if not (last == -1):
        t2 = nums[last]
        nums[last] = nums[p2]
        nums[p2] = t2
          
    t = nums[x]
    nums[x] = nums[p]
    nums[p] = t

print "After sort:"
print nums
