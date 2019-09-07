from Node import Node
import sys


def readFile():
    try:
        nodes = open("tinyDem.txt", "r")
        retlist = list()
        for line in nodes:
            retlist.append(Node(line))
        nodes.close()
        return retlist
    except Exception as ex:
        sys.exit("Exception occurred opening file "+str(ex))
