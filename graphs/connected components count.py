# https://structy.net/problems/connected-components-count


def dfs(graph: dict, start: int, visited: set) -> bool:
    if start in visited:
        return False
    visited.add(start)
    for neighbour in graph[start]:
        dfs(graph, neighbour, visited)
    return True


def connected_components_count(graph: dict) -> int:
    res = 0
    visited = set()
    for node in graph:
        # start dfs traversal
        if dfs(graph, node, visited):
            res += 1
    return res


tests = [
    {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]},
    {1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]},
    {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]},
    {},
    {0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []},
]
for test in tests:
    print(connected_components_count(test))
