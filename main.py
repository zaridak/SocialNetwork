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
step = dif/N
# todo find the correct interval limits
print("Min: " + str(minTimeStamp) + " || Max: " + str(maxTimeStamp))#+ "\nsec dif = " + str(dif))
print("Splitting to  " + str(N) + " intervals step: " + str(step))

allIntervals = list()
tmpMin = minTimeStamp
for i in range(0, N):
    allIntervals.append(Interval(tmpMin, tmpMin+step))
    tmpMin = tmpMin+step
for delete in allIntervals:
    delete.intervalPrint()

nodeCounter = 0
intCounter  = 0
# placing each line into intervals
for tmpNode in allNodes:
    nodeCounter+=1
    for tmpInter in allIntervals:
        intCounter+=1
        if float(tmpNode.getTimeStamp()) >= float(tmpInter.getMinBound()) and float(tmpNode.getTimeStamp()) <= float(tmpInter.getMaxBound()):
            # print("timeStamp: "+str(tmpNode.getTimeStamp())+" Going at min = "+str(tmpInter.getMinBound())+" max: "+str(tmpInter.getMaxBound()))
            print("Ekana add node me timeStamp " + str(tmpNode.getTimeStamp()) + " sto interval " + str(tmpInter.minValue) + " , " + str(tmpInter.maxValue))
            tmpInter.addNode(tmpNode)
            #tmpNode.setInterval(tmpInter)
print("TUPWNW NODES @ INTERNALS ")

# for aek in allIntervals:
#      print("Gia to interval "+str(aek.getMinMax()))
#      print("Exw sinolika parei "+str(aek.getTotalNodes())+" nodes")
# #    print(aek.printTotalNodes())
#
# for omg in allIntervals:
#     print(str(omg.getTotalNodes())+" "+str(omg.getMinBound())+" "+str(omg.getMaxBound()))
#     omg.printTotalNodes()

for aek in allIntervals:
    print(aek.getTotalNodes())
