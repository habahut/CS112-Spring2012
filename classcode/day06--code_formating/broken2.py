#!/usr/bin/env python
from random import randint

s=1
numberOfNumbers =int(raw_input())

randNums=[]

for _ in range(numberOfNumbers):
    randNums.append(randint(0,20))

print randNums


while s:
    s=0
    for i in range(1, numberOfNumbers):
        if randNums[i-1] > randNums[i]:
            temp1 = randNums[i-1]
            temp2 = randNums[i]
            
            randNums[i-1] = temp2
            randNums[i] = temp1
            s=1
        #end
        i += 1
    #end

print randNums
