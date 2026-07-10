from typing import List


# TC -> O(n^2)
# SC -> O(1)
def max_profit_buy_sell_stock(arr: List[int]) -> int:
    n = len(arr)
    max_profit = 0

    for i in range(n):
        for j in range(i+1, n):
            current_profit = arr[j] - arr[i]
            max_profit = max(max_profit, current_profit)

    return max_profit            

# TC -> O(n)
# SC -> O(1)
def max_profit_buy_sell_stock(arr: List[int]) -> int:
    """
    The idea is to track the minimum price so far while traversing the array and calculate the profit if we sold today. 
    This way, we can constantly update the maximum profit without using nested loops.
    """
    n = len(arr)
    max_profit = 0
    min_price = float('inf')

    for i in range(n):
        min_price = min(min_price, arr[i])
        max_profit = max(max_profit, arr[i] - min_price)
    return max_profit



if __name__ == "__main__":
    print(max_profit_buy_sell_stock([7,1,5,3,6,4]))
    print(max_profit_buy_sell_stock([7,6,4,3,1]))