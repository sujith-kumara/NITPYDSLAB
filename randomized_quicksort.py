import random

def random_partition(arr, f, l):
    random_index = random.randint(f, l)
    arr[f], arr[random_index] = arr[random_index], arr[f]

    key = arr[f]
    i, j = f + 1, l

    while True:
        while i <= j and arr[i] < key:
            i += 1
        while j >= f and arr[j] > key:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[j], arr[f] = arr[f], arr[j]
    return j

def random_qsort(arr, l, r):
    if l < r:
        m = random_partition(arr, l, r)
        random_qsort(arr, l, m - 1)
        random_qsort(arr, m + 1, r)

if __name__ == "__main__":
    n = int(input("Enter N: "))
    a = []

    print("Enter the elements to be sorted:")
    for i in range(n):
        a.append(int(input()))

    random_qsort(a, 0, n - 1)

    print("Sorted array:")
    for i in range(n):
        print(a[i], end=" ")
