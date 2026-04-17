'''a'''
class TreeNode:
    '''a'''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''a'''
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''a'''
        prev = None
        current = root

        while current:
            if current.val == key:
                break

            if key < current.val:
                prev = current
                current = current.left
            else:
                prev = current
                current = current.right
        else:
            return root

        if prev is None:
            if not current.left and not current.right:
                return None
            if not current.left:
                return current.right
            if not current.right:
                return current.left

        if current.left and current.right:
            succ_parent = current
            succ = current.right

            while succ.left:
                succ_parent = succ
                succ = succ.left

            current.val = succ.val

            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right

            return root


        if not current.left and not current.right:
            if prev.left == current:
                prev.left = None
            else:
                prev.right = None
            return root
        if not current.left:
            if prev.left == current:
                prev.left = current.right
            else:
                prev.right = current.right
            return root
        if not current.right:
            if prev.left == current:
                prev.left = current.left
            else:
                prev.right = current.left
            return root
