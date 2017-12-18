

def sum_of_num_tgt(lst, tgt):
    seen = set()
    for num in lst:
        lookup = tgt - num
        if lookup in seen:
            return True
        else:
            seen.add(num)

    return False

def missing_pair(lst):
    missing_ele = 0

    for ele in lst:
        missing_ele ^= ele

    return missing_ele

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]

    print(sum_of_num_tgt(lst, 100))

    lst2 = [1, 2, 3, 1, 2]

    print(missing_pair(lst2))
