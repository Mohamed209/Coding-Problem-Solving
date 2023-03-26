# https://structy.net/problems/largest-component
from typing import List


def dfs(graph: dict, start: int, visited: set, curr_path: List) -> int:
    if start in visited:
        return 0
    visited.add(start)
    curr_path.append(1)
    for neighbour in graph[start]:
        dfs(graph, neighbour, visited, curr_path)
    return len(curr_path)


def largest_component(graph: dict) -> int:
    visited = set()
    curr_path = []
    largest = 0
    for node in graph:
        # start dfs traversal
        size = dfs(
            graph, node, visited, curr_path
        )  # dfs should return size of the traversal
        if size > largest:
            largest = size
        curr_path.clear()
    return largest


tests = [
    {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]},
    {1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]},
    {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]},
    {},
    {0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []},
]
for test in tests:
    print(largest_component(test))
