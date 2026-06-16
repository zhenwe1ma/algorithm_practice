from typing import Hashable


Node = Hashable
Graph = dict[Node, dict[Node, int]]


def dijkstra(graph: Graph, start: Node) -> dict[Node, float]:
    """
    Dijkstra shortest path algorithm without heapq.

    Input:
        graph: Weighted directed graph.
               Example: {"A": {"B": 5, "C": 2}, "B": {"D": 1}}
        start: Start node.

    Output:
        A dict from node to shortest distance from start.

    Note:
        Edge weights must be non-negative.
        Unreachable nodes keep distance float("inf").
    """

    nodes = set(graph.keys())
    print(nodes)
    
    for neighbors in graph.values():
        nodes.update(neighbors.keys())
        print(neighbors.keys())
        
    nodes.add(start)
    print(nodes)

    distances = {node: float("inf") for node in nodes}
    distances[start] = 0
    visited = set()

    while len(visited) < len(nodes):
        current = None
        current_distance = float("inf")

        for node in nodes:
            if node not in visited and distances[node] < current_distance:
                current = node
                current_distance = distances[node]

        if current is None:
            break

        visited.add(current)

        for neighbor, weight in graph.get(current, {}).items():
            new_distance = distances[current] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


def main() -> None:
    graph = {
        "A": {"B": 5, "C": 2},
        "B": {"D": 4},
        "C": {"B": 1, "D": 7},
        "D": {},
    }

    start = "A"
    distances = dijkstra(graph, start)

    for node in sorted(distances):
        print(f"{start} -> {node}: {distances[node]}")


if __name__ == "__main__":
    main()
