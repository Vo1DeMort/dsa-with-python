# NOTE: adjacency list
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E', 'C', 'A']
graph['C'] = ['A', 'B', 'E', 'F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']
print(graph)

# NOTE: adjacency matirx
matrixElements = sorted(graph.keys())
cols = rows = len(matrixElements)

adjacencyMatrix = [[0 for x in range(rows)] for y in range(cols)]
edgesList = []
for key in matrixElements:
    for neighbor in graph[key]:
        edgesList.append((key, neighbor))
print(edgesList)

for edge in edgesList:
    indexOfFirstVertex = matrixElements.index(edge[0])
    indexOfSecondVertex = matrixElements.index(edge[1])
    adjacencyMatrix[indexOfFirstVertex][indexOfSecondVertex] = 1
print(adjacencyMatrix)
