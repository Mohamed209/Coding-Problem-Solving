# https://structy.net/problems/has-path
def has_path(graph: dict, src: str, dst: str) -> bool:
    if src == dst:
        return True
    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst):
            return True
    return False


graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}
print(has_path(graph, "f", "k"))  # True
graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}
print(has_path(graph, "f", "j"))  # False
graph = {
    "v": ["x", "w"],
    "w": [],
    "x": [],
    "y": ["z"],
    "z": [],
}
print(has_path(graph, "v", "w"))  # True
