# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.maxPath = float('-inf')

    def maxPathSum(self, root):
        self.maxPathSol(root)
        return self.maxPath

    def maxPathSol(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        left_path = self.maxPathSol(root.left)
        right_path = self.maxPathSol(root.right)

        curr_path = root.val + left_path + right_path

        self.maxPath = max(self.maxPath, curr_path)

        return root.val + max(left_path, right_path)

    
if __name__ == '__main__':
    n1 = TreeNode(-10)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.right = n3
    n1.left = n2
    n2.left = None
    n2.right = None
    n3.right = n5
    n3.left = n4

    sol = Solution()
    # sol.maxPathSum(n1)

    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)

    a1.left = a2
    a1.right = a3

    b1 = TreeNode(-3)

    c1 = TreeNode(-1)
    c2 = TreeNode(2)
    c1.left = c2

    sol.maxPathSum(c1)
    print(sol.maxPath)


