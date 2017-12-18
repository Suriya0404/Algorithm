from collections import defaultdict


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        trav = {root: 0}
        output = defaultdict(list)

        queue = [root]
        output[0].append(root.val)

        for root in queue:
            if root.left is not None:
                trav[root.left] = trav[root] + 1
                output[trav[root] + 1].append(root.left.val)
                queue.append(root.left)

            if root.right is not None:
                trav[root.right] = trav[root] + 1
                output[trav[root] + 1].append(root.right.val)
                queue.append(root.right)

        print(output)
        return [i for i in output.values()]