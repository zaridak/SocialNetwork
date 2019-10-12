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
N = 20

createFoldersIfNotExist()
deleteFilesIfExist()

allNodes = list()  # holds all the lines from txt as object(sourid,targetid,timestamp)
minTimeStamp: int
maxTimeStamp: int
allNodes, minTimeStamp, maxTimeStamp = inputFile.readFile("sx-stackoverflow-100k_clean.txt")  # fetching allNodes, Min/Max timeStamp from file

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

def write_Q3_file():
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
write_Q3_file()


# iterate all intervals and create Graphs for Q 3
allGraphsList=[]

#create graphs for each interval
j=0
for tmpInt in allIntervals: # for each interval
    Gd = nx.DiGraph()
    Gu = nx.Graph()
    if tmpInt.hasNodes() is True:  # null check
        j+=1
        for tmpNode in tmpInt.getIntervalNodes():
            Gd.add_edge(tmpNode.getSourceID(),tmpNode.getTargetID())
            Gu.add_edge(tmpNode.getSourceID(),tmpNode.getTargetID())
        allGraphsList.append({
            "interval":tmpInt,
            "Dgraph":Gd,
            "Ugraph":Gu
        })

def draw_graphs():
    for g in allGraphsList:
        G=g['Ugraph']
        nx.draw(G,with_labels = True)
        plt.savefig("GraphPics/3pic_"+str(j)+".png")
        plt.close()
draw_graphs()

for g in allGraphsList:
    CalculateCentrality(g['interval'], g['Dgraph'],g['Ugraph'])

def get_common_nodes(G,H):
    R=G.copy()
    R.remove_nodes_from(n for n in G if n not in H)
    return R.nodes

def get_edges_for_common_nodes(G, n):
    R=G.copy()
    R.remove_edges_from(edge for edge in G.edges if edge[0] not in n or edge[1] not in n) 
    return R.edges

for idx in range(len(allGraphsList)-1):
    interval0=allGraphsList[idx]['interval']
    graph0=allGraphsList[idx]['Ugraph']
    interval1=allGraphsList[idx+1]['interval']
    graph1=allGraphsList[idx+1]['Ugraph']
    print("Working on intervals: ")
    interval0.intervalPrint()
    interval1.intervalPrint()
    print("total interval: ", interval0.minValue, " - ", interval1.maxValue)
    commonNodes = get_common_nodes(graph0,graph1)
    graph0edges = get_edges_for_common_nodes(graph0,commonNodes)
    graph1edges = get_edges_for_common_nodes(graph1,commonNodes)
    print("common nodes: ", commonNodes)
    print("graph0 edges: ", graph0edges)
    print("graph1 edges: ", graph1edges)



def get_common_nodes(G,H):
    R=G.copy()
    R.remove_nodes_from(n for n in G if n not in H)
    return R.nodes

def get_edges_for_common_nodes(G, n):
    R=G.copy()
    R.remove_edges_from(edge for edge in G.edges if edge[0] not in n or edge[1] not in n) 
    return R.edges