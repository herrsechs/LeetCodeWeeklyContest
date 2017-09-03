def findSecondMinimumValue(self, root):
    if root is None:
        return -1
    elif root.left is None and root.right is None:
        return -1

    sml = root.val
    ret = float('Inf')
    nlst = [root.left, root.right]
    while len(nlst) > 0:
        ln, rn = nlst.pop(0), nlst.pop(0)
        lv, rv = ln.val, rn.val
        if lv > sml and lv < ret:
            ret = lv
        elif ln.left is not None and ln.right is not None:
            nlst.append(ln.left)
            nlst.append(ln.right)

        if rv > sml and rv < ret:
            ret = rv
        elif rn.left is not None and rn.right is not None:
            nlst.append(rn.left)
            nlst.append(rn.right)

    if ret == float('Inf'):
        return -1
    else:
        return ret


def trimBST(root, L, R):
    """
        pair = [parent, node, pos(1=left, 2=right, 0=root)]
    """
    nlst = [[None, root, 0]]
    while len(nlst) > 0:
        pair = nlst.pop(0)
        parent = pair[0]
        node = pair[1]
        pos = pair[2]
        v = node.val
        if v < L:
            node.left = None
            if parent is not None:
                if pos == 1:
                    parent.left = node.right
                    if parent.left is not None:
                        nlst.append([parent, parent.left, 1])
                elif pos == 2:
                    parent.right = node.right
                    if parent.right is not None:
                        nlst.append([parent, parent.right, 2])
            else:
                root = root.right
                if root is not None:
                    nlst.append([None, root, 0])
        elif v > R:
            node.right = None
            if parent is not None:
                if pos == 1:
                    parent.left = node.left
                    if parent.left is not None:
                        nlst.append([parent, parent.left, 1])
                elif pos == 2:
                    parent.right = node.left
                    if parent.right is not None:
                        nlst.append([parent, parent.right, 2])
            else:
                root = root.left
                if root is not None:
                    nlst.append([None, root, 0])
        else:
            if node.left is not None:
                nlst.append([node, node.left, 1])
            if node.right is not None:
                nlst.append([node, node.right, 2])
    return root


def maximunSwap(num):
    dlst = []
    dnum = num
    while dnum > 0
        dlst.append(dnum % 10)
        dnum = dnum / 10
    dlst.reverse()