class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_next(self, value):
        self.insert_next_in(self.root, value)

    def insert_next_in(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self.insert_next_in(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self.insert_next_in(current_node.right, value)

    def delete(self, value):
        """
        Delete a node with the given value from the binary tree.
        """

        def _delete_recursive(node, value):
            if node is None:
                return node
            if value < node.value:
                node.left = _delete_recursive(node.left, value)
            elif value > node.value:
                node.right = _delete_recursive(node.right, value)
            else:
                # Node with only one child or no child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                # Node with two children: Get the inorder successor (smallest in the right subtree)
                temp = node.right
                while temp.left is not None:
                    temp = temp.left
                node.value = temp.value
                node.right = _delete_recursive(node.right, temp.value)
            return node

        self.root = _delete_recursive(self.root, value)

    def preorder_traversal(self, node, visit):
        if node:
            visit(node)
            self.preorder_traversal(node.left, visit)
            self.preorder_traversal(node.right, visit)

    def inorder_traversal(self, node, visit):
        if node:
            self.inorder_traversal(node.left, visit)
            visit(node)
            self.inorder_traversal(node.right, visit)

    def postorder_traversal(self, node, visit):
        if node:
            self.postorder_traversal(node.left, visit)
            self.postorder_traversal(node.right, visit)
            visit(node)

    def find(self, value):
        """
        Find a node with the given value in the binary tree
        """
        return self._find_binary_search(self.root, value)

    def _find_binary_search(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        elif value < node.value:
            return self._find_binary_search(node.left, value)
        else:
            return self._find_binary_search(node.right, value)

    def find_min_val(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def visualize(self, node=None, prefix="", is_tail=True):
        """
        Visualize the binary tree structure using ASCII characters
        """
        if node is None:
            node = self.root

        if node is not None:
            print(prefix + ("└── " if is_tail else "├── ") + str(node.value))

            children = []
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)

            for i, child in enumerate(children):
                is_last = i == len(children) - 1
                extension = "    " if is_tail else "│   "
                if child == node.left:
                    self.visualize(
                        child, prefix + extension, is_last and node.right is None
                    )
                else:
                    self.visualize(child, prefix + extension, is_last)


# Example usage:
tree = BinaryTree(13)

# Inserting nodes for binary search tree
tree.insert_next(7)
tree.insert_next(15)
tree.insert_next(3)
tree.insert_next(9)
tree.insert_next(10)
tree.insert_next(7)
tree.insert_next(8)
tree.insert_next(14)
tree.insert_next(19)
tree.insert_next(18)


def print_node(node):
    print(node.value)


print("ASCII Tree Visualization:")
tree.visualize()

tree.delete(7)

print("\nASCII Tree Visualization after deleting 7:")
tree.visualize()

# print("\nInorder Traversal:")
# tree.inorder_traversal(tree.root, print_node)

""" print("\nOutput of Find Method 18:")
found_node = tree.find(18)
if found_node:
    print(f"Node with value {found_node.value} found.")
else:
    print("Node not found.")

print("\nOutput of Find Method 20:")
found_node = tree.find(20)
if found_node:
    print(f"Node with value {found_node.value} found.")
else:
    print("Node not found.")

print("\nMinimum Value in the Tree:")
min_value = tree.find_min_val()
print(f"The minimum value in the tree is: {min_value}") """
