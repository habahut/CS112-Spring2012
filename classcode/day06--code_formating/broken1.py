#!/usr/bin/env python

inputList = []
inputNumber = None

#get list of numbers
while inputNumber != "":
    inputNumber=raw_input()
    if inputNumber.isdigit():
        inputList.append(float(inputNumber))



total = 0

#sum up the list of numbers
for num in inputList:
    total += num


print total/len(inputList)        #calculates average of the list
