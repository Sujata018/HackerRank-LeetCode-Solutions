import sys
import numpy as np
from itertools import combinations as cb

A=[]
qsets=[]
n=0
q=0
modl=19**9+7

def getPowersA():
    '''
    Calculate adjacency, adjacency^2,...,adjacency^n, and store minimum value of each position
    among all powers in A.
    This will help in getting lengths of paths between any two nodes of the graph.
    '''
    global A,n
    C=np.copy(A)
    B=A
    for i in range(n-2):
        B=np.dot(B,A)
        C=np.where((C==0) & (B!=0) ,i+2,C)
    A=C
    
def initialiseA():
    '''
    Initialises the adjacency matrix from use input
    '''
    global A,n

    A=np.zeros([n,n],dtype=int)   # Adjacency matrix initialise to 0, A is the list of Adjacency matrix, (Adjacency matrix)^2, (Adjacency matrix)^3 and so on 
    for _ in range(n-1):          # Build adjacency matrix 
        try:
            a,b=list(map(int,input().split()))
        except:
            sys.exit('Please enter integers only.')
        try:
            A[a-1,b-1]=A[b-1,a-1]=1
        except:
            sys.exit('Invalid node number, acceptable range : 1 - '+str(n))

    if n>2:   # Calculate paths of length >1, if more than 2 nodes are present 
        getPowersA()

def buildQsets():
    '''
    Build the sets of q nodes from user inout
    '''
    global qsets,q, n
    for _ in range(q):              # Build the sets
        try:
            k=int(input())
        except:
            sys.exit('Please enter a single integer.')
        try:
            qset= list(map(int,input().split()))
        except:
            sys.exit('Please enter integers only.')
        if max(qset)>n or min(qset)<1:
            sys.exit('Invalid node number, acceptable range : 1 - '+str(n))
        lq=len(qset)
        if lq!=k:
            sys.exit('Mismatch in length of the set provided : length given = '+str(k)+' but actual length = ', lq)
            
        qsets += [qset]

def calc(qset):
    '''
    Calculate sum(a.b.dist(a,b)) mod(10^9 + 7) for all a,b in qset
    '''
    global modl,A
    s=0
    
    ab=list(cb(qset,2))
    for a,b in ab:
       s += a*b*A[a-1,b-1]
       s %= modl
       
    return s

'''
This is the main function
'''
if __name__=='__main__':
    
    try:
        n,q=list(map(int,input().split()))
    except:
        sys.exit('Please enter integers only.')
    print("n=",n, " q=",q)
        
    initialiseA()        # initialise adjacency matrix
    buildQsets()         # build qsets
    
    for qset in qsets:   # for each set, calculate the sum
        print(calc(qset))
            
