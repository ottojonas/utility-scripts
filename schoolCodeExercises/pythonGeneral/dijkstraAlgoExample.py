import heapq


def calculateDistances(graph, startingVertex):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[startingVertex] = 0

    pq = [(0, startingVertex)]
    print(pq)
    while len(pq) > 0:
        currentDistance, currentVertex = heapq.heappop(pq)

        if currentDistance > distances[currentVertex]:
            continue
        for neighbor, weight in graph[currentVertex].items():
            distance = currentDistance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                print(pq)
    return distances


exampleGraph = {
    "U": {"V": 2, "W": 5, "X": 1},
    "V": {"U": 2, "X": 2, "W": 3},
    "W": {"V": 3, "U": 5, "X": 3, "Y": 1, "Z": 5},
    "X": {"U": 1, "V": 2, "W": 3, "Y": 1},
    "Y": {"X": 1, "W": 1, "Z": 1},
    "Z": {"W": 5, "Y": 1},
}
print(calculateDistances(exampleGraph, "X"))
