from collections import deque

graph = dict()
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']


def breadthFirstSearch(graph, root):
    visitedVertices = list()
    graphQueue = deque([root])
    visitedVertices.append(root)
    node = root

    while len(graphQueue) > 0:
        node = graphQueue.popleft()
        adjacentNodes = graph[node]

        remainingElements = set(adjacentNodes).difference(set(visitedVertices))

        if len(remainingElements) > 0:
            for element in sorted(remainingElements):
                visitedVertices .append(element)
                graphQueue.append(element)

    return visitedVertices


print(breadthFirstSearch(graph, 'A'))
