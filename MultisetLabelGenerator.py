from igraph import *
from WL import *
from MultisetStringGenerator import *
import Labels

class MultisetLabelGenerator:

    def initLabels(self, g1, g2):
        for v in g1.vs:
            v[Labels.PREV_LABEL] = v.degree()
			#v[Labels.CURR_LABEL] = v.degree()
        for v in g1.vs:
            print (v)
        pass

    def generateLabels(self, g1, g2):
        for v in g1.vs:
            v["currMultiset"] = []
            for nv in v.neighbors():
                v["currMultiset"].append(nv[Labels.PREV_LABEL])
            v["currMultiset"].sort()
        #self.initLabels(g1, g2);
        pass
