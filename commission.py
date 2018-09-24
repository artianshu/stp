lockPrice = 45.0
stockPrice = 30.0
barrelsPrice = 25.0
totalBarrels = 0
totalStocks = 0
totalBarrels = 0
totalLocks = 0
locks = int(input("Enter value of locks:"))
while not locks == -1:
    stocks = int(input("Enter value of stocks:"))
    barrels = int(input("Enter value of barrels:"))
    totalLocks = totalLocks + locks
    totalStocks = totalStocks + stocks
    totalBarrels = totalBarrels + barrels
    locks = int(input("Enter value of locks:"))
print("Locks Sold:",totalLocks)
print("Stocks Sold:",totalStocks)
print("Barrels Sold:",totalBarrels)
lockSales = lockPrice * totalLocks
stockSales = stockPrice * totalStocks
barrelsSales = barrelsPrice * totalBarrels
sales = lockSales + stockSales + barrelsSales
print("Total Sales:",sales)
if sales > 1800:
    comm = 0.10* 1000.0
    comm = comm + 0.15 * 800.0
    comm = comm + 0.20 * (sales-1800.0)
elif sales > 1000.0:
    comm = 0.100 * 1000.0
    comm = comm + 0.15 * (sales-1000)
else:
    comm = 0.10 * sales
print("Commission is $",comm)