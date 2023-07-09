# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def is_valid_neighbour(cell_coords: List[int], visited: set) -> bool:
            return (
                (cell_coords[0] >= 0 and cell_coords[0] < len(maze))
                and (cell_coords[1] >= 0 and cell_coords[1] < len(maze[0]))
                and ((cell_coords[0], cell_coords[1])) not in visited
                and maze[cell_coords[0]][cell_coords[1]] != "+"
            )

        def is_exit_cell(cell_coords: List[int], cell_value: str) -> bool:
            empty_cell = cell_value == "."
            not_entrance = [cell_coords[0], cell_coords[1]] != entrance
            boarder_cell = cell_coords[0] in [0, len(maze) - 1] or cell_coords[1] in [
                0,
                len(maze[0]) - 1,
            ]
            return empty_cell and not_entrance and boarder_cell

        def bfs(graph: List[List[str]], start_cell: List[int]) -> int:
            queue = deque()
            queue.appendleft((start_cell[0], start_cell[1], 0))
            visited = set()
            visited.add((start_cell[0], start_cell[1]))
            while len(queue) > 0:
                print(queue[-1])
                current_cell = queue.pop()
                """
                during our level traversal , once we touch any border cell (exit),
                we should return immediately the steps from entrance cell to it
                the steps is simply our current level
                """
                if is_exit_cell(current_cell, graph[current_cell[0]][current_cell[1]]):
                    return current_cell[-1]  # current cell level
                next_level_4_neighbours = [
                    (current_cell[0] - 1, current_cell[1], current_cell[-1] + 1),
                    (current_cell[0] + 1, current_cell[1], current_cell[-1] + 1),
                    (current_cell[0], current_cell[1] - 1, current_cell[-1] + 1),
                    (current_cell[0], current_cell[1] + 1, current_cell[-1] + 1),
                ]
                for neighbour in next_level_4_neighbours:
                    if is_valid_neighbour(neighbour, visited):
                        # is current cell valid cell to be added to BFS queue ?
                        visited.add((neighbour[0], neighbour[1]))
                        queue.appendleft(neighbour)

            return -1

        return bfs(maze, entrance)


s = Solution()
print(
    s.nearestExit(
        maze=[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], entrance=[1, 0]
    )
)
print(
    s.nearestExit(
        maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
        entrance=[1, 2],
    )
)
