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
step = float(maxTimeStamp/N)
# todo find the correct interval limits
print("Min: " + str(minTimeStamp) + "\nMax: " + str(maxTimeStamp) + "\nsec dif = " + str(dif))
print("Splitting to  " + str(N) + " intervals step: " + str(step))

allIntervals = list()
tmpMin = minTimeStamp
for i in range(0, N):
    allIntervals.append(Interval(tmpMin, tmpMin+step))
    tmpMin = tmpMin+step
for delete in allIntervals:
    delete.toString()