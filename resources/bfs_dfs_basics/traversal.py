"""
basics of DFS/BFS traversal
"""
from collections import deque

graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}


def dfs(graph: dict, start: str) -> None:
    print(start)
    for neighbour in graph[start]:
        dfs(graph=graph, start=neighbour)
    return


def bfs(graph: dict, start: str):
    queue = deque()
    queue.appendleft(start)
    while len(queue) > 0:
        print(queue[-1])
        start = queue.pop()
        for neighbour in graph[start]:
            queue.appendleft(neighbour)

    return


dfs(graph=graph, start="a")
print("#" * 5)
bfs(graph=graph, start="a")
