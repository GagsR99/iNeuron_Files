## FUNCTION DEFINITION
def findmaxProfit(price):
    minPrice = float('inf')
    maxProfit = 0

    for i in range(len(price)):
        if price[i] < minPrice:
            minPrice = price[i]
        elif price[i] - minPrice > maxProfit:
            maxProfit = price[i] - minPrice
    return maxProfit


## Driver Code
price = [7,8,5,2,16,20]
maxProfit_value = findmaxProfit(price)
print(maxProfit_value)



