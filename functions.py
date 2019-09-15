import os.path


def createFoldersIfNotExist():
    if not os.path.exists('GraphPics'):
        os.makedirs('GraphPics')
    if not os.path.exists('Documents'):
        os.makedirs('Documents')

def deleteFilesIfExist():
    if os.path.exists("Documents/Q3Nodes.txt"):
        os.remove("Documents/Q3Nodes.txt")