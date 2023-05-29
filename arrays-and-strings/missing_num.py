def missing_num(arr):
    arr_hash = {}
    for i in arr:
        arr_hash[i] = 1
    
    for i in range(len(arr)):
        if i not in arr_hash:
            return i
    return -1

nums = [4,0,1,2]
result = missing_num(nums)
print(result)
