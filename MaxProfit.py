class MaxProfit:

    def maxProfit(self, prices):
        if len(prices) > 1:
            min_price = prices.pop(0)
            max_profit = 0
            for i in prices:
                price = i - min_price
                if i < min_price:
                    min_price = i
                else:
                    if price > max_profit:
                        max_profit = price
            return max_profit
        else:
            return 0
