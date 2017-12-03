def monotoneIncreasingDigits(N):
    """
    Given a non-negative integer N, find the largest number that is less than or equal to N 
    with monotone increasing digits.
    (Recall that an integer has monotone increasing digits 
    if and only if each pair of adjacent digits x and y satisfy x <= y.)

    Example 1:
    Input: N = 10
    Output: 9
    Example 2:
    Input: N = 1234
    Output: 1234
    Example 3:
    Input: N = 332
    Output: 299
    :param N: 
    :return: 
    """
    sN = str(N)
    backn = 0
    res = []
    for i in range(len(sN)):
        if i == 0:
            res.append(sN[i])
            continue
        num = int(sN[i])
        lastn = int(sN[i-1])
        if num > lastn:
            res.append(sN[i])
            backn = 0
        elif num == lastn:
            res.append(sN[i])
            backn += 1
        else:
            if backn == 0:
                l = int(res.pop())
                res.append(str(l-1))
            else:
                for j in range(backn):
                    res[i-j-1] = '9'
                res[i-backn-1] = str(int(res[i-backn-1])-1)
            for j in range(i, len(sN)):
                res.append('9')
            break
    res = int(''.join(res))
    return res

if __name__ == '__main__':
    print monotoneIncreasingDigits(668841)
