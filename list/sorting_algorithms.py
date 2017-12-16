# original approach:
def bubble_sort(lst):
    for _ in range(len(lst)):
        curr = 0
        while curr < len(lst) - 1:
            if lst[curr] > lst[curr + 1]:
                tmp = lst[curr + 1]
                lst[curr + 1] = lst[curr]
                lst[curr] = tmp
            curr += 1

    return lst

# better approach:
# last element after first iteration will be biggest so we can
# ignore the last elements after each iteration.
def bubble_sort2(lst):
    """
    Every element is compared with next element and shuffle if next element is greater
    than the current element.
    :param lst: list of unsorted integer values
    :return: list of sorted integer values.
    """
    print(lst)
    for big in range(len(lst), 0, -1):
        print('Big ' + str(big))
        for curr in range(big - 1):
            print(' curr ' + str(curr))
            if lst[curr] > lst[curr + 1]:
                tmp = lst[curr + 1]
                lst[curr + 1] = lst[curr]
                lst[curr] = tmp

    return lst


def selection_sort(lst):
    """
    selection sort improves over the bubble sort by just shuffle element in
    one pass.
    :param lst: List of unsorted integer values to sort
    :return: List of sorted integer values
    """
    for outer in range(len(lst)):
        print(' Outer ' + str(lst[outer]))
        min1 = lst[outer]
        loc = outer
        for curr in range(outer + 1, len(lst), 1):
            print(' Current ' + str(lst[curr]))
            if lst[curr] < min1:
                loc = curr
                min1 = lst[curr]
        print(str(loc) + ' : ' + str(min1))
        tmp = lst[outer]
        lst[outer] = min1
        lst[loc] = tmp

    return lst


def insertion_sort(lst):
    """
    Pseudo code:
    for ele1 in unsorted array.
        val = unsorted[ele1]
        for ele2 in sub list - start till position of ele1
            if sub-list[ele2 - 1] greater than sub-list[ele]:
                sub-list[ele] = sub[ele - 1]
            else:
                sub-list[ele] = val
    return sub



    :param lst:
    :return:
    """

    for outer in range(len(lst)):
        val = lst[outer]
        curr = outer - 1
        print('outer value: ' + str(val))

        while curr >= 0:
            print('inner value : ' + str(lst[curr]))
            if lst[curr] > val:
                lst[curr + 1] = lst[curr]
            else:
                break

            curr -= 1


        lst[curr + 1] = val
        print(lst)

    return lst


if __name__ == '__main__':
    l1 = [24, 17, 99, 57, 1, 84]

    # print(bubble_sort(l1))

    # print(bubble_sort2(l1))
    # print(selection_sort(l1))

    print(insertion_sort(l1))
