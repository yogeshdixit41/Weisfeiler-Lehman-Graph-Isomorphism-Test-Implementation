'''
File written by Yogesh Dixit
Date : 12 May 2016
'''
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
        concatString = ""
        for v in g.vs:
            for each in v[Labels.MULTISET]:
                concatString = concatString + str(each)
            v[Labels.CURRENT_LABEL_STR] = str(v[Labels.PREV_LABEL]) + concatString
