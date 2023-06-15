<aside>
💡 ********************Question 1********************

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with O(1) extra memory.

**Example 1:**

**Input:** s = ["h","e","l","l","o"]

**Output:** ["o","l","l","e","h"]

</aside>

Ans1:

```
def reverse_str(arr):
    i, j = 0, len(arr)-1

    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    return arr

nums = ["h","e","l","l","o"]
result = reverse_str(nums)
print(result)
```

<aside>
💡 ********************Question 2********************

Given a string s, *find the first non-repeating character in it and return its index*. If it does not exist, return -1.

**Example 1:**

**Input:** s = "leetcode"

**Output:** 0

</aside>

Ans2:

```
def first_non_repeating(str):
    word_freq = {}
    for i in str:
        word_freq[i] = word_freq.get(i,0) +1
    
    for i in range(len(str)):
        if word_freq[str[i]] == 1:
            return i
    return -1

str = "leetcode"
result = first_non_repeating(str)
print(result)
```

<aside>
💡 **************Question 3**************

Given a string s consisting of words and spaces, return *the length of the **last** word in the string.*

A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**

**Input:** s = "Hello World"

**Output:** 5

**Explanation:** The last word is "World" with length 5.

</aside>

Ans3:

```
def last_word(str):
    str.strip()
    count = len(str)-1
    result = ''
    while count != -1:
        if str[count] == ' ':
            break
        else:
            count -=1
    return len(str)-1-count

str = "Hello World"
result = last_word(str)
print(result)
```

<aside>
💡 ********************Question 4********************

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

**Example 1:**

**Input:** strs = ["flower","flow","flight"]

**Output:** "fl"

</aside>

Ans4:

```
def longest_common_prefix(arr):
    arr.sort(key = lambda a : len(a))
    common_prefix = arr[0]

    for i in range(1, len(arr)):
        word = arr[i]
        for j in range(len(common_prefix)):
            if common_prefix[j] == word[j]:
                continue
            else:
                common_prefix = common_prefix[0:j]
                break
    return common_prefix

strs = ["apple", "appricot", "application"]
result = longest_common_prefix(strs)
print(result)
```

<aside>
💡 ********************Question 5********************

Given a string s, find the length of the **longest substring** without repeating characters.

**Example 1:**

**Input:** s = "abcabcbb"

**Output:** 3

**Explanation:** The answer is "abc", with the length of 3.

</aside>

Ans5:

```
def longest_substring(str):
    index_hash = {}
    left = 0
    result = 0
    for j in range(len(str)):
        if str[j] in index_hash:
            left = max(index_hash[str[j]], left)
        index_hash[str[j]] = j+1
        result = max(result, j-left+1)
    return result

str = "abcabcbb"
result = longest_substring(str)
print(result)
```