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

    if table[index] is None:
        table[index] = create_node(key)
    else:
        # Linear probing - find the next available slot
        next_index = (index + 1) % table_size
        while next_index != index and table[next_index] is not None:
            next_index = (next_index + 1) % table_size

        if next_index == index:
            print("Hash table is full. Cannot insert.")
            return

        table[next_index] = create_node(key)

def search(table, key, table_size):
    index = hash_func(key, table_size)

    if table[index] is None:
        return -1  # Key not found at hashed index
    
    if table[index].data == key:
        return index  # Key found at hashed index
    
    # Linear probing to find the key
    next_index = (index + 1) % table_size
    while next_index != index:
        if table[next_index] is None:
            return -1  # Key not found
        if table[next_index].data == key:
            return next_index  # Key found
        next_index = (next_index + 1) % table_size

    return -1  # Key not found

def display(table, table_size):
    for i in range(table_size):
        print(f"Index {i}:", end="")
        if table[i] is not None:
            print(f" {table[i].data}", end="")
        print()

if __name__ == "__main__":
    TABLE_SIZE = 10
    hash_table = [None] * TABLE_SIZE

    size = int(input("Enter the size of the element array: "))
    elements = []

    print(f"Enter {size} elements:")
    for _ in range(size):
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
