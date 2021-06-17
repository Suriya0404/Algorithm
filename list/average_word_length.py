from __future__ import division


class Solution(object):

    def average_word_len(self, sent):
        if not sent:
            return 0

        word_list = sent.split()
        return sum([(len(word)) for word in word_list]) // len(word_list)


if __name__ == '__main__':
    sol = Solution()
    print(sol.average_word_len('This another test message'))
    print(sol.average_word_len(''))
