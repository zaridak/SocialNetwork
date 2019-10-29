import os.path
import shutil
import networkx as nx
import matplotlib.pyplot as plt
from Centralities import CalculateCentrality


def createFoldersIfNotExist():
    if not os.path.exists('GraphPics'):
        os.makedirs('GraphPics')
    if not os.path.exists('Documents'):
        os.makedirs('Documents')
    if not os.path.exists('Centrality_Diagrams'):
        os.makedirs('Centrality_Diagrams')
    if not os.path.exists('Similarity_Measures'):
        os.makedirs('Similarity_Measures')


def deleteFilesIfExist():
    if os.path.exists("Documents/Q3Nodes.txt"):
        os.remove("Documents/Q3Nodes.txt")
    if os.path.exists("Centrality_Diagrams/"):
        shutil.rmtree('Centrality_Diagrams/')
        os.makedirs('Centrality_Diagrams')
    if os.path.exists("Similarity_Measures/"):
        shutil.rmtree('Similarity_Measures/')
        os.makedirs('Similarity_Measures')


def write_Q3_file(allIntervals):
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


def draw_graphs(allGraphsList):
    j=1
    for g in allGraphsList:
        G=g['Ugraph']
        nx.draw(G, node_size=30)
        plt.savefig("GraphPics/3pic_"+str(j)+".png", dpi=1200)
        j+=1
        plt.close()

def draw_centrality_graphs(allGraphsList):
    for g in allGraphsList:
        CalculateCentrality(g['interval'], g['Dgraph'],g['Ugraph'])


def get_common_nodes(G,H):
    R=G.copy()
    R.remove_nodes_from(n for n in G if n not in H)
    return R.nodes


def get_graph_for_common_nodes(G, n):
    R=G.copy()
    R.remove_edges_from(edge for edge in G.edges if edge[0] not in n or edge[1] not in n) 
    return R

def get_CN(G):
    CN=[]
    for u in G.nodes:
        for v in G.nodes:
            if u != v:
                commonNeighbors = list(nx.common_neighbors(G, u, v))
                CN.append((u,v,len(commonNeighbors)))
    return CN


def get_GD(G):
    GD=[]
    for t in nx.all_pairs_shortest_path_length(G):
        u=t[0]
        for v in t[1]:
            if v!=u:
                GD.append((u,v,-t[1][v]))
    return GD


def get_JC(G):
    JC=[]
    for t in nx.jaccard_coefficient(G):
        if t[0]!=t[1]:
            JC.append(t)
    return JC


def get_A(G):
    A=[]
    for t in nx.adamic_adar_index(G):
        if t[0]!=t[1]:
            A.append(t)
    return A


def get_PA(G):
    PA=[]
    for t in nx.preferential_attachment(G):
        if t[0] != t[1]:
            PA.append(t)
    return PA


def get_success_percent(M0, G1):
    correct = 0
    total = len(M0)
    for p in M0:
        if(G1.has_edge(p[0],p[1])):
            correct+=1
    return correct/total


def common_nodes_to_file(
    idx, 
    interval0, 
    interval1, 
    commonNodes, 
    edges0, 
    edges1):
    fileName = "Similarity_Measures/CommonNodesAndEdges_"+str(idx)+".txt"
    lines=[]
    lines.append("j:" +str(idx))
    lines.append("Interval " + str(idx) +": " + interval0.getMinMax())
    lines.append("Interval " + str(idx+1) +": " + interval1.getMinMax())
    lines.append("Common Nodes:")
    lines.append("\n".join(commonNodes))
    lines.append("Interval " + str(idx) +" Edges of common nodes:")
    lines.append("\n".join([e[0]+"-"+e[1] for e in edges0]))
    lines.append("Interval " + str(idx+1) +" Edges of common nodes:")
    lines.append("\n".join([e[0]+"-"+e[1] for e in edges1]))
    with open(fileName, 'a') as f:
        f.writelines("\n".join(lines))



def similarity_measures_to_file(idx,measure,interval0,interval1,S_0,S_1,P,top,successRate):
    fileName = "Similarity_Measures/"+measure+"_"+str(idx)+".txt"
    lines=[]
    lines.append(measure + " j:" +str(idx))
    lines.append("Interval " + str(idx) +": " + interval0.getMinMax())
    lines.append("Interval " + str(idx+1) +": " + interval1.getMinMax())
    lines.append("P: " + str(P))
    lines.append("Success Rate " + str(successRate))
    lines.append("Interval " + str(idx) + " " + measure + "")
    lines.append("\n".join([e[0]+"-"+e[1] + ": " + str(e[2]) for e in S_0]))
    lines.append("Interval " + str(idx+1) + " " + measure + "")
    lines.append("\n".join([e[0]+"-"+e[1] + ": " + str(e[2]) for e in S_1]))
    lines.append("Top " + str(P) +" percent of measurements: ")
    lines.append("\n".join([e[0]+"-"+e[1] + ": " + str(e[2]) for e in top]))
    with open(fileName, 'a') as f:
        f.writelines("\n".join(lines))


# n_groups = 1
# means_frank = (13, 0.375)
# means_guido = (1, 0.25)
# means_3 = (17, 0.125)
# # create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 1
# opacity = 0.8

# plt.bar(3,5)
# rects1 = plt.bar(index, means_frank, bar_width,
# alpha=opacity,
# color='gold',
# label='Key')
# rects2 = plt.bar(index + bar_width, (10,20), bar_width,
# alpha=opacity,
# color='black',
# label='Value')
# rects2 = plt.bar(index + 2*bar_width, means_3, bar_width,
# alpha=opacity,
# color='green',
# label='Value')