
''' QHEAP1
'''

hp=[0,]      # min-heap. Root starts at index 1. First element is kept dummy, for easy calculation of indices of child=2*index of parent
hp_ptr=0     # pointer to the last element in the heap

'''
 To rebuild a heap after adding a new element at the end 
'''
def heapify_up(x):
    global hp, hp_ptr
    
    cur_ptr=x                # element is compared to its parent
    while cur_ptr > 1:       # loop until the root is reached
        parent_ptr=cur_ptr
        parent_ptr >>= 1   # identify parent index as child index/2
        if hp[cur_ptr] < hp[parent_ptr]: # swap with parent if child < parent
            hp[cur_ptr],hp[parent_ptr]=hp[parent_ptr],hp[cur_ptr]
            cur_ptr=parent_ptr           # make parent position as current and repeat until root reached or child >= parent 
        else:
            return 0
    return 0
        
'''
 To rebuild a heap by moving current element down 
'''
def heapify_down(cur_ptr):
    global hp, hp_ptr
    
    child_ptr=cur_ptr
    child_ptr <<= 1                    # first child is at current index * 2
    while child_ptr <= hp_ptr:          # loop until leaf reached
        if hp[child_ptr] > hp[child_ptr+1]:
            child_ptr += 1             # identify minimum among children
        if hp[cur_ptr] > hp[child_ptr]: # if current > minimum child, swap positions
            hp[cur_ptr],hp[child_ptr]=hp[child_ptr],hp[cur_ptr]
            cur_ptr=child_ptr          # update current
            child_ptr <<= 1            # identify new child
        else:
            return 0
    return 0


'''
function to add an element to a min-heap
'''
def heapInsert(x):
    global hp, hp_ptr

    n=len(hp)
    hp_ptr += 1
    if n==1:
        hp.append(x)
    elif n>1:
        if hp_ptr < n:
            hp[hp_ptr]=x
        else:
            hp.append(x)
        heapify_up(hp_ptr)
    else:
        return -1
    return 0

'''
function to delete an element from the min-heap
Assumpton : no duplicate elements in heap
'''
def heapDelete(element):
    global hp, hp_ptr

    if hp[hp_ptr] == element:  # To delete last element from heap, just decrease the heap size
        hp_ptr -= 1
        return 0
    
    current_ptr=hp.index(element)  # get index of the element to delete
    if current_ptr <=0:            # element not present in heap
        return -1

    hp[current_ptr]=hp[hp_ptr]     # replace with the last element from heap
    hp_ptr -= 1                    # decrease heap size

    if current_ptr > 1:            # if not the root element, look up in the heap
        parent_ptr=current_ptr
        parent_ptr >>= 1           # identify parent index = current floor[index / 2]
    
        if hp[parent_ptr] > hp[current_ptr]:
            heapify_up(current_ptr)# if parent > current, adjust ancestors 
    heapify_down(current_ptr)      # else check and correct heap properties with descendants
    
    return 0

'''
function to print minimum heap element
'''
def printMin():
    global hp, hp_ptr

    if len(hp)>1:
        print(hp[1])
        return 0
    else:
        retuen -1
      

if __name__=='__main__':
    n=int(input())
    for i in range(n):
        q=input()
        try:
            q=int(q)
        except:
            q,e=q.split()
            q=int(q)
        if q==1:
            heapInsert(e)
        elif q==2:
            heapDelete(e)
        elif q==3:
            printMin()
        else:
            fprintf(stderr,"Invalid query")
