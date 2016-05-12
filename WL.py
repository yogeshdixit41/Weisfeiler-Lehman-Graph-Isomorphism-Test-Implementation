from igraph import *
from MultisetStringGenerator import *
from MultisetLabelGenerator import *

class WL:
    def execute(self, g1, g2, numberOfIterations):
        mlg = MultisetLabelGenerator()
        mlsg = MultisetStringGenerator()
        mlg.initLabels(g1, g2)
        mlsg.initLabelStrings(g1,g2)
        for index in range(1, numberOfIterations):
            mlg.generateLabels(g1, g2)
            mlsg.generateStringLabels(g1, g2)
            pass
        pass
