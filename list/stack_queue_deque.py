class Stack:
    def __init__(self):
        self.lst = []

    def pop(self):
        return self.lst.pop()

    def append(self, item):
        self.lst.append(item)

    def peek(self):
        return self.lst[len(self.lst) - 1]


class Queue:
    def __init__(self):
        self.lst = []

    def enqueue(self, item):
        self.lst.insert(0, item)

    def dequeue(self):
        self.lst.pop()

    def peek(self):
        return self.lst[len(self.lst) - 1]


# sequential search
def sequential_search(lst, ele):
    found = False
    curr = 0

    if len(lst) == 0:
        return False

    while curr < len(lst) and not found:
        if lst[curr] == ele:
            found = True
            return found

        curr += 1

    return found


def sorted_seq_search(lst, ele):
    lst_sort = sorted(lst)

    for curr in xrange(len(lst_sort)):
        if lst_sort[curr] == ele:
            return True
        elif lst_sort[curr] > ele:
            return False

    return False


def binary_search(lst, ele):
    lst_sorted = sorted(lst)
    print(lst_sorted)

    mid = len(lst_sorted) / 2

    print('Middle element: ' + str(lst_sorted[mid]))

    if lst_sorted[mid] == ele:
        return True
    elif len(lst_sorted) == 1:
        return False
    elif lst_sorted[mid] > ele:
        return binary_search(lst_sorted[:mid], ele)
    elif lst_sorted[mid] < ele:
        return binary_search(lst_sorted[mid:], ele)


if __name__ == '__main__':
    lst = [23, 45, 56, 12, 78, 87, 95]

    print(sequential_search(lst, 78))

    print(sorted_seq_search(lst, 23))

    print(binary_search(lst, 49))