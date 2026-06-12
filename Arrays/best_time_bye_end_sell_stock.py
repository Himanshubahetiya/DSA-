prices = [7,1,5,3,6,4]

buy = 0
sell = 1
max_profit = 0

while sell < len(prices):
    if prices[sell] > prices[buy]:
        profit = prices[sell] - prices[buy]
        if max_profit < profit:
            max_profit = profit
    else:
        buy = sell
    sell += 1

print(max_profit)

