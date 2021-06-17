class Solution(object):

    def shortest_word_distance(self, words: List[str], word1: str, word2: str) -> int:
        ptr_word1 = -1 * len(words)
        ptr_word2 = len(words)
        distance = len(words)

        for idx, word in enumerate(words):
            if word == word1:
                ptr_word1 = idx
            elif word == word2:
                ptr_word2 = idx

            distance = min(distance, abs(ptr_word1 - ptr_word2))
            print('ptr_word1: ' + str(ptr_word1))
            print('ptr_word2: ' + str(ptr_word2))
            print('distance: ' + str(distance))

        return distance


if __name__ == '__main__':
    lst_words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"

    sol = Solution()
    print(sol.shortest_word_distance(lst_words, word1, word2))
