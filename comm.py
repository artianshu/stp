lockPrice=45.0
stockPrice=30.0
barrelsPrice=25.0
totalBarrels = 0
totalStocks = 0
totalBarrels = 0
totalLocks=0
locks=int(input("Enter value of locks:"))
while not locks==-1:
    stocks=int(input("Enter value of Stocks:"))
    barrels=int(input("Enter value of Barrels:"))
    totalLocks =  totalLocks+locks
    totalStocks = totalStocks+stocks
    totalBarrels = totalBarrels + barrels
    locks = int(input("Enter value of locks:"))
print("Locks Sold:",totalLocks)
print("Stocks Sold:",totalStocks)
print("Barrels Sold:",totalBarrels)
lockSales = lockPrice * totalLocks
stockSales = stockPrice * totalStocks
stockSales = stockPrice * totalStocks
barrelsSales = barrelsPrice * totalBarrels
sales = lockSales + stockSales + barrelsSales
print("Total Sales:",sales)
if sales > 1800.0 :
    commission = 0.10 * 1000.0
    commission = commission + 0.15*800.0
    commission = commission + 0.20*(sales-1800.0)
elif sales >1000.0:
    commission = 0.100*1000.0
    commission = commission + 0.15*(sales-1000.0)
else:
    commission=0.10*sales
print("Commission is $",commission)
