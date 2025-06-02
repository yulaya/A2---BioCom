import itertools
import networkx as nx

#generateGraph receivees an ID for a graph of size n and generates it's adjacency matrix 
def generateGraph(ID, n):
  #first, we want to intialiize our n by n adjacency matrix to be all 0s
  G = nx.DiGraph()
  G.add_nodes_from(range(n))
  #graphId bit in binary, will correspond to an index in the adjacency matrix -- excpet for the diagonal for a self edge. (why we do n^2 - n) 
  globalIndex = 0 ##global index will hold for us, our position in the ID, 
  for i in range(n):
  
    for j in range(n):
  
      if i == j:
       continue
  
      else:
        
        if ((ID >> globalIndex) & 1): # >> bitwise right shift of ID, followed by AND with 1 --> checks if the bit in the Id 
       ##corresponding to this spot in the adjacency matrix is 1 --> this edge exists in this graph
          G.add_edge(i,j)
      globalIndex = globalIndex + 1 # so that next time we shift by an increased amount, to correctly identify the next spot --> [123][456][789]....
  
  return G

def motifsCreator(n):

 motifs = []

 for graphId in range (2 ** ((n*(n-1)))): ##the idea is that there are 2^E possible graphs (being that in a fully connected directional graph there are n(n-1) edges)
  
  generatedGraph = generateGraph(graphId,n)
  #in this problem we are essentially dealing with unlabled graphs, this means that if our generetedGraph x and some previously genertedGraph y
  # are a vertex permutation of each other (like 1->2 is isomorphoc to 2->1) we don't want to count it as an additional graph in our list 
  
  if (nx.is_weakly_connected(generatedGraph)): ## is_weakly_connected is a function which takes in a directed graph and returns true if it is weakly connected, false otherwise
   
    if(len(motifs)!=0): #if the motifs is non empty, 
    
      isomorphic = False
      for motif in motifs: ##we want to check in our motif s, if our new graph is isomorphic to any of out already included graph motifs 
       
        if nx.is_isomorphic(motif, generatedGraph): #if there is a motif in motifs, that is isomorphic to our graph, we should not add it
          isomorphic = True
          break

      if not isomorphic: #if after finishing the loop, we get that we have found no motif, isomorphic to our graph, that means our graph is a new motif
        motifs.append(generatedGraph)

    else: #meaning -- if the set is empty, we need to add our graph as a motif 
      motifs.append(generatedGraph)

 return motifs
def printMotifs(motifsList,n):
  print(f"n={n}")
  print(f"count={len(motifsList)}")
  i = 1
  for g in motifsList:
    print(f"#{i}")
    for u,v in g.edges():
      print(f"{u+1} {v+1}")
    i = i + 1
def main():
  ##example input 
  n = 1
  motifs_all = motifsCreator(n)
  printMotifs(motifs_all,n)
if __name__=="__main__":
  main()
