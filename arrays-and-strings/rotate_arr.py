def rotate_arr(arr, k):
    n = len(arr)
    k = k%n
    reverse(arr,0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    return arr

def reverse(arr, start, end):
    i, j = start, end
    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1

nums =  [1, 2, 3, 4, 5]
result = rotate_arr(nums, 7)
print(result)
