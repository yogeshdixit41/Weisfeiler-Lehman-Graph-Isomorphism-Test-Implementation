from igraph import *
from WL import *
from MultisetStringGenerator import *

class MultisetLabelGenerator:

    def initLabels(self, g1, g2):
        for v in g1.vs:
            v['lPrev'] = v.degree()
        for v in g1.vs:
            print (v)
        pass

    def generateLabels(self, g1, g2):
        #self.initLabels(g1, g2);
        pass
