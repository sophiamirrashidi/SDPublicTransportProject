class Stop:
    def __init__(self, stopid, blockid, routes, income, pop):
        self.stopid = int(stopid)
        self.blockid = blockid
        self.routes = routes
        self.income = int(income)
        self.pop = int(pop)
        self.importance = 0
        self.weight = self.income/10 + self.pop*5

    def setStopid(self, stopid):
        self.stopid = stopid

    def setBlockid(self, blockid):
        self.blockid = blockid

    def setRoutes(self, routes):
        self.routes = routes

    def setIncome(self, income):
        self.income = income

    def setPop(self, pop):
        self.pop = pop

    def setImportance(self, importance):
        self.importance = importance

    def getStopid(self):
        return self.stopid

    def getBlockid(self):
        return self.blockid

    def getRoutes(self):
        return self.routes

    def getIncome(self):
        return self.income

    def getPop(self):
        return self.pop

    def getImportance(self):
        return self.importance

    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return f'stopid: {self.stopid}, blockid: {self.blockid}, routes: {self.routes}, income: {self.income}, pop: {self.pop}, weight: {self.weight}, importance: {self.importance}'
                
    
