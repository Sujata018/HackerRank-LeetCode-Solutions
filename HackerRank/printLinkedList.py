def printLinkedList(llist):
    for item in llist:
        print(item)

if __name__=='__main__':
    n=int(input())
    llist=[]
    for _ in range(n):
        llist.append(int(input()))

    printLinkedList(llist)
