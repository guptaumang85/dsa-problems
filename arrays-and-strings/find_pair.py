def find_pair(arr, sum):
    pivot = 0
    n = len(arr)
    for i in range(n-1):
        if arr[i+1] < arr[i]:
            pivot = i+1
            break
    l, r = pivot, pivot-1
    while l!=r:
        if arr[l] + arr[r] == sum:
            return True
        if arr[l] + arr[r] < sum:
            l  = (l+1)%n
        else:
            r = (r-1+n)%n
    return False

nums = [1,2,3,4,5]
result = find_pair(nums, 15)
print(result)
