class Node:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf

    def is_full(self, order):
        return len(self.keys) == (2 * order) - 1

class BTree:
    def __init__(self, order):
        self.root = Node()
        self.order = order

    def insert(self, key):
        root = self.root
        if root.is_full(self.order):
            new_root = Node(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, key)
            self.root = new_root
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if node.children[i].is_full(self.order):
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, index):
        order = self.order
        child = parent.children[index]
        new_child = Node(leaf=child.leaf)

        parent.keys.insert(index, child.keys[order - 1])
        parent.children.insert(index + 1, new_child)

        new_child.keys = child.keys[order:(2 * order) - 1]
        child.keys = child.keys[0:order - 1]

        if not child.leaf:
            new_child.children = child.children[order:2 * order]
            child.children = child.children[0:order - 1]

    def inorder_traversal(self, node):
        if node:
            i = 0
            while i < len(node.keys):
                if not node.leaf:
                    self.inorder_traversal(node.children[i])
                print(node.keys[i], end=' ')
                i += 1
            if not node.leaf:
                self.inorder_traversal(node.children[i])

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True

        if node.leaf:
            return False

        return self._search(node.children[i], key)

if __name__ == "__main__":
    order = 3
    b_tree = BTree(order)
    
    elements = [10, 20, 5, 6, 12, 30, 7, 17]

    for element in elements:
        b_tree.insert(element)

    print("In-order traversal of B-tree:")
    b_tree.inorder_traversal(b_tree.root)

    print("\nSearching for key 12:", b_tree.search(12))
    print("Searching for key 25:", b_tree.search(25))
