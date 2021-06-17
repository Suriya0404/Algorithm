from collections import defaultdict, deque
class Solution(object):

    def ladderLengthBFS(self, beginWord, endWord, wordList):
        """

        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """

        # 1. Loop through the word list
        # 2. create a dict the pattern word as key and the associated word as list
        # 2. Loop through the starting word and find the pattern in dict and add its values to a queue
        # 3. Do a BFS and find the shortest path to the end word

        total_collect = defaultdict(list)

        for word in wordList:
            for num in range(len(beginWord)):
                key = word[:num] + '_' + word[num+1:]
                total_collect[key].append(word)

        print(str(total_collect))









    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        current_word = beginWord
        word_seen = set(wordList)
        if beginWord in word_seen:
            word_seen.remove(beginWord)
        word_cnt = 0
        word_len = 0

        if endWord not in wordList:
            return 0

        # for word_len in range(len(beginWord)):
        while word_len < len(beginWord):
            current_list = list(current_word)
            current_list[word_len] = '_'
            pattern_word = ''.join(current_list)

            for word in word_seen:
                word_lst = list(word)
                word_lst[word_len] = '_'
                word_lst_pattern = ''.join(word_lst)

                if pattern_word != word_lst_pattern:
                    continue
                else:
                    if word == endWord:
                        return word_cnt
                    else:
                        print('Word: ' + word)
                        word_seen.remove(word)
                        current_word = word
                        word_len = -1
                        word_cnt += 1
                        break
            word_len += 1

        return 0


if __name__ == '__main__':
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    # beginWord = "hot"
    # endWord = "dog"
    # wordList = ["hot", "dog"]

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]

    sol = Solution()
    # print(sol.ladderLength(beginWord, endWord, wordList))
