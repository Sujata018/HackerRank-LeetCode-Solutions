'''
Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
Calculate the sum of that subset.
'''
    
def maxSubsetSum(arr):                

    lenArr=len(arr)

    dp=[0 for _ in range(lenArr)]    # Dynamic array to store the maximum sum upto current index position af arr

    dp[0]=max(0,arr[0])              # Only one element in arr, return it
    if(1==lenArr):
        return dp[0]

    dp[1]=max(0,arr[1])              # Only two elements in arr, return maximum of them
    if(2==lenArr):
        return max(dp[0],dp[1])

    for i in range(2,lenArr):        # For each index, maximum is either the idx - 1 position max, or maximum between idx -2 position and sum of current element with idx-2 position
        dp[i]=max(dp[i-2],dp[i-1],dp[i-2]+arr[i])
    print(dp)

    return max(dp[lenArr-1],dp[lenArr-2])
   

if __name__ == '__main__':
    
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)
