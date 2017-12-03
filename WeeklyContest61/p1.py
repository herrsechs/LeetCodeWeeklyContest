def dailyTemperatures(temperatures):
    """
    Given a list of daily temperatures, produce a list that, for each day in the input, 
    tells you how many days you would have to wait until a warmer temperature. 
    If there is no future day for which this is possible, put 0 instead.
    For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73],
    your output should be [1, 1, 4, 2, 1, 1, 0, 0].

    Note: The length of temperatures will be in the range [1, 30000].
    Each temperature will be an integer in the range [30, 100].
    :param temperatures: 
    :return: 
    """
    res = [0 for i in temperatures]
    stack = []
    i = 0
    while i < len(temperatures):
        if len(stack) == 0 or temperatures[stack[-1]] >= temperatures[i]:
            stack.append(i)
            i += 1
        else:
            res[stack[-1]] = i - stack[-1]
            stack.pop()

    return res


if __name__ == '__main__':
    t1 = [89,62,70,58,47,47,46,76,100,70]
    print dailyTemperatures(t1)
