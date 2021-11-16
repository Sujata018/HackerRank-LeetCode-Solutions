from math import log

maxBits=0
class node:
    '''
    A node with a left and right child.
    BitValue is either 0 or 1
    numval contains an integer, in case this is the end node of a number saved as a bit trie.
    '''
    def __init__(self,val):
        self.left = None
        self.right = None
        self.bitvalue = val
        self.numval=None

class trie:
    '''
    Trie structure to store numbers based on binary bits.
    '''
    def __init__(self):
        '''
        Initialise a trie with null bit
        '''
        self.head=node(None)
        
    def insert(self,num):
        '''
        inserts binary bits of a number in the trie. All elements added to the
        trie should have same height, for ease of search. So the number of bits
        for thw maximum number (maxBits) is used as the height of the trie.
        '''
        global maxBits                       # Height of the trie
        if type(num) == int:                 # store in trie if a valid number
            curNode=self.head
            bitRem=num                       # Remaining bits of the num is stored in bitRem
            for b in range(maxBits-1,-1,-1): # Check from the MSB to LSB
                bit= bitRem // 2**b          # current bit
                bitRem %= (2**b)             # remaining bit string
                if bit == 0:                 # add bit 0 to left child
                    if curNode.left is None: # if the left child does not exist, create it
                        n=node(bit)
                        curNode.left=n
                    curNode = curNode.left   # move to the left child
                else:                        # add bit 1 to right child
                    if curNode.right is None:# if the right child does not exist, create it
                        n=node(bit) 
                        curNode.right=n
                    curNode=curNode.right    # move to right child
            curNode.numval=num
        return self
            
    def search(self,q):
        '''
        Search for the element from trie, for which Xor(q,element) is maximum.
        '''
        global maxBits                       # height of the trie
        maxQBits=1+int(log(q,2))             # number of bits in the query integer
        if maxQBits > maxBits:               # if the number of bits in the query integer > max number of bits in trie
            q = q % (2**maxBits)             #    truncate till the last maxBits digits, because Xor with more significant digits will be the same for all elements in the trie 
        curNode=self.head                    # start with the root of the trie
        for b in range(maxBits-1,-1,-1):     # get the MSB of q, travel towards LSB
            bit = q // 2**b
            q %= (2**b)
            if bit == 1 and curNode.left is not None: # if current bit of q is 0, travel in trie to 1, and vice versa (so Xor is 1) 
                curNode=curNode.left
            elif bit == 1 and curNode.left is None:
                curNode=curNode.right        # if current bit of q is 1, travel in trie to 1, only if 0 branch is not present
            elif bit == 0 and curNode.right is not None:
                curNode=curNode.right
            else:
                curNode=curNode.left         # if current bit of q is 0, travel in trie to 0, only if 1 branch is not present

        return curNode.numval                # Travelling this way, the number is found in trie for which Xor is maximum with q
        
def maxXor(arr, queries):
    '''
    Given ar array of positive integers and a list of queries (>=0), this function
    returns the list of maximum Xor values between the queries and the array elements.
    '''
    global maxBits
    maxBits=1+int(log(max(arr),2))          # Calculate number of bots for the maximum element in the array.
    
    t = trie()                              # Define a null trie
    
    for a in arr:                           # Insert binary strings of each array element to the trie
        t=t.insert(a)
    
    result=[]                               # List of maximum Xors
    for q in queries:                       # Check max XOR for each queries
        if q ==0:
            EleMAxXor=max(arr)              # if query = 0, then max XOR will simply be the XOR with the maximum element in the array
        else:
            EleMAxXor=t.search(q)           # Find the element from trie, which has max XOR with the query
        result.append(q^EleMAxXor)          # add the Xor to the output list

    return result

if __name__=='__main__':
    print(maxXor([1,2,4,5,7],[0]))
