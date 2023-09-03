# https://leetcode.com/problems/keys-and-rooms
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set([0])

        # dfs helper
        def dfs(graph, start) -> None:
            for room in graph[start]:
                if room in visited_rooms:
                    continue
                visited_rooms.add(room)
                dfs(graph=graph, start=room)
            return

        dfs(graph=rooms, start=0)
        return len(visited_rooms) == len(rooms)


s = Solution()
print(s.canVisitAllRooms(rooms=[[1], [2], [3], []]))
print(s.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]))
