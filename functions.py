import os.path
import shutil

def createFoldersIfNotExist():
    if not os.path.exists('GraphPics'):
        os.makedirs('GraphPics')
    if not os.path.exists('Documents'):
        os.makedirs('Documents')
    if not os.path.exists('Centrality_Diagrams'):
        os.makedirs('Centrality_Diagrams')


def deleteFilesIfExist():
    if os.path.exists("Documents/Q3Nodes.txt"):
        os.remove("Documents/Q3Nodes.txt")
    if os.path.exists("Centrality_Diagrams/"):
        shutil.rmtree('Centrality_Diagrams/')
        os.makedirs('Centrality_Diagrams')


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