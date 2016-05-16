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

def testVF2(g1, g2):
    t0 = pc()
    print("VF2: " + str(g1.isomorphic(g2)))
    return pc() - t0

def testWL(algo, g1, g2):
    t0 = pc()
    isomorphic = algo.execute(g1, g2, 15)
    print("WL: " + str(isomorphic))
    return pc() - t0

def testLCFStat12():
    g1=Graph.LCF(12, (5, -5), 6)
    g2=Graph.Famous("Franklin")
    t1 = testVF2(g1, g2)
    wl = WL()
    t2 = testWL(wl, g1, g2)
    print('testLCFStat12')
    return ['testLCFStat12', t1, t2]

def testFull100ISO():
    g1 = Graph.Full(100)
    g2 = Graph.Full(100)
    t1 = testVF2(g1, g2)
    wl = WL()
    t2 = testWL(wl, g1, g2)
    print('testFull100ISO')
    return ['testFull100ISO', t1, t2]

def testFull1000ISO():
    g1 = Graph.Full(1000)
    g2 = Graph.Full(1000)
    t1 = testVF2(g1, g2)
    wl = WL()
    t2 = testWL(wl, g1, g2)
    print('testFull1000ISO')
    return ['testFull1000ISO', t1, t2]

def testFull1000NONISO():
    g1 = Graph.Tree(1000, 4, TREE_UNDIRECTED )
    g2 = Graph.Full(1000)
    t1 = testVF2(g1, g2)
    wl = WL()
    t2 = testWL(wl, g1, g2)
    print('testFull1000NONISO')
    return ['testFull1000NONISO', t1, t2]

def testTREE100ISO():
    g1 = Graph.Tree(100, 4, TREE_UNDIRECTED )
    g2 = Graph.Tree(100, 4, TREE_UNDIRECTED)
    t1 = testVF2(g1, g2)
    wl = WL()
    t2 = testWL(wl, g1, g2)
    print('testTREE100ISO')
    return ['testTREE100ISO', t1, t2]

def testTREE1000ISO():
    g1 = Graph.Tree(1000, 4, TREE_UNDIRECTED )
    g2 = Graph.Tree(1000, 4, TREE_UNDIRECTED)
    t1 = testVF2(g1, g2)
    wl = WL()
    t2 = testWL(wl, g1, g2)
    print('testTREE1000ISO')
    return ['testTREE1000ISO', t1, t2]



def main():
    stat1 = testLCFStat12()
    #print(stat1)
    stat2 = testFull100ISO()
    stat3 = testFull1000ISO()
    stat4 = testFull1000NONISO()
    stat5 = testTREE100ISO()
    stat6 = testTREE1000ISO()

    ret = [stat1, stat2, stat3, stat4, stat5, stat6]
    return ret

stats  = main()
print(str(stats))

# tracer = trace.Trace(
#     ignoredirs=[sys.prefix, sys.exec_prefix],
#     trace=0,
#     count=1)

# tracer.run('main()')
# r = tracer.results()
# r.write_results(show_missing=True, coverdir=".")
# print(str(r))
