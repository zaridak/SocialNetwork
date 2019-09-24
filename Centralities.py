import collections
import matplotlib.pyplot as dia
import networkx as nx


def CalculateCentrality(interval, G):
    # print(interval)
    # print(G.nodes())
    DegreeCentrality(interval, G)
    ClosenessCentrality(interval, G)
    BetweennesCentrality(interval, G)

def DegreeCentrality(interval, G):
    dc = collections.OrderedDict(sorted(nx.degree_centrality(G).items(), key=lambda kv: kv[1]))
    i = 0
    tmp = next(iter(dc.values())) # the first value of the centralities
    dictToDia = dict()
    leng = 0
    for value in dc.values():
        leng += 1
        if tmp == value:
            i += 1
            # if is last element
            if leng == len(dc):
                dictToDia.__setitem__(tmp, i/len(dc))
        if tmp != value:
            dictToDia.__setitem__(tmp, i/len(dc))
            i = 1
            tmp = value
            if leng == len(dc):
                dictToDia.__setitem__(tmp, i/len(dc))

    xlist = []
    ylist = []
    for k, v in dictToDia.items():
        xlist.append(k)
        ylist.append(v)

    #print(xlist)
    # proti agili x, deuterh y
    # dia.plot([1, 3], [2, 5], alpha=0.8, color='black', label='Key Value')
    dia.plot( xlist, ylist, alpha=0.8, color='gold', label='Key Value')

    dia.xlabel('Centrality')
    dia.ylabel('Percentage')
    dia.title(interval + "\n" + "Degree Centrality")
    yaxis = []
    test = list(dictToDia.values())

    yaxis.append(test[0])
    if len(dictToDia)%2 == 0:
        yaxis.append(round(test[int(len(dictToDia)/2)], 2))
    else:
        yaxis.append(round(test[int(len(dictToDia)/2 -1)], 2))
    yaxis.append(round((test[len(test)-1]), 2))
    i = 0
    # for v in dictToDia.values():
    #     str.append(v)
    dia.xticks(yaxis)
    dia.legend()
    dia.tight_layout()
    dia.show()

def ClosenessCentrality(interval, G):
    dc = collections.OrderedDict(sorted(nx.closeness_centrality(G).items(), key=lambda kv: kv[1]))
    i = 0
    tmp = next(iter(dc.values())) # the first value of the centralities
    dictToDia = dict()
    leng = 0
    for value in dc.values():
        leng += 1
        if tmp == value:
            i += 1
            # if is last element
            if leng == len(dc):
                dictToDia.__setitem__(tmp, i/len(dc))
        if tmp != value:
            dictToDia.__setitem__(tmp, i/len(dc))
            i = 1
            tmp = value
            if leng == len(dc):
                dictToDia.__setitem__(tmp, i/len(dc))

    xlist = []
    ylist = []
    for k, v in dictToDia.items():
        xlist.append(k)
        ylist.append(v)

    #print(xlist)
    # proti agili x, deuterh y
    # dia.plot([1, 3], [2, 5], alpha=0.8, color='black', label='Key Value')
    dia.plot( xlist, ylist, alpha=0.8, color='gold', label='Key Value')

    dia.xlabel('Centrality')
    dia.ylabel('Percentage')
    dia.title(interval + "\n" + "Closeness Centrality")
    yaxis = []
    test = list(dictToDia.values())

    yaxis.append(test[0])
    if len(dictToDia)%2 == 0:
        yaxis.append(round(test[int(len(dictToDia)/2)], 2))
    else:
        yaxis.append(round(test[int(len(dictToDia)/2 -1)], 2))
    yaxis.append(round((test[len(test)-1]), 2))
    i = 0
    # for v in dictToDia.values():
    #     str.append(v)
    dia.xticks(yaxis)
    dia.legend()
    dia.tight_layout()
    dia.show()

def BetweennesCentrality(interval, G):
    dc = collections.OrderedDict(sorted(nx.betweenness_centrality(G).items(), key=lambda kv: kv[1]))
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
    dia.title(interval + "\n" + "Betweenness Centrality")
    yaxis = []
    test = list(dictToDia.values())

    yaxis.append(test[0])
    if len(dictToDia) % 2 == 0:
        yaxis.append(round(test[int(len(dictToDia) / 2)], 2))
    else:
        yaxis.append(round(test[int(len(dictToDia) / 2 - 1)], 2))
    yaxis.append(round((test[len(test) - 1]), 2))
    i = 0
    # for v in dictToDia.values():
    #     str.append(v)
    dia.xticks(yaxis)
    dia.legend()
    dia.tight_layout()
    dia.show()
