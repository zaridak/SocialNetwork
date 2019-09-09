class Interval:
    minValue: float = 0
    maxValue: float = 0
    intervalNodes = list() # list with all nodes placed at this Interval

    def __init__(self, minvalue, maxvalue):
        self.minValue = minvalue
        self.maxValue = maxvalue

    def addNode(self, node):
        self.intervalNodes.append(node)

    def getTotalNodes(self):
        return len(self.intervalNodes)

    def getIntervalNodes(self):
        return self.intervalNodes

    def printTotalNodes(self):
        for fu in self.intervalNodes:
            print(fu.getTimeStamp())

    def toString(self):
        print("Min = "+str(self.minValue)+"\nMax = "+str(self.maxValue))

    def intervalPrint(self):
        print("["+str(self.minValue)+", "+str(self.maxValue)+"]")

    def getMinMax(self):
        return str(self.minValue)+", "+str(self.maxValue)

    def getMinBound(self):
        return self.minValue

    def getMaxBound(self):
        return self.maxValue

