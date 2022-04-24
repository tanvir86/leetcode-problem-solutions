class UndergroundSystem:

    def __init__(self):
        self.pendingCheckout = dict()
        self.avg = defaultdict(lambda: (0,0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.pendingCheckout[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.pendingCheckout[id]
        del self.pendingCheckout[id]
        
        self.avg[startStation+"-"+stationName] = (self.avg[startStation+"-"+stationName][0] + t - startTime, self.avg[startStation+"-"+stationName][1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg[startStation+"-"+endStation][0] / self.avg[startStation+"-"+endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
