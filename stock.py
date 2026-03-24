# Best Time to Buy and Sell Stock [LeetCode - 121]

class Solution(object):
       
    def maxProfit(self):

        cheap = int()
        prices = [5, 10, 12, 19, 1]
        min = prices[0]
        for i in prices:
            if i < min:
                min = i
                cheap = min
            
            elif cheap == prices[-1]:
                cheap = 0
                print(cheap)
                break
            
            elif cheap < i:
                stocks = [i]
                buy_stock = max(stocks)
                profit = buy_stock - cheap
                print(profit)
                
                
                   
obj = Solution()
obj.maxProfit() 