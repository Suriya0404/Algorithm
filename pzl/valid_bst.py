# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        root_list = []

        if not root:
            return True

        root_list.append(root)

        for root in root_list:
            if root.left:
                if (root.left.val >= root.val) or not root.left.val:
                    return False
                else:
                    root_list.append(root.left)

            if root.right:
                if (root.right.val <= root.val) or not root.right.val:
                    return False
                else:
                    root_list.append(root.right)

        return True


if __name__ == '__main__':

    sol = Solution()

    # [10, 5, 15, null, null, 6, 20]
    # Expected: False
    # returns: True

    sol.