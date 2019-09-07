class Interval:
    minValue: float = 0
    maxValue: float = 0
    intervalNodes = list()

    def __init__(self, minvalue, maxvalue):
        self.minValue = minvalue
        self.maxValue = maxvalue

    def addNode(self, node):
        self.intervalNodes.append(node)

    def getTotalNodes(self):
        return len(self.intervalNodes)

    def toString(self):
        print("Min = "+str(self.minValue)+"\nMax = "+str(self.maxValue))