def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price  # Found new minimum
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit  # Found better profit

    return max_profit

# Example test cases
print(maxProfit([7, 10, 1, 3, 6, 9, 2]))  # Output: 8
print(maxProfit([7, 6, 4, 3, 1]))         # Output: 0
print(maxProfit([1, 3, 6, 9, 11]))        # Output: 10
