#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#
''' 
Stack of buildings seen so far, starting from left, whose rectangle length is not yet decided (no building with height less than them, on their right is read so far)  
'''
st=[]
st_ptr=-1

'''
function to push an element from the global stack
'''
def push(element):
    global st,st_ptr

    st_ptr += 1
    if len(st)==st_ptr:    # if the stack pointer points to the last element, then append
        st.append(element)
    else:                  # otherwise insert into free space available
        st[st_ptr]=element
    
       
'''
function to pop an element from the global stack
'''
def pop():
    global st,st_ptr
    
    if st_ptr < 0:
        return -1
    else:
        st_ptr -= 1
        return st[st_ptr+1]

'''
function to peek at an element from the global stack
'''
def peek():
    global st,st_ptr
    if st_ptr < 0:
        return -1
    return st[st_ptr]
   
def largestRectangle(h):
    
    n=len(h)
    
    if min(h)== max(h):           # if all buildings are of same height, return the area
        return long(min(h)*n)

    h=[[0,x,n-1] for x in h]      # initialise left and right limit of each rectangle that can be drawn with that building's height, to start and end of the array 
    
    push(0)                       # add first building to the stack 
    
    for i in range(n-1):          # travel array sequentially to scan change of heights
        if h[i][1] < h[i+1][1]:   # if next building is higher 
            h[i+1][0] = i+1       # then a rectangle with height of next building can not have current building in it
        elif h[i][1] > h[i+1][1]: # if next building is lower
            while peek() >=0 and h[peek()][1]> h[i+1][1]: # right rectangle limit of all buildings on left, higher than next building, is the current building
                k=pop()
                h[k][2] = i
            k=peek()
            if h[k][1]== h[i+1][1]:
                h[i+1][0]=h[k][0]
            else:
                h[i+1][0]=k+1
        else:                     # if next building is of same height, then both buildings will always be part of the same rectangle
            h[i+1][0]=h[i][0]    
        push(i+1)                 # add next building to stack
        
 
    print(h)
    r=[(x[2]-x[0]+1)*x[1] for x in h]
    print(r)
    return max(r)
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
     
'''
if __name__ == '__main__':

    i1= 1000000
    i2= 900000
    h = [2,2,i1,i2,1,4,5]

    result = largestRectangle(h)

    print(str(result) + '\n')
