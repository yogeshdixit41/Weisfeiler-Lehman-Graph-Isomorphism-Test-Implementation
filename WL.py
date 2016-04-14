from igraph import *
from MultisetStringGenerator import *
from MultisetLabelGenerator import *

class WL:
    def execute(self, g1, g2, numberOfIterations):
        mlg = MultisetLabelGenerator()
        mlsg = MultisetStringGenerator()
        mlg.initLabels(g1, g2)
        for index in range(1, numberOfIterations):

        pass
