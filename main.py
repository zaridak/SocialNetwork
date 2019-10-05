import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import myParser as inputFile
import matplotlib.pyplot as dia
from Interval import Interval
from functions import *
from Centralities import CalculateCentrality

# self.data = np.array(rows, dtype=object)

print("Give N")
# N = int(sys.stdin.readline())
N = 2

createFoldersIfNotExist()
deleteFilesIfExist()

allNodes = list()  # holds all the lines from txt as object(sourid,targetid,timestamp)
minTimeStamp: int
maxTimeStamp: int
allNodes, minTimeStamp, maxTimeStamp = inputFile.readFile("tinyDem.txt")  # fetching allNodes, Min/Max timeStamp from file

print("Totally " + str(len(allNodes)) + " nodes")
dif = (maxTimeStamp - minTimeStamp)
step = dif / N

print("Min: " + str(minTimeStamp) + " || Max: " + str(maxTimeStamp))  # + "\nsec dif = " + str(dif))
print("Splitting to " + str(N) + " intervals step: " + str(step))

allIntervals = []

tmpMin = minTimeStamp
for i in range(N):
    allIntervals.append(Interval(tmpMin, tmpMin + step))
    tmpMin = tmpMin + step
for delete in allIntervals:
    delete.intervalPrint()

nodeCounter = 0
intCounter = 0
# placing each line into intervals
for tmpNode in allNodes:
    nodeCounter += 1
    for tmpInter in allIntervals:
        intCounter += 1
        if float(tmpNode.getTimeStamp()) >= float(tmpInter.getMinBound()) and float(tmpNode.getTimeStamp()) <= float(
                tmpInter.getMaxBound()):
            tmpInter.addNode(tmpNode)
            tmpNode.setInterval(tmpInter)
print("Printing NODES @ INTERNALS ")

q3file = 0
#  Writing nodes of Q 3 to txt file
for tmp in allIntervals:
    # tmp.intervalPrint()
    print(tmp.getMinMax())
    fileName = "Documents/Q3Nodes.txt"
    q3file = open(fileName, 'a')
    q3file.write(tmp.getMinMax())
    print("I have " + str(tmp.getTotalNodes()) + " nodes:")
    for aek in tmp.getIntervalNodes():
        q3file.write(str(aek.getSourceID())+ " "+str(aek.getTargetID())+"\n")
        # print(str(aek.getSourceID())+ " "+str(aek.getTargetID()))
q3file.close()


# iterate all intervals and create Graphs for Q 3
allNxGraphs = dict()  # maybe different than N, if G empty
j=0
for i in range(0,1):
    for tmpInt in allIntervals: # for each interval
        G = nx.Graph()
        if tmpInt.hasNodes() is True:  # null check
            j+=1
            for tmpNode in tmpInt.getIntervalNodes():
                G.add_edge(tmpNode.getSourceID(),tmpNode.getTargetID())
            nx.draw(G,with_labels = True)

            allNxGraphs.__setitem__(tmpInt.getMinMax(),G)
            plt.savefig("GraphPics/3pic_"+str(j)+".png")
            plt.close()

# lol = nx.degree_centrality(G)
# wtf = nx.generate_adjlist(G,',')

for k, v in allNxGraphs.items():
    CalculateCentrality(k, v)
