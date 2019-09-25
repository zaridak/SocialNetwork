import collections
import matplotlib.pyplot as dia
import networkx as nx


pic = 0

def CalculateCentrality(interval, G):
    # DegreeCentrality(interval, G)
    # ClosenessCentrality(interval, G)
    # BetweennesCentrality(interval, G)
    # EigenvectorCentrality(interval, G)
    # KatzCentrality(interval, G)
    Centrality(interval, G, "DegreeCentrality")
    Centrality(interval, G, "ClosenessCentrality")
    Centrality(interval, G, "BetweennesCentrality")
    Centrality(interval, G, "EigenvectorCentrality")
    Centrality(interval, G, "KatzCentrality")


def Centrality(interval, G, title):
    dc = 0
    label = ""
    if title == "DegreeCentrality":
        dc = collections.OrderedDict(sorted(nx.degree_centrality(G).items(), key=lambda kv: kv[1]))
        label = "Degree Centrality"
    elif title == "ClosenessCentrality":
        dc = collections.OrderedDict(sorted(nx.closeness_centrality(G).items(), key=lambda kv: kv[1]))
        label = "Closeness Centrality"
    elif title == "BetweennesCentrality":
        dc = collections.OrderedDict(sorted(nx.betweenness_centrality(G).items(), key=lambda kv: kv[1]))
        label = "Betweennes Centrality"
    elif title == "EigenvectorCentrality":
        dc = collections.OrderedDict(sorted(nx.eigenvector_centrality(G).items(), key=lambda kv: kv[1]))
        label = "Eigenvector Centrality"
    elif title == "KatzCentrality":
        dc = collections.OrderedDict(sorted(nx.katz_centrality_numpy(G).items(), key=lambda kv: kv[1]))
        label = "Katz Centrality"

    i = 0
    tmp = next(iter(dc.values()))  # the first value of the centralities
    dictToDia = dict()
    leng = 0
    for value in dc.values():
        leng += 1
        if tmp == value:
            i += 1
            # if is last element
            if leng == len(dc):
                dictToDia.__setitem__(tmp, i / len(dc))
        if tmp != value:
            dictToDia.__setitem__(tmp, i / len(dc))
            i = 1
            tmp = value
            if leng == len(dc):
                dictToDia.__setitem__(tmp, i / len(dc))

    xlist = []
    ylist = []
    for k, v in dictToDia.items():
        xlist.append(k)
        ylist.append(v)

    # print(xlist)
    # proti agili x, deuterh y
    # dia.plot([1, 3], [2, 5], alpha=0.8, color='black', label='Key Value')
    dia.plot(xlist, ylist, alpha=0.8, color='gold', label='Key Value')

    dia.xlabel('Centrality')
    dia.ylabel('Percentage')
    dia.title(interval + "\n" + label)

    dia.legend()
    dia.tight_layout()

    global pic
    pic += 1
    dia.savefig("Centrality_Diagrams/"+label+str(pic))

    # dia.show()


# def DegreeCentrality(interval, G):
#     dc = collections.OrderedDict(sorted(nx.degree_centrality(G).items(), key=lambda kv: kv[1]))
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
#     dc = collections.OrderedDict(sorted(nx.closeness_centrality(G).items(), key=lambda kv: kv[1]))
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
#     dc = collections.OrderedDict(sorted(nx.betweenness_centrality(G).items(), key=lambda kv: kv[1]))
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
#     dc = collections.OrderedDict(sorted(nx.eigenvector_centrality(G).items(), key=lambda kv: kv[1]))
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
#     dc = collections.OrderedDict(sorted(nx.katz_centrality_numpy(G).items(), key=lambda kv: kv[1]))
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
