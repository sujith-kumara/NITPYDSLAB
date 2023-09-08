#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

int hash(int key, int table_size) {
    return key % table_size;
}

void insert(Node* table[], int key, int table_size) {
    int index = hash(key, table_size);
    Node* newNode = createNode(key);

    if (table[index] == NULL) {
        table[index] = newNode;
    } else {
        Node* current = table[index];
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}

int search(Node* table[], int key, int table_size) {
    int index = hash(key, table_size);
    Node* current = table[index];

    while (current != NULL) {
        if (current->data == key) {
            return index; // Key found at index
        }
        current = current->next;
    }

    return -1; // Key not found
}

void display(Node* table[], int table_size) {
    for (int i = 0; i < table_size; i++) {
        printf("Index %d:", i);
        Node* current = table[i];
        while (current != NULL) {
            printf(" %d", current->data);
            current = current->next;
        }
        printf("\n");
    }
}

int main() {
    Node* hashTable[TABLE_SIZE] = {NULL};
    int size;

    printf("Enter the size of the element array: ");
    scanf("%d", &size);

    int elements[size];

    printf("Enter %d elements:\n", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &elements[i]);
    }

    for (int i = 0; i < size; i++) {
        insert(hashTable, elements[i], TABLE_SIZE);
    }

    display(hashTable, TABLE_SIZE);

    int searchValue;
    printf("Enter a value to search for: ");
    scanf("%d", &searchValue);

    int result = search(hashTable, searchValue, TABLE_SIZE);

    if (result != -1) {
        printf("\nValue %d found at index %d\n", searchValue, result);
    } else {
        printf("\nValue %d not found\n", searchValue);
    }

    return 0;
}
