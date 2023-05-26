<aside>
💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

</aside>

Ans1: 
```
def two_sum(arr, target):
    hash_data = {}

    for i in range(len(arr)):
        if arr[i] in hash_data:
            return [i, hash_data[arr[i]]]
        else:
            hash_data[target-arr[i]] = i
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
```

<aside>
💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

</aside>
Ans2:

```
def array_count(nums, val):
    new_arr = []
    for i in nums:
        if i == val:
            continue
        else:
            new_arr.append(i)
    return len(new_arr)

nums = [3,2,2,3]
target = 3
result = array_count(nums, target)
print(result)

```

<aside>
💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2

</aside>
Ans3:

```
def array_count(nums, val):
    i = len(nums)//2
    while i < len(nums):
        if val == nums[i] or i==0 or nums[i-1] < val < nums[i]:
            return i
        elif val > nums[i]:
            i = i+1
        else:
            i = i-1
    return len(nums)


nums = [1,3,5,9, 11,13]
target = 15
result = array_count(nums, target)
print(result)
```

<aside>
💡 **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

</aside>
Ans4:

```
def get_increment(arr):
    arr[len(arr)-1] = arr[len(arr)-1] + 1
    return arr

nums = [1,2,3]
result = get_increment(nums)
print(result)
```

<aside>
💡 **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**Example 1:**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

</aside>
Ans5:

```
def merge_arr(nums1, nums2, m, n):
    for i in range(len(nums1)-1, -1, -1):
        if m == -1:
            nums1[0:i+1] = nums2[0:n+1]
            break
        elif n==-1:
            break
        elif nums1[m] > nums2[n]:
            nums1[i] = nums1[m]
            m -=1
        else:
            nums1[i] = nums2[n]
            n -= 1
            
    return nums1

nums1 = [2,5,7,0,0,0,0]
nums2 = [5,6,7,13]
m = 3
n = 4
result = merge_arr(nums1, nums2, m-1, n-1)
print(result)
```

<aside>
💡 **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true

</aside>
Ans6:

```
def is_dup(arr):
    arr_freq = {}
    for i in arr:
        if i in arr_freq:
            return True
        else:
            arr_freq[i] = 1
    return False

nums = [1,2,3,1]
result = is_dup(nums)
print(result)
```

<aside>
💡 **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

</aside>
Ans7:

```
def adjust_arr(arr):
    last_non_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[last_non_zero] = arr[i]
            last_non_zero +=1

    for i in range(last_non_zero, len(arr)):
        arr[i] = 0
    return arr

nums = [0,1,0,3,12]
result = adjust_arr(nums)
print(result)
```

<aside>
💡 **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]

</aside>
Ans8:

```
def findErrorNums(nums):
    n = len(nums)
    nums_arr = []
    duplicate = -1
    missing = -1

    for num in nums:
        if num in nums_arr:
            duplicate = num
        nums_arr.append(num)

    for i in range(1, n + 1):
        if i not in nums_arr:
            missing = i
            break

    return [duplicate, missing]


nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)
```