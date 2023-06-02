def majority_elem(arr):
    elem_freq = {}
    for i in arr:
        if i in elem_freq:
            elem_freq[i] += 1
        else:
            elem_freq[i] = 1
    for key in elem_freq:
        if elem_freq[key] > len(arr)//2:
            return key

nums = [0, 1,1,1, 2]
result = majority_elem(nums)
print(result)
