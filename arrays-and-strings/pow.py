def next_permutation(arr):
    if n==0:
        return 1
    if n<0:
        n = -n
        x = 1/x
    if n%2==0:
        return pow(x*x, n//2)
    else:
        return x*pow(x*x, n//2)


nums = [1, 3, 5]
result = pow(2,-1)
print(result)
