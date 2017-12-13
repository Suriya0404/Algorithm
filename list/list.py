

def anagram_check(string1, string2):

    str1 = sorted(string1.replace(' ', '').lower())
    str2 = sorted(string2.replace(' ','').lower())

    return str1 == str2

def anagram_check2(string1, string2):

    str1 = sorted(string1.replace(' ', '').lower())
    str2 = sorted(string2.replace(' ', '').lower())

    ltr_cnt = {}

    for letter in str1:
        if letter in ltr_cnt:
            ltr_cnt[letter] += 1
        else:
            ltr_cnt[letter] = 1

    for letter in str2:
        if letter in ltr_cnt:
            ltr_cnt[letter] -= 1
        else:
            ltr_cnt[letter] = 1

    if sum(ltr_cnt.values()) > 0:
        return False

    return True


if __name__ == '__main__':
    print(anagram_check('clint Eastwood', 'old west action'))

    print(anagram_check2('clint Eastwood', 'old wst action'))


