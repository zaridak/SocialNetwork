import matplotlib
import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
import myParser as inputFile
import matplotlib.pyplot as dia
from Interval import Interval
from functions import *
from Centralities import CalculateCentrality

# self.data = np.array(rows, dtype=object)

def ask_input(Label):
    print(label)
    return int(sys.stdin.readline())
print("Give N")
# N = ask_input("Enter Number of Time Intervals")
# P_GD = ask_input("Enter PGD%")
# P_CN = ask_input("Enter PCN%")
# P_JC = ask_input("Enter PJC%")
# P_A = ask_input("Enter PA%")
# P_PA= ask_input("Enter PPA%")

N = 20
P_GD = 20
P_CN = 20
P_JC = 20
P_A = 20
P_PA = 20

createFoldersIfNotExist()
deleteFilesIfExist()

allNodes = list()  # holds all the lines from txt as object(sourid,targetid,timestamp)
minTimeStamp: int
maxTimeStamp: int
allNodes, minTimeStamp, maxTimeStamp = inputFile.readFile("sx-stackoverflow-10k.txt")  # fetching allNodes, Min/Max timeStamp from file

print("Totally " + str(len(allNodes)) + " nodes")
dif = (maxTimeStamp - minTimeStamp)
step = dif / N
# Question 1 Finding tMin and tMax
print("Min: " + str(minTimeStamp) + " || Max: " + str(maxTimeStamp))  # + "\nsec dif = " + str(dif))
print("Splitting to " + str(N) + " intervals step: " + str(step))

allIntervals = []

# Question 2 seperating into intervals
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


write_Q3_file(allIntervals)

# iterate all intervals and create Graphs for Q 3
allGraphsList=[]

#create graphs for each interval
for tmpInt in allIntervals: # for each interval
    Gd = nx.DiGraph()
    Gu = nx.Graph()
    if tmpInt.hasNodes() is True:  # null check
        for tmpNode in tmpInt.getIntervalNodes():
            Gd.add_edge(tmpNode.getSourceID(),tmpNode.getTargetID())
            Gu.add_edge(tmpNode.getSourceID(),tmpNode.getTargetID())
        allGraphsList.append({
            "interval":tmpInt,
            "Dgraph":Gd,
            "Ugraph":Gu
        })

draw_graphs(allGraphsList)
draw_centrality_graphs(allGraphsList)


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
    graph0WithCommonNodes = get_graph_for_common_nodes(graph0,commonNodes)
    graph0edges=graph0WithCommonNodes.edges
    graph1WithCommonNodes = get_graph_for_common_nodes(graph1,commonNodes)
    graph1edges=graph1WithCommonNodes.edges
    print("common nodes: ", commonNodes)
    print("graph0 edges: ", graph0edges)
    print("graph1 edges: ", graph1edges)

    #i.  [Graph Distance]
    S_GD_0 = get_GD(graph0WithCommonNodes)
    S_GD_1 = get_GD(graph1WithCommonNodes)

    #ii.  [Common Neighbors] όπου  το σύνολο των γειτόνων του κόμβου .
    # currently takes a long time to calculate :/
    S_CN_0 = get_CN(graph0WithCommonNodes)
    S_CN_1 = get_CN(graph1WithCommonNodes)

    #iii.  [Jaccard’s Coefficient]
    S_JC_0 = get_JC(graph0WithCommonNodes)
    S_JC_1 = get_JC(graph1WithCommonNodes)
    
    #iv.  [Adamic / Adar]
    S_A_0 = get_A(graph0WithCommonNodes)
    S_A_1 = get_A(graph1WithCommonNodes)

    #v.  [Preferential Attachment]
    S_PA_0 = get_PA(graph0WithCommonNodes)
    S_PA_1 = get_PA(graph1WithCommonNodes)

    p_GD_0 = int(math.ceil(P_GD*len(S_GD_0)/100))
    p_CN_0 = int(math.ceil(P_CN*len(S_CN_0)/100))
    p_JC_0 = int(math.ceil(P_JC*len(S_JC_0)/100))
    p_A_0 = int(math.ceil(P_A*len(S_A_0)/100))
    p_PA_0 = int(math.ceil(P_PA*len(S_PA_0)/100))

    top_GD_0 = sorted(S_GD_0, key=lambda x: x[2], reverse=True)[:p_GD_0]
    top_CN_0 = sorted(S_CN_0, key=lambda x: x[2], reverse=True)[:p_CN_0]
    top_JC_0 = sorted(S_JC_0, key=lambda x: x[2], reverse=True)[:p_JC_0]
    top_A_0 = sorted(S_A_0, key=lambda x: x[2], reverse=True)[:p_A_0]
    top_PA_0 = sorted(S_PA_0, key=lambda x: x[2], reverse=True)[:p_PA_0]

    success_rate_GD=get_success_percent(top_GD_0, graph1WithCommonNodes)
    success_rate_CN=get_success_percent(top_CN_0, graph1WithCommonNodes)
    success_rate_JC=get_success_percent(top_JC_0, graph1WithCommonNodes)
    success_rate_A=get_success_percent(top_A_0, graph1WithCommonNodes)
    success_rate_PA=get_success_percent(top_PA_0, graph1WithCommonNodes)

    print("break")

