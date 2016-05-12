from igraph import *
from MultisetStringGenerator import *
from MultisetLabelGenerator import *
from Compression import *

class WL:
    def initIteration(self, g):
        for v in g.vs:
            v[Labels.CURRENT_LABEL_STR] = v[Labels.PREV_LABEL] = str(v.degree())

    def execute(self, g1, g2, numberOfIterations):

        mlg = MultisetLabelGenerator()
        mlsg = MultisetStringGenerator()
        compressor = LabelCompression()

        self.initIteration(g1)
        self.initIteration(g2)

        compressor.initHash()
        g1 = compressor.compress(g1) #hash initialization
        g2 = compressor.compress(g2) #hash initialization

        for index in range(1, numberOfIterations):
            mlg.generateLabels(g1)
            mlg.generateLabels(g2)
            mlsg.generateStringLabels(g1)
            mlsg.generateStringLabels(g2)
            g1 = compressor.compress(g1)
            g2 = compressor.compress(g2)

        #print(g1.setOfNewlyCreatedLabels)
        #print(g2.setOfNewlyCreatedLabels)

        if(g1.setOfNewlyCreatedLabels == g2.setOfNewlyCreatedLabels):
            print ("Graphs are isomorphic")
        else:
            print ("Graphs are not isomorphic")
            #compare g1 and g2
