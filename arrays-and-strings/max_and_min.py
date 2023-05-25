"""
💡 Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

**Examples:**

Input: arr[] = {3, 5, 4, 1, 9}

Output: Minimum element is: 1

Maximum element is: 9
"""

def max_and_min(arr):
    max = arr[0]
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return [max, min]

max, min = max_and_min([1000, 11, 445, 1, 330, 3000])
print(f'max element is: {max}, and minimum element is {min}')
