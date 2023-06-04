<aside>
💡 **Question 1**
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

**Example 1:**
Input: nums = [1,4,3,2]
Output: 4

**Explanation:** All possible pairings (ignoring the ordering of elements) are:

1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4
</aside>

Ans1:

```
def max_min_pair_sum(arr):
    sorted_arr = sorted(arr)
    sum = 0
    for i in range(0, len(sorted_arr), 2):
        sum += min(sorted_arr[i], sorted_arr[i+1])
    return sum

nums = [1,4,3,2]
result = max_min_pair_sum(nums)
print(result)
```

Question 2
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

Example 1:
Input: candyType = [1,1,2,2,3,3]
Output: 3

Ans2: 

```
def diff_candies(arr):
    candies_type = set()
    for i in arr:
        if i not in candies_type:
            candies_type.add(i)
    return(int(min(len(arr)/2, len(candies_type))))

nums = [1,1, 3, 4, 4, 5]
result = diff_candies(nums)
print(result)
```

Question 3
We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5

Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Ans3:

```
def findLHS(nums):
    freq = {}
    max_length = 0
    for i in nums:
        freq[i] = freq.get(i, 0) + 1
    
    for num in freq:
        if num+1 in freq:
            length = freq[num] + freq[num+1]
            max_length = max(length, max_length)
    return max_length

nums = [1, 3, 2, 2, 5, 2, 3, 7]  # Example input
result = findLHS(nums)
print(result)
```

Question 4
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Ans4:

```
def plant_flowerbed(arr, n):
    for i in range(0, len(arr)):
        if (arr[i] == 0 and (i==0 or arr[i-1] == 0) and 
            (i ==len(arr)-1 or arr[i+1]==0)):
            arr[i] = 1
            n-=1
        if n==0:
            return True
    return False


nums = [0, 0, 1, 0, 0, 1, 0, 0]  # Example input
result = plant_flowerbed(nums, 2)
print(result)
```

Question 5
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Ans5:

```
def max_product(arr):
    sorted_arr = sorted(arr)
    return max(sorted_arr[-1] * sorted_arr[-2] * sorted_arr[-3], sorted_arr[0] * sorted_arr[1] * sorted_arr[-1])

nums = [-1, -2, -3, -4]  # Example input
result = max_product(nums)
print(result)
```

Question 6
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Ans6:

```
def find_target(arr, target):
    l = arr[0]
    r = len(arr) - 1
    while l!=r:
        count = (l+r)//2
        if arr[count]==target:
            return(count)
        elif target > arr[count]:
            l = count + 1
        else:
            r = count - 1
    return(-1)


nums = [1, 3, 5, 7, 9]  # Example input
result = find_target(nums, 10)
print(result)
```

Question 7
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true

```
def is_monotonic(arr):
    inc_count = 0
    dec_count = 0
    for i in range(len(arr)-1):
        if arr[i+1] > arr[i]:
            inc_count += 1
        elif arr[i+1] < arr[i]:
            dec_count += 1
        else:
            inc_count += 1
            dec_count += 1
    if inc_count == len(arr) -1 or dec_count == len(arr) -1:
        return True
    else:
        return False



nums = [5, 5, 3, 2, 1]
result = is_monotonic(nums)
print(result)
```

Question 8
You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

Example 1:
Input: nums = [1], k = 0
Output: 0

Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

Ans8:

```
def minimum_score(arr,k):
    minimum = arr[0]
    maximum = arr[0]

    for i in arr:
        minimum = min(minimum, i)
        maximum = max(maximum, i)
    
    initial_diff = maximum - minimum

    for i in arr:
        minus_k = min(minimum, i-k)
        plus_k = max(maximum, i+k)
        new_score = plus_k - minus_k
        initial_diff = min(new_score, initial_diff)
    
    return initial_diff


nums = [1, 3, 5]
result = minimum_score(nums,2)
print(result)
```