class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = float('-inf') #first buy
        s1 = 0 #first sell
        b2 = float('-inf') #second buy depends on first sell
        s2 = 0 # total result

        for price in prices:
            b1 = max(b1,-price) #first stock buying
            s1 = max(s1 , b1+price) # first sell price
            b2 = max(b2 , s1-price) #last sell subtractd with the current price
            s2 = max(s2 , b2+price) #final profit
        return s2