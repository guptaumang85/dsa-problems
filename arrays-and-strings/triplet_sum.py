"""
<aside>
💡 Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

**Example:**

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

</aside>
"""

def triplet_sum(arr):
    result = []
    sorted_arr = sorted(arr)
    for k in range(len(sorted_arr)):
        if sorted_arr[k-1] == sorted_arr[k]:
            continue
        if sorted_arr[k] > 0:
            break
        result = result + two_sum(k, sorted_arr)
    return result

def two_sum(k, sorted_arr):
    print(k)
    i = k+1
    j = len(sorted_arr)-1
    result = []
    while i!=j:
        if sorted_arr[i]+sorted_arr[j]+sorted_arr[k] == 0:
            result.append([sorted_arr[k], sorted_arr[i], sorted_arr[j]])
            j -= 1
        elif sorted_arr[i]+sorted_arr[j]+sorted_arr[k] > 0:
            j -= 1
        else:
            i += 1
    return result

result = triplet_sum([-1,0,1,2,-1,-4])
print(result)
