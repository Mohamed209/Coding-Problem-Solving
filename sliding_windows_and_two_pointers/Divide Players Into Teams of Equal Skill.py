# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill
from typing import List

"""
for this problem , valid skill arrays must have these example shapes 
[1,2,3,4]
[20,21,22,23]
[1,2,3,4,5,6]
[101,102,103,104,105,106]
simply must be consecutive n skills
so sorting + two pointers will help us discover this pattern in the skill array
"""


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        teams_chem = []
        ref_team = [skill[left], skill[right]]
        while left < right:
            if skill[left] + skill[right] == ref_team[0] + ref_team[1]:
                teams_chem.append(skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1
        return sum(teams_chem)
