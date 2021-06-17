class Solution(object):
    def replace_none(self, lst):
        if len(lst) == 0:
            return []

        if len(lst) == 1:
            return lst

        prev_val = lst[0]
        for idx, number in enumerate(lst[1:]):
            if number is None:
                lst[idx + 1] = prev_val
            else:
                prev_val = number

        return lst


if __name__ == '__main__':
    sol = Solution()
    print(sol.replace_none([12, None, None, None, 45, None]))