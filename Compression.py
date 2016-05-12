from igraph import *
import cairo
import Labels

def displayG(g):
    layout = g.layout("kk")
    plot(g, layout = layout, target=g['name'] + '.png')
    # plot(g)

class LabelCompression:

    def initHash(self):
        self.HASH = dict()
        self.HASH['index'] = '1'
        self.HASH['1'] = '1'
        self.HASH['2'] = '2'
        self.HASH['3'] = '3'

    def createTestGraph(self):
        testGraph = Graph.GRG(10, 0.2)
        i = 1
        for v in testGraph.vs:
            v[Labels.CURRENT_LABEL_STR] = str(i%3 + 1)
            i = i + 1

        testGraph['name'] = 'LGtest'
        return testGraph

    def __init__(self):
        self.testGraph = self.createTestGraph()
        displayG(self.testGraph)
        self.initHash()

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

comp = LabelCompression()
summary(comp.testGraph)
g = comp.testGraph
for v in g.vs:
            vNeigh = g.neighbors(v, mode="out")
            #print('curr: ' + v[Labels.CURRENT_LABEL_STR])
            #print('neighCount: ' + str(len(vNeigh)))

comp.compress(comp.testGraph)

#for v in g.vs:
            #print('newLabel: ' + v[Labels.PREV_LABEL])
