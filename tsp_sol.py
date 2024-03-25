from typing import Dict, List, Tuple
from itertools import permutations


def generate_routes(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[str]:
    nodes = list(graph.keys())
    nodes.remove(start)
    for route in permutations(nodes):
        yield (start,) + route + (start,)


def solve_travelling_salesman_prob(graph: Dict[str, Dict[str, int]], start: str):
    cal_distance = lambda route: sum(
        graph[start][stop] for start, stop in zip(route, route[1:])
    )
    shortest_path = min(generate_routes(graph, start), key=cal_distance)
    return shortest_path, cal_distance(shortest_path)


graph = {
    "A": {"B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30},
}

if __name__ == "__main__":
    shortest_path, shortest_dist = solve_travelling_salesman_prob(graph, "A")
    print(*shortest_path, sep=" -> ")
    print("Distance: ", shortest_dist)
