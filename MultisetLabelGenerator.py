from igraph import *
from WL import *
from MultisetStringGenerator import *
import Labels

class MultisetLabelGenerator:

    def initLabels(self, g):
        for v in g.vs:
            v[Labels.PREV_LABEL] = str(v.degree())

    def generateLabels(self, g):
        for v in g.vs:
            v[Labels.MULTISET] = []
            for nv in v.neighbors():
                v[Labels.MULTISET].append(nv[Labels.PREV_LABEL])
            v[Labels.MULTISET].sort()
