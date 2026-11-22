# Sliding Window pattern
# Two-pointer pattern
# fast & slow pointer pattern
# Merger interval pattern
# cyclic sort pattern
# in-place reversa of linked list pattern
# tree breadth-first search pattern
# Depth-first search DFS pattern
# two heap pattern
# subsets pattern
# Modified binary search pattern
# Bitwise Xor patter
# Top k elements pattern
#  kway merge pattern
# 0/1 knapsack DP pattern
# Topological sort Graph pattern

def max_subarraySum(nums,k):
    windowSum = sum(nums[:k])
    maxSum = windowSum

    for i in range(k, len(nums)):
        windowSum += nums[i] - nums[i - k]
        maxSum = max(maxSum, windowSum)
    return maxSum

print(max_subarraySum([2, 1, 5, 1, 3, 2], 3))
