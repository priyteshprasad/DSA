#  Python program finding subarray with max sum
# Kaden's Algorithm

def maxSumSubArray(arr):
    maxSum = -999999
    currSum = 0

    for i in range(len(arr)):
        currSum = currSum + arr[i]
        if currSum > maxSum:
            # we check if the current sum is greater then maxSum till no,
            # means we have find a new sub array with max sum
            maxSum = currSum
        if currSum < 0:
            # there is no point of adding the sum of subarray if its sum is negative
            currSum = 0
    return maxSum


def minSumSubArry(arr=[]):
    currSum = 0
    minSum = 9999999
    for i in range(len(arr)):
        currSum += arr[i]

        if currSum < minSum:
            minSum = currSum
        if currSum > 0:
            currSum = 0

    return minSum


print(minSumSubArry([-5, -7, -45, -44, -8, 10000]))
print(maxSumSubArray([-5, -7, -45, -44, -88]))
