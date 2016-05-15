from igraph import *
from WL import *

def generateTree(nodes, seed):
    degree = seed;
    g = Graph.Tree(nodes, degree)
    return g

def generateRandom(seed):
    prob = seed
    g = Graph.GRG(10, prob)

def displayG(g):
    layout = g.layout("kk")
    plot(g, layout = layout)



G1 = generateTree(10, 2)
G2 = generateTree(10, 3)
G3 = generateRandom(0.1)
G4 = generateRandom(0.2)
n = 12

algo = WL()
G1['name'] = 'G1'
G2['name'] = 'G2'
displayG(G1)
print(G1)
isomorphic = algo.execute(G1, G1, n)
print("Isomorphic = " + str(isomorphic))

#displayG(G1)
#displayG(G2)
