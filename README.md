
# Biological Computation  Exercise #2

This repository includes 2 code files -- Q1, and Q2. 

Q1 takes as input a positive integer *n*, and generates all unique connected subgraphs of size *n*

Q2 take as input a description of a graph G by its edges, and a positive integer n -- and counts how many of each motif of size n, are subgraphs of G. 
        
python code. makes use of *itertools* and *networkx* 

## Weakly Connected Digraph


A weakly connected digraph is a directed graph in which it is possible to reach any node starting from any other node by traversing edges in some direction (i.e., not necessarily in the direction they point). The nodes in a weakly connected digraph therefore must all have either outdegree or indegree of at least 1. The numbers of nonisomorphic simple weakly connected digraphs on n=1, 2, ... nodes are 1, 2, 13, 199, 9364, ... ([OEIS A003085](https://oeis.org/A003085)).

![Weakly Connected Digraph -- wolfram ](https://mathworld.wolfram.com/images/eps-svg/WeaklyConnectedDigraphs_700.svg)

see [Weakly Connected Digraph](https://mathworld.wolfram.com/WeaklyConnectedDigraph.html)

Each unique (nonisomorphic) digraph of size n, is a motif of size n. 

as mentioned, since the growth of (Number of weakly connected digraphs with n unlabeled nodes.) as a function of (n) is very rapid, the runtime of the functions implemented in this repository, also grows rapidly. runtime for an instance where n=6, approximated at 19-20 hours. 

-----
This code was written in a AI assisted environment (Google Colab -- gemini)
