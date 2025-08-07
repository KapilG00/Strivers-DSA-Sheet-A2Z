from typing import List


# TC -> O(n^2)
# SC -> O(1)
def max_profit_buy_sell_stock(arr: List[int]) -> int:
    n = len(arr)
    max_profit = float('-inf')

    for i in range(n):
        for j in range(i+1, n):
            current_profit = arr[j] - arr[i]
            if current_profit > max_profit:
                max_profit = current_profit
    if max_profit < 0:
        max_profit = 0

    return max_profit            

# TC -> O(n)
# SC -> O(1)
def max_profit_buy_sell_stock(arr: List[int]) -> int:
    n = len(arr)
    max_profit = float('-inf')
    min_price = float('inf')

    for i in range(n):
        min_price = min(min_price, arr[i])
        max_profit = max(max_profit, arr[i] - min_price)
    return max_profit



if __name__ == "__main__":
    print(max_profit_buy_sell_stock([7,1,5,3,6,4]))
    print(max_profit_buy_sell_stock([7,6,4,3,1]))