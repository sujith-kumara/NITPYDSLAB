class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def leftRotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

def rightRotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x

def splay(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        if root.left is None:
            return root
        if key < root.left.key:
            root.left.left = splay(root.left.left, key)
            root = rightRotate(root)
        elif key > root.left.key:
            root.left.right = splay(root.left.right, key)
            if root.left.right is not None:
                root.left = leftRotate(root.left)
        if root.left is not None:
            return rightRotate(root)
        else:
            return root
    else:
        if root.right is None:
            return root
        if key < root.right.key:
            root.right.left = splay(root.right.left, key)
            if root.right.left is not None:
                root.right = rightRotate(root.right)
        elif key > root.right.key:
            root.right.right = splay(root.right.right, key)
            root = leftRotate(root)
        if root.right is not None:
            return leftRotate(root)
        else:
            return root

def insert(root, key):
    if root is None:
        return Node(key)

    root = splay(root, key)

    if key < root.key:
        new_node = Node(key)
        new_node.right = root
        new_node.left = root.left
        root.left = None
        return new_node
    elif key > root.key:
        new_node = Node(key)
        new_node.left = root
        new_node.right = root.right
        root.right = None
        return new_node
    else:
        return root

def delete(root, key):
    if root is None:
        return root

    root = splay(root, key)

    if root.key != key:
        return root

    if root.left is None:
        temp = root
        root = root.right
    else:
        temp = root
        root = splay(root.left, key)
        root.right = temp.right

    del temp
    return root

def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)
        print(root.key, end=' ')
        inOrderTraversal(root.right)

if __name__ == "__main__":
    root = None
    root = insert(root, 100)
    root = insert(root, 50)
    root = insert(root, 200)
    root = insert(root, 40)
    root = insert(root, 60)

    print("In-order traversal before deletion:")
    inOrderTraversal(root)
    print()

    root = delete(root, 50)
    print("In-order traversal after deleting key 50:")
    inOrderTraversal(root)
    print()
