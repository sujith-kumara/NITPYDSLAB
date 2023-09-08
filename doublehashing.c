#include <stdio.h>
#include <stdlib.h>

int hash1(int key, int table_size) {
    return key % table_size;
}

int hash2(int key, int table_size) {
    return 8 - (key % 8);
}

int doubleHash(int key, int i, int table_size) {
    return (hash1(key, 11) + i * hash2(key, 8)) % table_size;
}

void insert(int table[], int key, int table_size) {
    int index = hash1(key, 11);

    if (table[index] == -1) {
        table[index] = key;
    } else {
        int i = 1;
        do {
            index = doubleHash(key, i, table_size);

            if (table[index] == -1) {
                table[index] = key;
                return;
            }

            i++;
        } while (i < table_size);
        printf("Error: Hash table is full.\n");
    }
}

int search(int table[], int key, int table_size) {
    int index = hash1(key, 11);

    if (table[index] == key) {
        return index;
    } else if (table[index] == -1) {
        return -1; // Key not found
    } else {
        int i = 1;
        do {
            index = doubleHash(key, i, table_size);

            if (table[index] == key) {
                return index;
            }

            if (table[index] == -1) {
                return -1; // Key not found
            }

            i++;
        } while (i < table_size);
        return -1; // Key not found
    }
}

void display(int table[], int table_size) {
    for (int i = 0; i < table_size; i++) {
        printf("Index %d: %d\n", i, table[i]);
    }
}

int main() {
    int size;

    printf("Enter the size of the element array: ");
    scanf("%d", &size);

    int elements[size];

    printf("Enter %d elements:\n", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &elements[i]);
    }

    int *hashTable = malloc(11 * sizeof(int));

    // Initialize hash table with -1 (indicating empty slots)
    for (int i = 0; i < 11; i++) {
        hashTable[i] = -1;
    }

    for (int i = 0; i < size; i++) {
        insert(hashTable, elements[i], 11);
    }

    display(hashTable, 11);

    int keyToSearch;
    printf("Enter a value to search for: ");
    scanf("%d", &keyToSearch);

    int result = search(hashTable, keyToSearch, 11);

    if (result != -1) {
        printf("\nValue %d found at index %d\n", keyToSearch, result);
    } else {
        printf("\nValue %d not found\n", keyToSearch);
    }

    free(hashTable); // Free the dynamically allocated memory

    return 0;
}
