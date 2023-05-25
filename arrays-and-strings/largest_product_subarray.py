def largest_product_subarray(arr):
    max_till_now = arr[0]
    min_till_now = arr[0]
    result = arr[0]
    for i in range(1, len(arr)):
        temp_max = max(max_till_now*arr[i], min_till_now*arr[i], arr[i])
        min_till_now = min(max_till_now*arr[i], min_till_now*arr[i], arr[i])
        max_till_now = temp_max
        if max_till_now > result:
            result = max_till_now
    return result

result = largest_product_subarray([2,3,-2,4])
print(f'Maximuml product of subarray is {result}')
                           