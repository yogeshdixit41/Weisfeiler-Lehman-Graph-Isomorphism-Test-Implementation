from igraph import *
from WL import *
from MultisetLabelGenerator import *

class MultisetStringGenerator:
    '''
    * second step : ( Sorting each multiset and return resulting string)
    * input params: multiset
    * output:
    '''
    def initLabelStrings(self, g):
        for v in g.vs:
            v[Labels.CURRENT_LABEL_STR] = str(v.degree())


    def generateStringLabels(self, g):
        concatString = ""
        for v in g.vs:
            #concatArr = [str(each) for each in v["currMultiset"]]
            for each in v["currMultiset"]:
                concatString = concatString + str(each)
            #concatString = ''.join(concatArr)
            v[Labels.CURRENT_LABEL_STR] = str(v[Labels.PREV_LABEL]) + concatString
