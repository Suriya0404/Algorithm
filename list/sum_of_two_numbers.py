
def find_missing(list1, list2):
    return set(list1) - set(list2)

def find_missing(list1, list2):

    for curr in range(len(list1)):
        if curr not in list2:
            return False




def sum_of_two_number(a_num_list):
    num_list, total = a_num_list
    sean = set()
    final = set()

    for curr in range(len(num_list) - 1):
        curr_num = num_list[curr]

        target = total - curr_num

        if target not in sean:
            sean.add(curr_num)
        else:
             final.add((min(target, curr_num), max(target, curr_num)))

    print('\n'.join(map(str, list(final))))
    return final

def sentence_reversal(sent):
    words = sent.split(' ')
    rev_words = words[::-1]
    return ' '.join(map(str, rev_words))

if __name__ == '__main__':
    num_list = [[1, 2, 3, 4, 5, 1, 2, 3], 4]
    sum_of_two_number(num_list)
    print(sentence_reversal('This is suriya'))