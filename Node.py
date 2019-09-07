import sys
#class holding a node, one line
class Node:
    sourceID  = 0
    targetID  = 0
    timeStamp = 0

    def __init__(self, source, target, time):
        self.sourceID = source
        self.targetID = target
        self.timeStamp = time

    def __init__(self, Line):
        tmp = Line.split()
        try:
            self.sourceID = tmp[0]
            self.targetID = tmp[1]
            self.timeStamp =tmp[2]
        except Exception as ex:
            sys.exit("Error at Node constructor, wrong file format"+str(ex))

    def getSourceID(self):
        return self.sourceID

    def getTargetID(self):
        return self.targetID

    def getTimeStamp(self):
        return self.timeStamp

    def setSourceID(self, source):
        self.sourceID = source

    def toString(self):
        print(self.sourceID+" "+self.targetID+" "+self.timeStamp)
