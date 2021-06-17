class Solution(object):

    def count_friends(self, friend_graph):

        friend_cnt = {}

        for assoc in friend_graph:
            if len(assoc) not in (1, 2):
                continue
            elif len(assoc) == 2:
                for friend in assoc:
                    friend_cnt[friend] = friend_cnt.get(friend, 0) + 1
            elif len(assoc) == 1:
                friend_cnt[assoc[0]] = friend_cnt.get(assoc[0], 0)

        return friend_cnt


if __name__ == '__main__':
    sol = Solution()

    input1 = [['A', 'B'], ['B', 'C'], ['B', 'D'], ['E']]
    print(sol.count_friends(input1))

    input2 = [['A', 'B'], ['B', 'C'], ['B', 'D'], ['E', 'C'], ['E']]
    print(sol.count_friends(input2))
