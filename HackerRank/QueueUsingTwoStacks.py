#!/usr/bin/env python
# coding: utf-8

A=[]
tail=0

'''
Push function for the back stack , to enqueue
'''
def push(data):
    global A
    A.append(data)

'''
Pop function for the front stack to dequeue
'''
def pop():
    global tail
    tail += 1   

'''
Main function to accept inputs from stdin and do operations on the queue

Input: Line 1 -> n : an integer specifying the number of queries
       Line 2-n+1  : n lines each containing a query

       query line structure:
            1 x: Enqueue element  into the end of the queue.
            2: Dequeue the element at the front of the queue.
            3: Print the element at the front of the queue.

Logic: The requirement is to implement a queue using two stacks,
       and do push, pop, seek operations on the stack.

       Two stacks, occupying the same array elements are implemented, with
       head of stack 1 as the front of the queue, and head of stack 2 as the
       rear of the queue.
       Push in stack 2 represents enqueue operation
       Pop in stack 1 represents dequeue operation
       Seek at stack 1 represents print (option 3)
'''
if __name__=='__main__':
    global A,tail
    n=int(input())
    for i in range(n):
        q=input()
        qtype=int(q[0])
        if qtype== 1:
            A.append(q[2:])
        elif qtype == 2:
            pop()
        elif qtype == 3:
            print(A[tail])

