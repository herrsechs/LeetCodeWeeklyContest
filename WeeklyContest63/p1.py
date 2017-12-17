# coding=utf-8
def minCostClimbingStairs(cost):
    """
    On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

    Once you pay the cost, you can either climb one or two steps.
     You need to find minimum cost to reach the top of the floor,
    and you can either start from the step with index 0, or the step with index 1.

    Example 1:
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
    Example 2:
    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
    :param cost: list[int]
    :return: 
    Dynamic Programming
    动态规划问题
    """
    if len(cost) < 2:
        return cost[0]

    prev1 = cost[1]
    prev2 = cost[0]

    for i in range(2, len(cost)):
        cur = cost[i] + min([prev1, prev2])
        prev2 = prev1
        prev1 = cur
    return min([prev1, prev2])

if __name__ == '__main__':
    print minCostClimbingStairs([0, 1, 1, 0])
