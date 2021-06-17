class Solution(object):

    def flatten_nested_list(self, in_list):
        for item in in_list:
            if isinstance(item, list):
                for nest_item in self.flatten_nested_list(item):
                    yield nest_item
            else:
                yield item


if __name__ == '__main__':
    nests = [1, 2, [3, 4, [5], ['hi']], [6, [[[7, 'hello']]]]]

    sol = Solution()
    print(list(sol.flatten_nested_list(nests)))

