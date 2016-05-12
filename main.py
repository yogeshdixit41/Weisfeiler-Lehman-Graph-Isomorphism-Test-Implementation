from igraph import *
from WL import *

def generateTree(nodes, seed):
    degree = seed;
    g = Graph.Full(degree)
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

#displayG(G1)
#displayG(G2)
algo.execute(G1, G2, n)

# algo2 = WL()

#print(algo2.execute(G3, G4))
