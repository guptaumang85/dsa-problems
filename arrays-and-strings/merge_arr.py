def merge_arr(arr1, arr2, m, n):
    m -=1
    n-=1
    for i in range(len(arr1)-1, -1, -1):
        print(f'{arr1}, n = {n}, m = {m}')
        if m== -1:
            arr1[i] = arr2[n]
            n-=1
        elif n== -1:
            arr1[i] = arr1[m]
            m-=1
        elif arr1[m]> arr2[n]:
            arr1[i] = arr1[m]
            m -= 1
        else:
            arr1[i] = arr2[n]
            n-=1
    return arr1

num1 = [1,2,3,0,0,0]
num2 = [2,5,6]
result = merge_arr(num1, num2, 3, 3)
print(result)
