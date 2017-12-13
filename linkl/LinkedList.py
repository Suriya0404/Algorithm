class SingleLinkedList:
    def __init__(self, val):
        self.value = val
        self.next = None


class DoubleLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None



if __name__ == '__main__':
    # Single Linked List
    a = SingleLinkedList(10)
    b = SingleLinkedList(20)
    c = SingleLinkedList(30)
    a.next = b
    b.next = c

    # Double Linked List
    x = DoubleLinkedList(100)
    y = DoubleLinkedList(200)
    z = DoubleLinkedList(300)

    x.next = y
    y.previous = x
    y.next = z
    z.previous = y





