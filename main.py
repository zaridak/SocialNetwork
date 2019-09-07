import myParser as inputFile

allNodes = list()

allNodes = inputFile.readFile()

if allNodes is not None:
    for run in allNodes:
        run.toString()
else:
    print("Failed to read file")

print("Exw sunolika "+str(len(allNodes))+" nodes")

