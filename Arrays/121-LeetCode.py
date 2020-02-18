class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''''
        if len(prices)<=1:
            
            return 0
        
        buyValue = prices[0]
        buyFlag = False
        buyIndex = 0
        sell = 0
        
        for i in range(len(prices)-1):

            if prices[i] < prices[i+1] and prices[i] <= buyValue:
                buyFlag = True
                buyValue = prices[i]
                buyIndex = i
        
        if buyFlag == True:
            
            for j in range(buyIndex+1,len(prices)):

                if prices[j] > buyValue and prices[j] > sell:

                    sell = prices[j]
        else:
            
            buyValue = 0
         
        return sell-buyValue
            '''
        max_profit, min_price = 0,float('inf')

        for price in prices:

                min_price = min(min_price,price)
                profit = price-min_price
                max_profit = max(max_profit,profit)
                
        return max_profit
            
        
        
        
        
        
            
            
            
        