import heapq

def k_smallest(k, arr):
    return heapq.nsmallest(k, arr)[-1]

k = 2
arr = [3,2,1,5,6,4]
print(f'{k} smallest element is {k_smallest(k, arr)}')
