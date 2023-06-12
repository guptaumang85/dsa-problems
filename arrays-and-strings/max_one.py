def max_one(arr):
    total_max = 0
    current_max = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            total_max = max(total_max, current_max)
            current_max = 0
        else:
            current_max +=1
    total_max = max(total_max, current_max)
    return total_max

nums = []
result = max_one(nums)
print(result)
