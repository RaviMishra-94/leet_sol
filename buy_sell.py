class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sorted_list = sorted(prices, reverse=True)
       
        sell = max(prices)
        buy = min(prices)
        sell_index = prices.index(sell)
        buy_index = prices.index(buy)
        print(prices)
        print(sorted_list)
        print(buy, sell)
        print(buy_index, sell_index)
        if prices == sorted_list:
            return 0 
        elif sell_index > buy_index:
            profit = sell - buy
            return profit
        else:
            while sell_index <= buy_index:
                sell_index = sell_index + 1
                sell = sorted_list[sell_index]
                print(sell)
                print(buy)
                profit = sell - buy
                return profit
                break
 

prices = [2,4,1]      
sol_inst = Solution()
answer = sol_inst.maxProfit(prices)
print(answer)