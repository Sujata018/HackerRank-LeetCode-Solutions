import sys

def obtainMin(L,d,t):
    '''
    Given a list of integers, a division parameter, and a threshold,
    calculate the number of minimum steps required to obtain an array
    with atleast threshold number of equal elements, where each step will divide
    one of the elements of the array by the division parameter.
    '''
    n=len(L)
    if n < t:
        sys.exit("List of numbers"+str(n)+" is smaller than threshol"+str(t))

    A=[[] for _ in range(max(L)+1)] # Array to store number of steps from each elements of L to obtain the A[i] 
    for i in L:
        c=0             # number of steps
        A[i] += [0]     # initial number is otained by step 0
        while i > 0:
            c += 1
            i //= d
            A[i] += [c]

    mins=sum(A[0])     # minimum number of steps

    for i in range(len(A)):
        if len(A[i]) >= t:  # if atleast threshold number of elements are reduced to A[i]
            A[i].sort()     # sort A[i] in ascending order and take the least k steps
            mins=min(mins,sum(A[i][:t]))

    return mins

if __name__=='__main__':
    if len(sys.argv)<=1:
        sys.exit("Usage "+sys.argv[0]+" <list>")
    try:
        L=list(map(int,sys.argv[1:]))
    except:
        sys.exit("All list elements should be integers")
    print("L=",L)
    try:
        d,t=list(map(int,input("Enter divisor and threshold: ").split()))
    except:
        sys.exit("Enter integers for divisor and threshold")
        
    print(obtainMin(L,d,t))
    
            
            
    
