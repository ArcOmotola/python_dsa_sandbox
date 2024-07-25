class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if value == self.value:
            return self
        elif value < self.value and self.left:
            return self.left.find(value)
        elif value > self.value and self.right:
            return self.right.find(value)
        return None

    def in_order_traversal(self, result):
        if self.left:
            self.left.in_order_traversal(result)
        result.append(self.value)
        if self.right:
            self.right.in_order_traversal(result)

    def pre_order_traversal(self, result):
        result.append(self.value)
        if self.left:
            self.left.pre_order_traversal(result)
        if self.right:
            self.right.pre_order_traversal(result)

    def post_order_traversal(self, result):
        if self.left:
            self.left.post_order_traversal(result)
        if self.right:
            self.right.post_order_traversal(result)
        result.append(self.value)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)
        else:
            self.root.insert(value)

    def find(self, value):
        if self.root:
            return self.root.find(value)
        return None

    def in_order_traversal(self):
        result = []
        if self.root:
            self.root.in_order_traversal(result)
        return result

    def pre_order_traversal(self):
        result = []
        if self.root:
            self.root.pre_order_traversal(result)
        return result

    def post_order_traversal(self):
        result = []
        if self.root:
            self.root.post_order_traversal(result)
        return result


# Example Usage
if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree()

    # Insert values
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)

    # Find a value
    node = tree.find(7)
    if node:
        print(f'Node with value {node.value} found')
    else:
        print('Node not found')

    # Perform traversals
    print('In-order traversal:', tree.in_order_traversal())
    print('Pre-order traversal:', tree.pre_order_traversal())
    print('Post-order traversal:', tree.post_order_traversal())
