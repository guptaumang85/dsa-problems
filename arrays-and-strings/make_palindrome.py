def make_palindrome(arr):
    i = 0
    j = len(arr) - 1
    count = 0
    while i != j:
        if arr[i] == arr[j]:
            i+=1
            j-=1
        elif arr[i] > arr[j]:
            arr[j-1] = arr[j] + arr[j-1]
            j-=1
            count +=1
        else:
            arr[i+1] = arr[i]+arr[i+1]
            i+=1
            count +=1
    return count

nums = [11, 14, 15, 99]
result = make_palindrome(nums)
print(result)
