from collections import deque

class Node:
    '''s'''
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node: Node):
    '''s'''
    if node is None:
        return []
    res = []
    q = deque()
    q.append(node)
    while q:
        cur = q.popleft()
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
        res.append(cur.value)

    return res
