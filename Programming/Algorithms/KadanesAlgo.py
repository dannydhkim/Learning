"""
Kadanes Algorithm:

Finds the maximum contiguous subarray

E.g. 
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

def maxSubArray(nums):
    currentMax = globalMax = nums[0]

    for i in range(1, len(nums)):
        print (i,":", nums[i])
        currentMax = max(nums[i], nums[i] + currentMax)
        print('newNum:', currentMax)
        globalMax = max(currentMax, globalMax)
        print('maxTotal:', globalMax)
    
    return globalMax

def main():
    # test1 =  [-2,1,-3,4,-1,2,1,-5,4]
    # print(maxSubArray(test1))

    test2 =  [15, -2, -1, -4, -2, -3, 13]
    print(maxSubArray(test2)) 

    # test3 =  [-2, -5, 6, -2, -3, 1, 5, -6]
    # print(maxSubArray(test3))

if __name__ == "__main__":
    main()