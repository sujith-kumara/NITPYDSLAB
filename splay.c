#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    struct Node *left;
    struct Node *right;
} Node;

Node* newNode(int key) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->key = key;
    node->left = node->right = NULL;
    return node;
}

Node* rightRotate(Node* x) {
    Node* y = x->left;
    x->left = y->right;
    y->right = x;
    return y;
}

Node* leftRotate(Node* x) {
    Node* y = x->right;
    x->right = y->left;
    y->left = x;
    return y;
}

Node* splay(Node* root, int key) {
    if (root == NULL || root->key == key) return root;
    if (root->key > key) {
        if (root->left == NULL) return root;
        if (root->left->key > key) {
            root->left->left = splay(root->left->left, key);
            root = rightRotate(root);
        } else if (root->left->key < key) {
            root->left->right = splay(root->left->right, key);
            if (root->left->right != NULL) root->left = leftRotate(root->left);
        }
        return (root->left == NULL) ? root : rightRotate(root);
    } else {
        if (root->right == NULL) return root;
        if (root->right->key > key) {
            root->right->left = splay(root->right->left, key);
            if (root->right->left != NULL) root->right = rightRotate(root->right);
        } else if (root->right->key < key) {
            root->right->right = splay(root->right->right, key);
            root = leftRotate(root);
        }
        return (root->right == NULL) ? root : leftRotate(root);
    }
}

Node* insert(Node* root, int key) {
    if (root == NULL) return newNode(key);
    root = splay(root, key);
    if (root->key == key) return root;
    Node* node = newNode(key);
    if (root->key > key) {
        node->right = root;
        node->left = root->left;
        root->left = NULL;
    } else {
        node->left = root;
        node->right = root->right;
        root->right = NULL;
    }
    return node;
}

Node* deleteNode(Node* root, int key) {
    if (root == NULL) return NULL;
    root = splay(root, key);
    if (root->key != key) return root;
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

Node* search(Node* root, int key) {
    return splay(root, key);
}

void inorder(Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->key);
        inorder(root->right);
    }
}

int main() {
    Node* root = NULL;
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 70);
    root = insert(root, 60);
    root = insert(root, 80);
    
    printf("Inorder traversal: ");
    inorder(root);
    printf("\n");
    
    root = deleteNode(root, 20);
    printf("Inorder traversal after deleting 20: ");
    inorder(root);
    printf("\n");
    
    Node* searchResult = search(root, 30);
    if (searchResult != NULL) {
        printf("Key 30 found in the tree.\n");
    } else {
        printf("Key 30 not found in the tree.\n");
    }
    
    return 0;
}

