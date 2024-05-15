def maxProfit(self, prices: list[int]) -> int:

    p1 = 0
    p2 = 0
    max_profit = 0

    while p2!=len(prices):

        if prices[p2]>= prices[p1]:
            current_profit = prices[p2]-prices[p1]
            max_profit = max(max_profit, current_profit)
            p2 += 1
        else:
            p1 = p2
    
    return max_profit