import matplotlib.pyplot as plt
import networkx as nx
import myParser as inputFile
from Interval import Interval

print("Give N")
# N = int(sys.stdin.readline())
N = 2

allNodes = list()  # holds all the lines from txt as object(sourid,targetid,timestamp)
minTimeStamp: int
maxTimeStamp: int
allNodes, minTimeStamp, maxTimeStamp = inputFile.readFile()  # fetching allNodes, Min/Max timeStamp from file

# if allNodes is not None:
#     for run in allNodes:
#         run.toString()
# else:
#     print("Failed to read file")

print("Exw sunolika " + str(len(allNodes)) + " nodes")

# maxStamp = int(allNodes[0].getTimeStamp())
# minStamp = int(allNodes[0].getTimeStamp())
# for run in allNodes:
#     if int(run.getTimeStamp()) > maxStamp:
#         maxStamp = int(run.getTimeStamp())
#     if int(run.getTimeStamp()) < minStamp:
#         minStamp = int(run.getTimeStamp())

dif = (maxTimeStamp - minTimeStamp)
step = dif / N
# todo find the correct interval limits
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
print("TUPWNW NODES @ INTERNALS ")

for tmp in allIntervals:
    tmp.intervalPrint()
    print("Exw " + str(tmp.getTotalNodes()) + " nodes ta:")
    for aek in tmp.getIntervalNodes():
        print(str(aek.getSourceID())+ " "+str(aek.getTargetID()))

# for tmp in allNodes:
#     tmp.toString()
#     print("Eimai sto ",end=" ")
#     tmp.getInterval().toString()

G = nx.grid_2d_graph(5, 5)  # 5x5 grid

# print the adjacency list

# nx.draw(H)
# plt.show()

G=nx.Graph()
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

#iterate all intervals and create Graphs
for i in range(0,1):
    for tmpInt in allIntervals: # for each interval
        if tmpInt.hasNodes() is True:
            for tmpNode in tmpInt.getIntervalNodes():
                G.add_edge(tmpNode.getSourceID(),tmpNode.getTargetID())




nx.draw(G)
plt.savefig("simple_path.png") # save as png

print(G.nodes())
# print(G.edges())

G.remove_edges_from(G.edges())
G.add_edge("9","8")
G.add_edge("1","1")
print(G.edges())
nx.draw(G)
plt.savefig("simple_path2.png") # save as png