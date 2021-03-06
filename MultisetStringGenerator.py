
from igraph import *
from WL import *
from MultisetLabelGenerator import *

class MultisetStringGenerator:
    '''
    * second step : ( Sorting each multiset and return resulting string)
    * input params: multiset
    * output:
    '''



    def generateStringLabels(self, g):
        for v in g.vs:
            concatString = ""
            for each in v[Labels.MULTISET]:
                concatString = concatString + str(each)
            v[Labels.CURRENT_LABEL_STR] = str(v[Labels.PREV_LABEL]) + concatString
