#include <stdio.h>
#include <stdlib.h> // For rand() and srand()
#include <time.h>   // For seeding the random number generator

void swap(int *p, int *q) {
    int t;
    t = *p;
    *p = *q;
    *q = t;
}

int randomPartition(int a[], int f, int l) {
    // Generate a random index between f and l
    int randomIndex = f + rand() % (l - f + 1);
    
    // Swap the randomly selected element with the first element
    swap(&a[f], &a[randomIndex]);

    int key = a[f], i = f + 1, j = l;

    do {
        while (i <= j && a[i] < key)
            i++;
        while (j >= f && a[j] > key)
            j--;
        if (i < j)
            swap(&a[i], &a[j]);
    } while (i <= j);

    swap(&a[j], &a[f]);
    return (j);
}

void randomQSort(int a[], int l, int r) {
    int m;
    if (l < r) {
        m = randomPartition(a, l, r);
        randomQSort(a, l, m - 1);
        randomQSort(a, m + 1, r);
    }
}

int main() {
    int n, i, a[100];

    printf("Enter N: ");
    scanf("%d", &n);

    srand(time(NULL)); // Seed the random number generator

    printf("Enter the elements to be sorted:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    randomQSort(a, 0, n - 1);

    printf("Sorted array:\n");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);

    return 0;
}
