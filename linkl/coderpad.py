# from nose.tools import assert_equal

class SingleLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


def cyclic_check(node):
    visited = []

    while node.next is not None:
        if node.value in visited:
            return True
        else:
            print(node.value)

        visited.append(node.value)
        node = node.next

    return False


def reverse_singleLinkList(first_node):
    print('Reversing the linked list .... ')
    nodes = []
    print(first_node.value)
    nodes.append(first_node)
    node = first_node

    print('collecting nodes ...')
    while node.next is not None:
        node = node.next
        print(node.value)
        nodes.append(node)

    print('Reversing')
    curr = len(nodes)
    print(curr)
    while curr != 0:
        print('Inside while loop ...')
        print(curr)
        node = nodes[curr - 1]
        print(node.value)

        if curr > 1:
            print('Inside if .....')
            next_node = nodes[curr - 2]
            print(next_node.value)

        node.next = next_node
        curr -= 1

    return node


def jose_reverse_ll(head):
    current_node = head
    next_node = None
    previous_node = None

    while current:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current
        current_node = next_node

    return previous_node


def nth_node_from_last(nth, tail_node):
    current_node = tail_node

    for _ in xrange(nth):
        print(current_node.value)
        next_node = current_node.next
        current_node = next_node

    return current_node.value


def say_hello():
    print 'Hello, World'


if __name__ == '__main__':
    # for i in xrange(5):
    #     say_hello()

    sl1 = SingleLinkedList(10)
    sl2 = SingleLinkedList(20)
    sl3 = SingleLinkedList(30)
    sl4 = SingleLinkedList(40)

    sl1.next = sl2
    sl2.next = sl3
    sl3.next = sl4

    print(cyclic_check(sl4))

#     node = reverse_singleLinkList(sl1)

#     print(node.value)
    # print(node.next.value)
    # print(node.next.value)

    print('Nth node from last')
    print(nth_node_from_last(2, sl4))


