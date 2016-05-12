from igraph import *
from WL import *
from MultisetLabelGenerator import *

class MultisetStringGenerator:
    '''
    * second step : ( Sorting each multiset and return resulting string)
    * input params: multiset
    * output:
    '''
    def initLabelStrings(self, g1, g2):
        for v in g1.vs:
            v[Labels.CURRENT_LABEL_STR] = str(v[Labels.PREV_LABEL])
        for v in g1.vs:
            print (v)
        pass

    def generateStringLabels(self, g1, g2):
        concatString = ""
        for v in g1.vs:
            for each in v["currMultiset"]:
                concatString = concatString + str(each)
            v[Labels.CURRENT_LABEL_STR] = str( v[Labels.PREV_LABEL]) + concatString
            print (v[Labels.CURRENT_LABEL_STR])
        pass
