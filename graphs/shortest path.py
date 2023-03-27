# https://structy.net/problems/shortest-path

from collections import deque
from typing import List


def build_graph(edges: List[List[str]]) -> dict:
    graph = {}

    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


def bfs(graph: dict, start: str, end: str) -> int:
    queue = deque()
    visited = set()
    queue.appendleft((start, 0))
    shortest = int(1e9)
    while len(queue) > 0:
        current = queue.pop()
        visited.add(current[0])
        curr_dist = current[-1]
        for neighbour in graph[current[0]]:
            if neighbour in visited:
                continue
            if neighbour == end:
                if shortest > curr_dist:
                    shortest = curr_dist + 1
            queue.appendleft((neighbour, current[-1] + 1))
    if shortest == int(1e9):
        return -1
    return shortest


def shortest_path(edges: List[List[str]], node_A: str, node_B: str) -> int:
    graph = build_graph(edges)
    return bfs(graph, node_A, node_B)


tests = [
    [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]],
    [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]],
    [
        ["a", "c"],
        ["a", "b"],
        ["c", "b"],
        ["c", "d"],
        ["b", "d"],
        ["e", "d"],
        ["g", "f"],
    ],
    [
        ["a", "c"],
        ["a", "b"],
        ["c", "b"],
        ["c", "d"],
        ["b", "d"],
        ["e", "d"],
        ["g", "f"],
    ],
    [
        ["a", "c"],
        ["a", "b"],
        ["c", "b"],
        ["c", "d"],
        ["b", "d"],
        ["e", "d"],
        ["g", "f"],
    ],
    [
        ["c", "n"],
        ["c", "e"],
        ["c", "s"],
        ["c", "w"],
        ["w", "e"],
    ],
    [
        ["c", "n"],
        ["c", "e"],
        ["c", "s"],
        ["c", "w"],
        ["w", "e"],
    ],
    [
        ["m", "n"],
        ["n", "o"],
        ["o", "p"],
        ["p", "q"],
        ["t", "o"],
        ["r", "q"],
        ["r", "s"],
    ],
]
start_end = [
    ("w", "z"),
    ("y", "x"),
    ("a", "e"),
    ("e", "c"),
    ("b", "g"),
    ("w", "e"),
    ("n", "e"),
    ("m", "s"),
]
for test, startend in zip(tests, start_end):
    print(shortest_path(test, *startend))
