"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.



"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        src_lst = []
        tgt_lst = []

        node = l1
        src_lst.append(node.val)
        while True:
            node = node.next
            src_lst.append(node.val)
            if not node.next:
                break

        node = l2
        tgt_lst.append(node.val)
        while True:
            node = node.next
            tgt_lst.append(node.val)
            if not node.next:
                break

        try:
            src_num = int(''.join(map(str, src_lst[::-1])))
            tgt_num = int(''.join(map(str, tgt_lst[::-1])))
        except Exception as ex:
            raise ex

        out_num = src_num + tgt_num

        out_lst = [num for num in str(out_num)]

        # for idx, out in enumerate(out_lst[::-1]):
        for idx in range(len(out_lst) - 1, -1, -1):
            num = out_lst[idx]
            node = ListNode(num)
            if idx != 0:
                node.next = ListNode(out_lst[idx - 1])

        return node


if __name__ == '__main__':
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    l12 = ListNode(2)
    l14 = ListNode(4)
    l13 = ListNode(3)

    l12.next = l14
    l14.next = l13

    l25 = ListNode(5)
    l26 = ListNode(6)
    l24 = ListNode(4)

    l25.next = l26
    l26.next = l24

    sol = Solution()
    node = sol.addTwoNumbers(l12, l25)

    while True:
        print(node.val)
        if not node.next:
            break
