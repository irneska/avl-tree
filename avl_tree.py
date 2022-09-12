class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class AvlTree:
    def insert(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) >= 0:
                node = self.right_rotate(node)
            else:
                node = self.left_right_rotate(node)
        elif balance < -1:
            if self.get_balance(node.right) <= 0:
                node = self.left_rotate(node)
            else:
                node = self.right_left_rotate(node)

        return node

    @staticmethod
    def get_height(node):
        if not node:
            return -1

        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left.height = 1 + max(self.get_height(left.left), self.get_height(left.right))

        return left

    def left_rotate(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right.height = 1 + max(self.get_height(right.left), self.get_height(right.right))

        return right

    def left_right_rotate(self, node):
        node.left = self.left_rotate(node.left)

        return self.right_rotate(node)

    def right_left_rotate(self, node):
        node.right = self.right_rotate(node.right)

        return self.left_rotate(node)

    def preorder(self, root):
        if root:
            print(root.value),
            self.preorder(root.left)
            self.preorder(root.right)
