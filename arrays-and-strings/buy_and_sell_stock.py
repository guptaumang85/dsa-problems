"""
<aside>
💡 You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Example :**

Input: prices = [7,1,5,3,6,4]

Output: 5

</aside>
"""

def buy_and_sell_stock(arr):
    profit = 0
    min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i]< min_val:
            min_val = arr[i]
        if profit < (arr[i] - min_val):
            profit = arr[i] - min_val
    return profit

profit = buy_and_sell_stock([7,1,5,3,6,4])
print(f'total profit is {profit}')
