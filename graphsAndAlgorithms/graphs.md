# graph is a set of finite number of vertices( nodes) and edges
# edges are the links between vertices
# each edge in graph joins tow distinct nodes

# graph is a formal mathematical representation of a network


# loop
 - don't really understand about this

# degree of a vertex/ node
 - total number of edges

# adjacency

# path

# leaf vertex (pendant vertex)
 - if the node has only one degree

## types of graph
 1. directed graph (have direction arrows)
 2. undirected graph (no direction arrows)
 
# directed graph
- indegree : no of edges that come into a vertex
- outdegree : no of edges that go out of a vertex
- isolated vertex : if zero edge
- source vertex : if indegree is zero
- sink vertex : if outdegree is zero

# directed acyclic graph - DAG 
- graph with no cycle
## a 'cycle' is formed when the starting node of the first edge is equal to the ending node of the last edge in a sequence

# weighted graph
- a graph which has numeric weight for the edges 
- could be either directed or undirected graph

# bipartite graph (aka bigraph)
- all the nodes of the graph can be divided into two sets
- edges connect the nodes from one set to nodes from another set

# graph representation
- can be done with 
1. adjacency list : based on linked list
2. adjacency matrix


# adjacency list
- if two nodes has a direct connection between them ,they are adjacent
- with linked list , adjacent nodes to the nodes are stored

# adjacency matrix
- represented with (Vertex x Vertex)
- edge is represented with binary value

# graph traversal
- breadth-first-search BFS
- depth-first-search DFS

-breadth : width

# breadth-first-search
- similar to order traversal in tree
- sibling nodes are visited first
- works level by level
- first visit the node, then look up all neighbors
- visit those neighbors one by one ,while adding their neighbors to the list as well
- no vertex(node ) is visited twice
- queue is used to store nodes to be visited

# depth-first-search
- similar to preorder traversal in tree
- child nodes are visited first rather than siblings
- visit the adjacent nodes , if the edge leads to a visited one, back to the current node

# minimum spanning tree : MST









































