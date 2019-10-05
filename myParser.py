from Node import Node
import sys

def readFile(filename):
    maxTimeStamp: int = 0
    minTimeStamp: int = 0
    try:
        nodes = open(filename, "r")
        #nodes = open("DEMOsx-stackoverflow.txt", "r") #10.000 entries
        #nodes = open("sx-stackoverflow-100k.txt", "r")  # 100.000 entries

        retlist = list()
        for line in nodes:
            retlist.append(Node(line))
            tmp = line.split()
            try:
                if minTimeStamp is 0:
                    minTimeStamp = int(tmp[2])
                else:
                    minTimeStamp = min(int(minTimeStamp), int(tmp[2]))
                if maxTimeStamp == 0:
                    maxTimeStamp = int(tmp[2])
                else:
                    maxTimeStamp = max(int(maxTimeStamp), int(tmp[2]))
            except Exception as ex:
                sys.exit("Exception occurred finding min/max " + str(ex))
        nodes.close()
        return retlist, int(minTimeStamp), int(maxTimeStamp)
    except Exception as ex:
        sys.exit("Exception occurred opening file " + str(ex))
