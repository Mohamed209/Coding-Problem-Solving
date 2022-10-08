// https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        Map<Integer, Integer> map = new HashMap<>();
        return minCostClimbingStairs(map, cost, cost.length, 0);
    }

    public int minCostClimbingStairs(Map<Integer, Integer> map, int[] cost, int num, int result) {
        if (num == 0 || num == 1) {
            return result;
        }
        if (map.containsKey(num)) {
            return map.get(num);
        }
        int result1 = minCostClimbingStairs(map, cost, num - 1, cost[num - 1]);
        int result2 = minCostClimbingStairs(map, cost, num - 2, cost[num - 2]);

        result = result + Math.min(result1, result2);
        map.put(num, result);
        return result;
    }
}