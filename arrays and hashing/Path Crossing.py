# https://leetcode.com/problems/path-crossing
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        origin = (0, 0)
        visited = set()
        visited.add(origin)
        current_position = [origin[0], origin[1]]
        for step in path:
            if step == "N":
                current_position[1] += 1
            elif step == "S":
                current_position[1] -= 1
            elif step == "E":
                current_position[0] += 1
            else:
                current_position[0] -= 1
            if tuple(current_position) in visited:
                return True
            else:
                visited.add(tuple(current_position))
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPathCrossing("NES"))
    print(s.isPathCrossing("NESWW"))
