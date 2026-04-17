'''d'''
def pre_order(node):
    '''pre ord'''
    res = []
    def dfs(node):
        if node:
            res.append(node.data)
            dfs(node.left)
            dfs(node.right)

    dfs(node)
    return res


def in_order(node):
    '''in ord'''
    res = []
    def dfs(node):
        if node:
            dfs(node.left)
            res.append(node.data)
            dfs(node.right)

    dfs(node)
    return res

def post_order(node):
    '''post ord'''
    res = []
    def dfs(node):
        if node:
            dfs(node.left)
            dfs(node.right)
            res.append(node.data)

    dfs(node)
    return res
