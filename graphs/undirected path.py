# https://structy.net/problems/undirected-path

# convert edges to graph (adj list format)
def build_graph(edges):
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


def has_path(graph: dict, src: str, dst: str) -> bool:
    if src == dst:
        return True
    for neighbour in graph[src]:
        if (
            neighbour in visited
        ):  # since the graph is undirected , need to watch out cycles !
            continue
        visited.add(neighbour)
        if has_path(graph, neighbour, dst):
            return True
    return False


def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path(graph, src=node_A, dst=node_B)


visited = set()
edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]
print(undirected_path(edges, "j", "m"))  # -> True
visited = set()
edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]
print(undirected_path(edges, "m", "j"))  # -> True
visited = set()
edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]
print(undirected_path(edges, "l", "j"))  # -> True
visited = set()
edges = [
    ("b", "a"),
    ("c", "a"),
    ("b", "c"),
    ("q", "r"),
    ("q", "s"),
    ("q", "u"),
    ("q", "t"),
]
print(undirected_path(edges, "r", "b"))  # -> False
