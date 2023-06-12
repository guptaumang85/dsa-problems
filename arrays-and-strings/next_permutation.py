def next_permutation(arr):
    count = len(arr) - 1
    while count !=0:
        if arr[-1]> arr[count-1]:
            arr[-1], arr[count-1] = arr[count-1]. arr[-1]
            break
        count -=1
    reverse(arr, count)
    return arr

def reverse(arr, start):
    i, j = start, len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


nums = [3,2,1]
result = next_permutation(nums)
print(result)
