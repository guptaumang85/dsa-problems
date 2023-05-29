def merge_interval(arr):
    new_arr = []
    new_arr.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i][0] <= arr[i-1][1]:
            new_arr[i-1][1] = arr[i][1]
        else:
            new_arr.append([arr[i][0], arr[i][1]])
    return new_arr

nums = [[1,3],[2,6],[8,10],[15,18]]
result = merge_intervals(nums)
print(result)
