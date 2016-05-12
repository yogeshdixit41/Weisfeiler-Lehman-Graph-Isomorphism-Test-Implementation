from igraph import *
from MultisetStringGenerator import *
from MultisetLabelGenerator import *
from Compression import *

class WL:
    def execute(self, g1, g2, numberOfIterations):
        mlg = MultisetLabelGenerator()
        mlsg = MultisetStringGenerator()
        compressor = LabelCompression()

        mlg.initLabels(g1)
        mlg.initLabels(g2)
        mlsg.initLabelStrings(g1)
        mlsg.initLabelStrings(g2)
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
            print("--------------------------------")
            print(g1)
            print("...............")
            print(g2)
            print("--------------------------------")
            #compare g1 and g2

