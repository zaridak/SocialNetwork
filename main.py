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

lol = nx.degree_centrality(G)
wtf = nx.generate_adjlist(G,',')
#print("lol = "+str(lol))
print(lol.keys())
print(lol.values())

# for line in wtf:
#     print(line)

# data to plot
n_groups = 1
means_frank = (13, 0.375)
means_guido = (1, 0.25)
means_3 = (17, 0.125)
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 1
opacity = 0.8

rects1 = plt.bar(index, means_frank, bar_width,
alpha=opacity,
color='gold',
label='Key')

rects2 = plt.bar(index + bar_width, means_guido, bar_width,
alpha=opacity,
color='black',
label='Value')

rects2 = plt.bar(index + 2*bar_width, means_3, bar_width,
alpha=opacity,
color='green',
label='Value')

rects2 = plt.bar(index + 3*bar_width, (48, 0.125), bar_width,
alpha=opacity,
color='grey')

rects2 = plt.bar(index + 4*bar_width, (2, 0.125), bar_width,
alpha=opacity,
color='yellow')

rects2 = plt.bar(index + 5*bar_width, (3, 0.125), bar_width,
alpha=opacity,
color='purple')

rects2 = plt.bar(index + 6*bar_width, (3, 0.125), bar_width,
alpha=opacity,
color='gold')

dia.xlabel('Node')
dia.ylabel('Centrality')
dia.title('Degree Centrality')

dia.xticks(index, ('ο'))

dia.legend()

# dia.tight_layout()
dia.show()
