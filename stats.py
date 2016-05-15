from igraph import *
from WL import *
import trace
from time import perf_counter as pc

def displayG(g):
    layout = g.layout("kk")
    plot(g, layout = layout)

def writeG(g):
    layout = g.layout("kk")
    plot(g, layout = layout, target=g['name'] + '.png')
# Tests:
# 

def testLCF():
    g1=Graph.LCF(12, (5, -5), 6)
    g2=Graph.Famous("Franklin")

    t0 = pc()
    print(g1.isomorphic(g2))
    print(pc() - t0)

    g1['name'] = "LCF"
    g2['name'] = "Franklin"
    writeG(g1)
    writeG(g2)
    algo = WL()
    t0 = pc()
    isomorphic = algo.execute(g1, g2, 12)
    print("Isomorphic = " + str(isomorphic))
    print(pc() - t0)

    # self.assertRaises(InternalError, Graph.LCF, 12, (5, -5), -3)


def main():
    formula = "Alice-Bob-Cecil-Alice, Daniel-Cecil-Eugene, Cecil-Gordon"
    g = Graph.Formula(formula)
    # displayG(g)
    testLCF()

tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)

tracer.run('main()')
r = tracer.results()
# r.write_results(show_missing=True, coverdir=".")
# print(str(r))

