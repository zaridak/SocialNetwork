import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import myParser as inputFile
import matplotlib.pyplot as dia
from Interval import Interval
from functions import *


print("Give N")
# N = int(sys.stdin.readline())
N = 2

createFoldersIfNotExist()
deleteFilesIfExist()

allNodes = list()  # holds all the lines from txt as object(sourid,targetid,timestamp)
minTimeStamp: int
maxTimeStamp: int
allNodes, minTimeStamp, maxTimeStamp = inputFile.readFile()  # fetching allNodes, Min/Max timeStamp from file

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
        print(str(aek.getSourceID())+ " "+str(aek.getTargetID()))
q3file.close()

# G = nx.grid_2d_graph(5, 5)  # 5x5 grid
# print the adjacency list
# nx.draw(H)
# plt.show()
# G=nx.Graph()
# G.add_node("a")
# G.add_nodes_from(["d","b","c"])
# G.add_node("aek")
# G.add_node("original")
# edge = ("d", "e")
# G.add_edge(*edge)
# edge = ("a", "b")
# G.add_edge(*edge)
# G.add_edge(*edge)
# edge= ("aek","original")
# G.add_edge(*edge)
# edge = ("c","aek")
# G.add_edge(*edge)
# print("Nodes of graph: ")
# print(G.nodes())
# print("Edges of graph: ")
# print(G.edges())
# for line in nx.generate_adjlist(G):
#    print(line)

# iterate all intervals and create Graphs for Q 3
j=0
for i in range(0,1):
    for tmpInt in allIntervals: # for each interval
        G = nx.Graph()
        if tmpInt.hasNodes() is True: # null check
            j+=1
            for tmpNode in tmpInt.getIntervalNodes():
                G.add_edge(tmpNode.getSourceID(),tmpNode.getTargetID())
            nx.draw(G,with_labels = True)
            plt.savefig("GraphPics/3pic_"+str(j)+".png")
            plt.close()

# instal matplotlib
# python -m pip install -U pip
# python -m pip install -U matplotlib

lol = nx.degree_centrality(G)
print(lol)
print(lol.keys())
print(lol.values())

##################################
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))

dia.stem(x, y, use_line_collection=True)
dia.show()
dia.savefig("test.png")