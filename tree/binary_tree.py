
class BinaryTree:

    def __init__(self, node_value):
        self.key = node_value
        self.right_node = None
        self.left_node = None

    def add_left_node(self, node_value):

        if self.left_node is None:
            tmp = BinaryTree(node_value)
            self.left_node = tmp
        else:
            tmp = BinaryTree(node_value)
            tmp.left_node = self.left_node
            self.left_node = tmp

    def add_right_node(self, node_value):

        if self.right_node is None:
            tmp = BinaryTree(node_value)
            self.right_node = tmp
        else:
            tmp = BinaryTree(node_value)
            tmp.right_node = self.right_node
            self.right_node = tmp

    def get_right_node(self):
        return self.right_node

    def get_left_node(self):
        return self.left_node

    def set_node_key(self, key):
        self.key = key

    def get_node_key(self):
        return self.key


def inorder_traverse(tree):
    if tree is not None:
        print(tree.get_node_key())
        inorder_traverse(tree.get_left_node())
        # print(tree.get_node_key())
        inorder_traverse(tree.get_right_node())
        # print(tree.get_node_key())

if __name__ == '__main__':

    a = BinaryTree(10)
    a.add_left_node(20)
    a.add_right_node(30)
    a.add_left_node(15)

    a.get_left_node().add_right_node(25)
    a.get_right_node().add_right_node(45)
    a.get_right_node().add_left_node(35)

    # print(a.get_node_key())
    # print(a.left_node.get_node_key())
    # print(a.left_node.left_node.get_node_key())
    # print(a.right_node.get_node_key())

    inorder_traverse(a)

