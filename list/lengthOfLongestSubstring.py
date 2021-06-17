

def lengthOfLongestSubstring_x(s):
    # create a for loop for length of string and decrement it.
    # From the starting of word till length get the word
    # check if word has any repeating letters by creating a set
    # if len of set and len of word same then return len of word
    # Move next character + len < length of word continue above algorithm.

    total_len = len(s)

    if total_len == 0:
        return 0
    elif total_len == 1:
        return 1

    # print('Total length: ' + str(total_len))
    for word_len in range(total_len, -1, -1):
        # print('word_len: ' + str(word_len))
        idx = 0

        while idx + word_len <= total_len:
            # print('idx: ' + str(idx))
            # print('word_len: ' + str(word_len))

            sub_word = s[idx: idx + word_len]
            uni_word = set(sub_word)
            # print('sub word: ' + sub_word)
            # print('uni word: ' + str(uni_word))
            if len(sub_word) == len(uni_word):
                # print('word: ' + sub_word)
                return word_len
            idx += 1


def lengthOfLongestSubstring(s):
    # Internet solution
    # Set two pointers - running index pointer and max of non repeating index (start index)
    # diff between these pointers are collected and stored in a variable and returned
    found = {}
    start_index = max_length = 0

    for idx, let in enumerate(s):
        if let in found:
            start_index = max(start_index, found[let] + 1)

        found[let] = idx
        max_length = max(max_length, idx - start_index + 1)

    return max_length


result = {}
for string in ['abcabcbb', 'bbbbb', 'ppwwkew', 'wcabcdeghi', 'bpfbhmipx', 'tmmzuxt', 'AABGAKGIMN', 'stackoverflow']:
    result[string] = lengthOfLongestSubstring(string)
print(result)