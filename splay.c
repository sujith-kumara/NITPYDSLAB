#include <stdio.h>
#include <stdlib.h>

struct Node {
    int key;
    struct Node* left;
    struct Node* right;
};

typedef struct Node Node;

// Function prototypes
Node* createNode(int key);
Node* splay(Node* root, int key);
Node* insert(Node* root, int key);
Node* delete(Node* root, int key);
Node* search(Node* root, int key);
Node* leftRotate(Node* x);
Node* rightRotate(Node* y);
void inOrderTraversal(Node* root);

Node* createNode(int key) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Error: Memory allocation failed\n");
        exit(1);
    }
    newNode->key = key;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

Node* splay(Node* root, int key) {
    if (root == NULL || root->key == key) {
        return root;
    }

    if (key < root->key) {
        if (root->left == NULL) {
            return root;
        }
        if (key < root->left->key) {
            root->left->left = splay(root->left->left, key);
            root = rightRotate(root);
        } else if (key > root->left->key) {
            root->left->right = splay(root->left->right, key);
            if (root->left->right != NULL) {
                root->left = leftRotate(root->left);
            }
        }
        return (root->left == NULL) ? root : rightRotate(root);
    } else {
        if (root->right == NULL) {
            return root;
        }
        if (key < root->right->key) {
            root->right->left = splay(root->right->left, key);
            if (root->right->left != NULL) {
                root->right = rightRotate(root->right);
            }
        } else if (key > root->right->key) {
            root->right->right = splay(root->right->right, key);
            root = leftRotate(root);
        }
        return (root->right == NULL) ? root : leftRotate(root);
    }
}

Node* insert(Node* root, int key) {
    if (root == NULL) {
        return createNode(key);
    }

    root = splay(root, key);

    if (key < root->key) {
        Node* newNode = createNode(key);
        newNode->right = root;
        newNode->left = root->left;
        root->left = NULL;
        return newNode;
    } else if (key > root->key) {
        Node* newNode = createNode(key);
        newNode->left = root;
        newNode->right = root->right;
        root->right = NULL;
        return newNode;
    } else {
        return root;
    }
}

Node* delete(Node* root, int key) {
    if (root == NULL) {
        return root;
    }

    root = splay(root, key);

    if (root->key != key) {
        return root;
    }

    Node* temp;
    if (root->left == NULL) {
        temp = root;
        root = root->right;
    } else {
        temp = root;
        root = splay(root->left, key);
        root->right = temp->right;
    }

    free(temp);
    return root;
}

Node* leftRotate(Node* x) {
    Node* y = x->right;
    x->right = y->left;
    y->left = x;
    return y;
}

Node* rightRotate(Node* y) {
    Node* x = y->left;
    y->left = x->right;
    x->right = y;
    return x;
}

Node* search(Node* root, int key) {
    if (root == NULL || root->key == key) {
        return splay(root, key);
    }

    if (key < root->key) {
        if (root->left == NULL) {
            // Key not found, splay the last accessed node
            return splay(root, key);
        }
        if (key < root->left->key) {
            root->left->left = search(root->left->left, key);
            root = rightRotate(root);
        } else if (key > root->left->key) {
            root->left->right = search(root->left->right, key);
            if (root->left->right != NULL) {
                root->left = leftRotate(root->left);
            }
        }
        return (root->left == NULL) ? root : rightRotate(root);
    } else {
        if (root->right == NULL) {
            // Key not found, splay the last accessed node
            return splay(root, key);
        }
        if (key < root->right->key) {
            root->right->left = search(root->right->left, key);
            if (root->right->left != NULL) {
                root->right = rightRotate(root->right);
            }
        } else if (key > root->right->key) {
            root->right->right = search(root->right->right, key);
            root = leftRotate(root);
        }
        return (root->right == NULL) ? root : leftRotate(root);
    }
}

void inOrderTraversal(Node* root) {
    if (root != NULL) {
        inOrderTraversal(root->left);
        printf("%d ", root->key);
        inOrderTraversal(root->right);
    }
}

int main() {
    Node* root = NULL;
    int choice, key;

    while (1) {
        printf("\nSplay Tree Menu:\n");
        printf("1. Insert a key\n2. Delete a key\n3. Print in-order traversal\n4. Search for a key\n5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the key to insert: ");
                scanf("%d", &key);
                root = insert(root, key);
                printf("Splay Tree after insertion: ");
                inOrderTraversal(root);
                printf("\n");
                break;
            case 2:
                printf("Enter the key to delete: ");
                scanf("%d", &key);
                root = delete(root, key);
                printf("Splay Tree after deletion: ");
                inOrderTraversal(root);
                printf("\n");
                break;
            case 3:
                printf("In-order traversal of splay tree: ");
                inOrderTraversal(root);
                printf("\n");
                break;
            case 4:
                printf("Enter the key to search: ");
                scanf("%d", &key);
                root = search(root, key);
                printf("Splay Tree after search: ");
                inOrderTraversal(root);
                printf("\n");
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
