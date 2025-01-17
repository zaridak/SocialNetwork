import collections
import matplotlib.pyplot as dia
import networkx as nx


pic = 0


def CalculateCentrality(interval, DirectedGraph, UndirectedGraph):
    # DegreeCentrality(interval, G)
    # ClosenessCentrality(interval, G)
    # BetweennesCentrality(interval, G)
    # EigenvectorCentrality(interval, G)
    # KatzCentrality(interval, G)
    Centrality(interval, UndirectedGraph, "DegreeCentrality")
    Centrality(interval, UndirectedGraph, "ClosenessCentrality")
    Centrality(interval, UndirectedGraph, "BetweennesCentrality")
    Centrality(interval, UndirectedGraph, "EigenvectorCentrality")
    Centrality(interval, UndirectedGraph, "KatzCentrality")
    Centrality(interval, DirectedGraph, "InDegreeCentrality")
    Centrality(interval, DirectedGraph, "OutDegreeCentrality")


def Centrality(interval, G, title):
    dc = 0
    label = ""
    if title == "DegreeCentrality":
        # dc = list(nx.degree_centrality(G).items(), key=lambda kv: kv[1])
        dc = list(nx.degree_centrality(G).items())
        label = "Degree Centrality"
    elif title == "ClosenessCentrality":
        # dc = list(nx.closeness_centrality(G).items(), key=lambda kv: kv[1])
        dc = list(nx.closeness_centrality(G).items())
        label = "Closeness Centrality"
    elif title == "BetweennesCentrality":
        # dc = list(nx.betweenness_centrality(G).items(), key=lambda kv: kv[1])
        dc = list(nx.betweenness_centrality(G).items())
        label = "Betweennes Centrality"
    elif title == "EigenvectorCentrality":
        # dc = list(nx.eigenvector_centrality_numpy(G,1000).items(), key=lambda kv: kv[1])
        dc = list(nx.eigenvector_centrality_numpy(G, 1000).items())
        label = "Eigenvector Centrality"
    elif title == "KatzCentrality":
        # dc = list(nx.katz_centrality_numpy(G).items(), key=lambda kv: kv[1])
        dc = list(nx.katz_centrality_numpy(G).items())
        label = "Katz Centrality"
    elif title == "InDegreeCentrality":
        # dc = list(nx.in_degree_centrality(G).items(), key=lambda kv: kv[1])
        dc = list(nx.in_degree_centrality(G).items())
        label= "In-Degree Centrality"
    elif title == "OutDegreeCentrality":
        # dc = list(nx.out_degree_centrality(G).items(), key=lambda kv: kv[1])
        dc = list(nx.out_degree_centrality(G).items())
        label= "Out-Degree Centrality"


    i = 0
    vals={} 
    for v in dc:
        if v[1] in vals:
            vals[v[1]]+=1
        else:
            vals[v[1]]=1
    xlist = list(vals.keys())
    ylist = list(vals.values())
    dia.plot(xlist, ylist, alpha=0.8, color='gold', label='Key Value')

    dia.xlabel('Centrality')
    dia.ylabel('Percentage')
    dia.title(interval.getMinMax() + "\n" + label)

    global pic
    pic += 1
    dia.savefig("Centrality_Diagrams/"+label+str(pic))

    # dia.show()


# def DegreeCentrality(interval, G):
#     dc listsorted(nx.degree_centrality(G).items(), key=lambda kv: kv[1])
#     i = 0
#     tmp = next(iter(dc.values())) # the first value of the centralities
#     dictToDia = dict()
#     leng = 0
#     for value in dc.values():
#         leng += 1
#         if tmp == value:
#             i += 1
#             # if is last element
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i/len(dc))
#         if tmp != value:
#             dictToDia.__setitem__(tmp, i/len(dc))
#             i = 1
#             tmp = value
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i/len(dc))
#
#     xlist = []
#     ylist = []
#     for k, v in dictToDia.items():
#         xlist.append(k)
#         ylist.append(v)
#
#     #print(xlist)
#     # proti agili x, deuterh y
#     # dia.plot([1, 3], [2, 5], alpha=0.8, color='black', label='Key Value')
#     dia.plot( xlist, ylist, alpha=0.8, color='gold', label='Key Value')
#
#     dia.xlabel('Centrality')
#     dia.ylabel('Percentage')
#     dia.title(interval + "\n" + "Degree Centrality")
#
#     # yaxis = []
#     # test = list(dictToDia.values())
#     # yaxis.append(test[0])
#     # if len(dictToDia)%2 == 0:
#     #     yaxis.append(round(test[int(len(dictToDia)/2)], 2))
#     # else:
#     #     yaxis.append(round(test[int(len(dictToDia)/2 -1)], 2))
#     # yaxis.append(round((test[len(test)-1]), 2))
#     # for v in dictToDia.values():
#     #     str.append(v)
#     # dia.xticks(yaxis)
#     dia.legend()
#     dia.tight_layout()
#     dia.show()
#
#
# def ClosenessCentrality(interval, G):
#     dc listsorted(nx.closeness_centrality(G).items(), key=lambda kv: kv[1])
#     i = 0
#     tmp = next(iter(dc.values())) # the first value of the centralities
#     dictToDia = dict()
#     leng = 0
#     for value in dc.values():
#         leng += 1
#         if tmp == value:
#             i += 1
#             # if is last element
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i/len(dc))
#         if tmp != value:
#             dictToDia.__setitem__(tmp, i/len(dc))
#             i = 1
#             tmp = value
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i/len(dc))
#
#     xlist = []
#     ylist = []
#     for k, v in dictToDia.items():
#         xlist.append(k)
#         ylist.append(v)
#
#     #print(xlist)
#     # proti agili x, deuterh y
#     # dia.plot([1, 3], [2, 5], alpha=0.8, color='black', label='Key Value')
#     dia.plot( xlist, ylist, alpha=0.8, color='gold', label='Key Value')
#
#     dia.xlabel('Centrality')
#     dia.ylabel('Percentage')
#     dia.title(interval + "\n" + "Closeness Centrality")
#
#     # yaxis = []
#     # test = list(dictToDia.values())
#     # yaxis.append(test[0])
#     # if len(dictToDia)%2 == 0:
#     #     yaxis.append(round(test[int(len(dictToDia)/2)], 2))
#     # else:
#     #     yaxis.append(round(test[int(len(dictToDia)/2 -1)], 2))
#     # yaxis.append(round((test[len(test)-1]), 2))
#     # for v in dictToDia.values():
#     #     str.append(v)
#     #dia.xticks(yaxis)
#     dia.legend()
#     dia.tight_layout()
#     dia.show()
#
#
# def BetweennesCentrality(interval, G):
#     dc listsorted(nx.betweenness_centrality(G).items(), key=lambda kv: kv[1])
#     i = 0
#     tmp = next(iter(dc.values()))  # the first value of the centralities
#     dictToDia = dict()
#     leng = 0
#     for value in dc.values():
#         leng += 1
#         if tmp == value:
#             i += 1
#             # if is last element
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i / len(dc))
#         if tmp != value:
#             dictToDia.__setitem__(tmp, i / len(dc))
#             i = 1
#             tmp = value
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i / len(dc))
#
#     xlist = []
#     ylist = []
#     for k, v in dictToDia.items():
#         xlist.append(k)
#         ylist.append(v)
#
#     # print(xlist)
#     # proti agili x, deuterh y
#     # dia.plot([1, 3], [2, 5], alpha=0.8, color='black', label='Key Value')
#     dia.plot(xlist, ylist, alpha=0.8, color='gold', label='Key Value')
#
#     dia.xlabel('Centrality')
#     dia.ylabel('Percentage')
#     dia.title(interval + "\n" + "Betweenness Centrality")
#
#     # yaxis = []
#     # test = list(dictToDia.values())
#     # yaxis.append(test[0])
#     # if len(dictToDia) % 2 == 0:
#     #     yaxis.append(round(test[int(len(dictToDia) / 2)], 2))
#     # else:
#     #     yaxis.append(round(test[int(len(dictToDia) / 2 - 1)], 2))
#     # yaxis.append(round((test[len(test) - 1]), 2))
#     i = 0
#     # for v in dictToDia.values():
#     #     str.append(v)
#     # print("to yaxis einai " + str(yaxis))
#     # yaxis.append(min(test))
#     # yaxis.append(max(test))
#     #dia.xticks(yaxis)
#     dia.legend()
#     dia.tight_layout()
#     dia.show()
#
#
# def EigenvectorCentrality(interval, G):
#     dc listsorted(nx.eigenvector_centrality(G).items(), key=lambda kv: kv[1])
#     i = 0
#     tmp = next(iter(dc.values()))  # the first value of the centralities
#     dictToDia = dict()
#     leng = 0
#     for value in dc.values():
#         leng += 1
#         if tmp == value:
#             i += 1
#             # if is last element
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i / len(dc))
#         if tmp != value:
#             dictToDia.__setitem__(tmp, i / len(dc))
#             i = 1
#             tmp = value
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i / len(dc))
#
#     xlist = []
#     ylist = []
#     for k, v in dictToDia.items():
#         xlist.append(k)
#         ylist.append(v)
#
#     # print(xlist)
#     # proti agili x, deuterh y
#     # dia.plot([1, 3], [2, 5], alpha=0.8, color='black', label='Key Value')
#     dia.plot(xlist, ylist, alpha=0.8, color='gold', label='Key Value')
#
#     dia.xlabel('Centrality')
#     dia.ylabel('Percentage')
#     dia.title(interval + "\n" + "Eigenvector Centrality")
#
#     # yaxis = []
#     # test = list(dictToDia.values())
#     # yaxis.append(test[0])
#     # if len(dictToDia) % 2 == 0:
#     #     yaxis.append(round(test[int(len(dictToDia) / 2)], 2))
#     # else:
#     #     yaxis.append(round(test[int(len(dictToDia) / 2 - 1)], 2))
#     # yaxis.append(round((test[len(test) - 1]), 2))
#     # yaxis.append(min(test))
#     # yaxis.append(max(test))
#     # for v in dictToDia.values():
#     #     str.append(v)
#     # dia.xticks(yaxis)
#     dia.legend()
#     dia.tight_layout()
#     dia.show()
#
#
# def KatzCentrality(interval, G):
#
#     dc listsorted(nx.katz_centrality_numpy(G).items(), key=lambda kv: kv[1])
#     i = 0
#     tmp = next(iter(dc.values()))  # the first value of the centralities
#     dictToDia = dict()
#     leng = 0
#     for value in dc.values():
#         leng += 1
#         if tmp == value:
#             i += 1
#             # if is last element
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i / len(dc))
#         if tmp != value:
#             dictToDia.__setitem__(tmp, i / len(dc))
#             i = 1
#             tmp = value
#             if leng == len(dc):
#                 dictToDia.__setitem__(tmp, i / len(dc))
#
#     xlist = []
#     ylist = []
#     for k, v in dictToDia.items():
#         xlist.append(k)
#         ylist.append(v)
#
#     # print(xlist)
#     # proti agili x, deuterh y
#     # dia.plot([1, 3], [2, 5], alpha=0.8, color='black', label='Key Value')
#     dia.plot(xlist, ylist, alpha=0.8, color='gold', label='Key Value')
#
#     dia.xlabel('Centrality')
#     dia.ylabel('Percentage')
#     dia.title(interval + "\n" + "Katz Centrality")
#
#     # yaxis = []
#     # test = list(dictToDia.values())
#     # yaxis.append(test[0])
#     # if len(dictToDia) % 2 == 0:
#     #     yaxis.append(round(test[int(len(dictToDia) / 2)], 2))
#     # else:
#     #     yaxis.append(round(test[int(len(dictToDia) / 2 - 1)], 2))
#     # yaxis.append(round((test[len(test) - 1]), 2))
#     # for v in dictToDia.values():
#     #     str.append(v)
#     # print("to yaxis einai "+str(yaxis))
#     # yaxis.append(min(test))
#     # yaxis.append(max(test))
#     # dia.xticks(yaxis)
#     dia.legend()
#     dia.tight_layout()
#     dia.savefig("lola.png")
#     dia.show()
