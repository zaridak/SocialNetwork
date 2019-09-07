import sys


# class holding a node, one line
class Node:
    sourceID: int = 0
    targetID: int = 0
    timeStamp: int = 0

    def __init__(self, source, target, time):
        self.sourceID = source
        self.targetID = target
        self.timeStamp = time

    def __init__(self, line):
        tmp = line.split()
        try:
            self.sourceID = tmp[0]
            self.targetID = tmp[1]
            self.timeStamp = tmp[2]
        except Exception as ex:
            sys.exit("Error at Node constructor, wrong file format" + str(ex))

    def getSourceID(self):
        return self.sourceID

    def getTargetID(self):
        return self.targetID

    def getTimeStamp(self):
        return self.timeStamp

    def setSourceID(self, source):
        self.sourceID = source

    def toString(self):
        print(self.sourceID + " " + self.targetID + " " + self.timeStamp)