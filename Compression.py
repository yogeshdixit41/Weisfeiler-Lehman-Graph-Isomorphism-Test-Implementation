from igraph import *
import cairo
import Labels

def displayG(g):
    layout = g.layout("kk")
    plot(g, layout = layout, target=g['name'] + '.png')
    # plot(g)

class LabelCompression:

    def __init__(self):
        self.HASH = dict()
        self.HASH['index'] = '0'

    def getHASH(self):
        return self.HASH

    def createTestGraph(self):
        testGraph = Graph.GRG(10, 0.2)
        i = 1
        for v in testGraph.vs:
            v[Labels.CURRENT_LABEL_STR] = str(i%3 + 1)
            i = i + 1

        testGraph['name'] = 'LGtest'
        return testGraph

    def compress(self, g):
        labels = []
        labels = [ v[Labels.CURRENT_LABEL_STR] for v in g.vs ]

        labels.sort()

        for s in labels:
            fs = -1
            if s not in self.HASH:
                currentIndex = self.HASH['index']
                newIndex = str(int(currentIndex) + 1)
                self.HASH['index'] = newIndex
                fs = newIndex
                self.HASH[s] = fs

        #relabelling
        for v in g.vs:
            v[Labels.PREV_LABEL] = self.HASH[v[Labels.CURRENT_LABEL_STR]]

        g.setOfNewlyCreatedLabels = set([ v[Labels.PREV_LABEL] for v in g.vs ])
        return g

    def testGraph(self):
        return self.testGraph

