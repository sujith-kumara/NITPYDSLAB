class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_node(data):
    return Node(data)

def hash_func(key, table_size):
    return key % table_size

def insert(table, key, table_size):
    index = hash_func(key, table_size)
    new_node = create_node(key)

    if table[index] is None:
        table[index] = new_node
    else:
        current = table[index]
        while current.next is not None:
            current = current.next
        current.next = new_node

def search(table, key, table_size):
    index = hash_func(key, table_size)
    current = table[index]

    while current is not None:
        if current.data == key:
            return index  # Key found at index
        current = current.next

    return -1  # Key not found

def display(table, table_size):
    for i in range(table_size):
        print(f"Index {i}:", end="")
        current = table[i]
        while current is not None:
            print(f" {current.data}", end="")
            current = current.next
        print()

if __name__ == "__main__":
    TABLE_SIZE = 10
    hash_table = [None] * TABLE_SIZE

    size = int(input("Enter the size of the element array: "))
    elements = []

    print(f"Enter {size} elements:")
    for i in range(size):
        elements.append(int(input()))

    for elem in elements:
        insert(hash_table, elem, TABLE_SIZE)

    display(hash_table, TABLE_SIZE)

    search_value = int(input("Enter a value to search for: "))
    result = search(hash_table, search_value, TABLE_SIZE)

    if result != -1:
        print(f"\nValue {search_value} found at index {result}\n")
    else:
        print(f"\nValue {search_value} not found\n")
