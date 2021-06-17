class Solution(object):

    def count_of_letters_in_sentence(self, letter, sentence):
        cnt = 0
        for let in sentence:
            if let == letter:
                cnt += 1

        return cnt

if __name__ == '__main__':
    sol = Solution()
    print(sol.count_of_letters_in_sentence('c', 'abcdcccssdd aacccsrdds'))
