# https://structy.net/problems/island-count
def dfs(r, c, grid, visited):
    if (
        r < 0
        or r >= len(grid)
        or c < 0
        or c >= len(grid[0])
        or (r, c) in visited
        or grid[r][c] == "W"
    ):
        return False
    visited.add((r, c))
    dfs(r - 1, c, grid, visited)
    dfs(r + 1, c, grid, visited)
    dfs(r, c - 1, grid, visited)
    dfs(r, c + 1, grid, visited)
    return True


def island_count(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    res = 0
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, grid, visited):
                res += 1
    return res


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
    [
        ["W", "W"],
        ["W", "W"],
        ["W", "W"],
    ],
]
for test in tests:
    print(island_count(test))
