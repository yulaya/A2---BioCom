import itertools
import networkx as nx

def extractGraph(graph, n):
  "input string of graph is expected to be lines, where each line contains two numbers, u and v, such that"
  "an edge u->v exists in the graph"
  "return the ID of the graph"
  G = nx.DiGraph()
  G.add_nodes_from(range(n))

  for line in graph.strip().split('\n'):
    if line.strip():
      uv = line.strip().split()
      u = int(uv[0])
      v = int(uv[1])
      G.add_edge(u-1,v-1)
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
def MotifsNdSubgraphs(graph, n):
  "input string of graph is expected to be lines, where each line contains two numbers, u and v, such that"
  "an edge u->v exists in the graph"
  "return motif and subgraph description of the graph"
  "n is the size of the subgraphs we want to find"
  G = extractGraph(graph, n)
  subgraphs = []
  nodes = G.nodes()
  
  for node_subset in itertools.combinations(nodes, n):
    nG = G.subgraph(node_subset)
    edges = nG.edges()
    ## according to the output format, graphs should be described by their edges, therefore we don't want to include edgeless grapsh
    if nG.number_of_edges() == 0:
      continue
    for r in range(1, len(edges)+1):
      for edge_subset in itertools.combinations(edges, r):
        subG = nx.DiGraph()
        subG.add_nodes_from(node_subset)
        subG.add_edges_from(edge_subset)
        if subG.number_of_edges() == 0:
          continue
        subgraphs.append(subG)
  
  motifs = motifsCreator(n) ##cretaes list of all motifs of size n
  numMotifs = len(motifs)
  motifApearances = []
  for graph in subgraphs:
    if not nx.is_weakly_connected(graph): #since all motifs are weakly connected, if the graph is not weakly connected, then it includes none of the motifs of size n
      continue
    ## if the graph is weakly connected:
    for i, motif in enumerate(motifs):
      if (nx.is_isomorphic(graph, motif)): ## we go over each subgraph, and for each subgraph, check if it is isomorphic to any motif
      #if graph is isomorphic to motif i, then we should update, that it has appeared. 
        motifApearances.append(i) #if some subgraph, is isomorphic to some motif, then we should add that that motif appeared.
        continue #since all motifs are non ismorphoc to each other, if our subgraph is isomorphic to one motif, then it is only ismorphic to that one
  return subgraphs, motifApearances, numMotifs
  
def printMotifApearancesAndSubgraphsToFile(motifsApearances,subgraphs,numMotifs,n,filename = "output.txt"):
  with open(filename, "w") as f:
    f.write(f"n={n}\n")
    for i,g in enumerate(subgraphs):
      f.write(f"#{i+1}\n") #print the "index" of the subgraph, and then the subgraph
      for u,v in g.edges():
        f.write(f"{u+1} {v+1}\n")
    #after printing the subgrpah, we want to print which motifs appear
    motifCount = [0]*numMotifs
    for j in motifsApearances:
      motifCount[j] = motifCount[j]+1
    for k in range (numMotifs):
        f.write(f"Motif #{k+1}:{motifCount[k]}\n")


def main():
  ##example input 
  n = 3
  graph = """
          1 2 
          1 3
          2 3
          2 1
          3 1
          3 2
          """
  sG,mA,nM = MotifsNdSubgraphs(graph,n)
  printMotifApearancesAndSubgraphsToFile(mA,sG,nM,n,filename = "file.txt")
if __name__=="__main__":
  main()
