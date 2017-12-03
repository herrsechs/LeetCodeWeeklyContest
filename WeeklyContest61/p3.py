def deleteAndEarn(nums):
    nums.sort()
    plist = []
    p = (0, 0)
    for i in nums:
        if p[0] == 0:
            p[0], p[1] = i, i
            continue
        if i == p[0]:
            p[1] += i
        else:
            plist.append(p)
            p[0], p[1] = i, i
