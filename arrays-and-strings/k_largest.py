"""
<aside>
💡 Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example 1:**

Input: nums = [3,2,1,5,6,4], k = 2

Output: 5

</aside>

"""

import heapq

def k_largest(arr,k):
    return heapq.nlargest(k, arr)[-1]

k = 2
arr = [3,2,1,5,6,4]
print(f'{k} largest element is {k_largest(arr, k)}')
