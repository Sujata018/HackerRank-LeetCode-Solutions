'''
    This program receives an input interegr array and a target integer, and returns
    the indices of the two integers from the array whose sum is same as the target.
    Inputs          : nums   -> an integer array with integers in range [-10^19 , 10^19]
                      target -> an integer in range [-10^19 , 10^19]
    Output          : a list with two indices.
    Assumption      : There is only one combination of integes whose sums is the target. 
'''
def twoSum(nums, target):
    '''
    Time Complexity  : O(n)
                      Search array sequentially O(n), look in dictionary O(1)
    Space complexity : O(n) - to store the dictionary of the element vs indices
    '''
    d={}
    ## Linear travel in array, if complement is present in dictionary, then ##
    ## return indices, or add to the dictionary and check next element      ##

    for i in range(len(nums)):
        n=target - nums[i]
        if n in d:
            return [i, d[n]]
        else:
            d[nums[i]]=i

def twoSum1(nums, target):
    '''
    Time Complexity  : O(n log n)
                       Sorting O(n log n), searching O(n)
    Space complexity : O(n) - to store indices
    '''
    nums=list(zip(nums,[i for i in range(len(nums))])) # zips array elements with indices
    nums=sorted(nums)                                  # sort on array elements

    ## Fix two pointers pt1 to start position and pt2 to end position ##
    ## of the array. pt1 travels forward, if sum of elements pointed  ##
    ## by pt1 and pt2 are less than target, pt2 moves backward if     ##
    ## sum is more than the target. Continues until the elements      ##
    ## found, or pt1 meets pt2.                                       ##
    i=0                                                # pt1
    j=len(nums)-1                                      # pt2
    while (i<j):                                       
            sumij=nums[i][0]+nums[j][0]
            if sumij==target:
                return [nums[i][1],nums[j][1]]         # return indices if sum matches target
            if sumij > target:
                j -= 1
            else:
                i += 1
    return -1                                          # return -1 if no pair found 

if __name__=='__main__':

    if twoSum([3,2,3],6) in ([0,2],[2,0]): print('ok')
    else: print('Error')
    if twoSum([1,3,2,5],5)in ([1,2],[2,1]): print('ok')
    else: print('Error in answer ',twoSum([1,3,2,5],5))
