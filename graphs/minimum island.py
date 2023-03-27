# https://structy.net/problems/minimum-island

from typing import List, Union


def dfs(r: int, c: int, grid: List[List[str]], visited: set) -> Union[bool, int]:
    if (
        r < 0
        or r >= len(grid)
        or c < 0
        or c >= len(grid[0])
        or (r, c) in visited
        or grid[r][c] == "W"
    ):
        return False  # hey ! there is no islands here
    visited.add((r, c))
    return (  # found island , let us count its land
        1
        + dfs(r - 1, c, grid, visited)
        + dfs(r + 1, c, grid, visited)
        + dfs(r, c - 1, grid, visited)
        + dfs(r, c + 1, grid, visited)
    )


def minimum_island(grid: List[List[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    res = []
    for r in range(rows):
        for c in range(cols):
            ret = dfs(r, c, grid, visited)
            if ret:
                res.append(ret)
    return min(res) if res != [] else 0


tests = [
    [
        ["W", "L", "W", "W", "W"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "L", "W"],
        ["W", "W", "L", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "W"],
    ],
    [
        ["L", "W", "W", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["W", "L", "W", "L", "W"],
        ["W", "W", "W", "W", "W"],
        ["W", "W", "L", "L", "L"],
    ],
    [
        ["L", "L", "L"],
        ["L", "L", "L"],
        ["L", "L", "L"],
    ],
    [["W", "W"], ["L", "L"], ["W", "W"], ["W", "L"]],
]
for test in tests:
    print(minimum_island(test))
