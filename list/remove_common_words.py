class Solution(object):

    def remove_common_words(self, sent1=None, sent2=None):

        if not sent1 and not sent2 and sent1 is None and sent2 is None:
            return None
        elif not sent1 and sent2:
            return list(set(sent2.split()))
        elif sent1 and not sent2:
            return list(set(sent1.split()))

        word_check = {}

        for word in sent1.split():
            word_check[word] = 1

        for word in sent2.split():
            if word in word_check:
                word_check[word] -= 1
            else:
                word_check[word] = 1

        return [word for word, val in word_check.items() if val == 1]


if __name__ == '__main__':
    sol = Solution()
    result = sol.remove_common_words('This is test message suriya', 'This is another test message for today')
    print(result)
    result = sol.remove_common_words('This is test message suriya', '')
    print(result)
    result = sol.remove_common_words('', 'This is another test message for today')
    print(result)
