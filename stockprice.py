class StockPrice(object):

    def __init__(self):
        self.stockprice={}
        self.currenttime=0


    def update(self, timestamp, price):
        self.stockprice[timestamp] = price
        if self.currenttime<=timestamp:
            self.currenttime=timestamp
        

    def current(self):
        return self.stockprice[self.currenttime]
        

    def maximum(self):
        return max(self.stockprice.values())
        

    def minimum(self):
        return min(self.stockprice.values())
        
newobj=StockPrice()
newobj.update(1,10)
print(newobj.current())
print(newobj.maximum())
print(newobj.minimum())

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()