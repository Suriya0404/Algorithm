# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        nodes = [(root, 1)]
        max_level = {1: root.val}

        for node, level in nodes:
            if level in max_level:
                max_level[level] += node.val
            else:
                max_level[level] = node.val

            if node.left:
                nodes.append((node.left, level + 1))

            if node.right:
                nodes.append((node.right, level + 1))

        lst = sorted(max_level.items(), key=lambda k: k[1], reverse=True)

        return lst[0][0]

    def maxLevelSumRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def bfs_inorder_traversal(node, level):
            if node.left:
                bfs_inorder_traversal(node.left, level + 1)

            dd[level] += node.val

            if node.right:
                bfs_inorder_traversal(node.right, level + 1)

        dd = defaultdict(int)
        bfs_inorder_traversal(root, 1)

        return max(dd, key=dd.get)