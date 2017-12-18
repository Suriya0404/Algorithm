from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        trav = {root.val: 0}
        output = defaultdict(list)

        queue = [root]
        output[0].append(root.val)

        for root in queue:
            if root.left is not None:
                trav[root.left.val] = trav[root.val] - 1
                output[trav[root.val] - 1].append(root.left.val)
                queue.append(root.left)

            if root.right is not None:
                trav[root.right.val] = trav[root.val] + 1
                output[trav[root.val] + 1].append(root.right.val)
                queue.append(root.right)

        return [i for i in output.values()]

if __name__ == '__main__':
