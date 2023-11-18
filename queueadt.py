class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty queue")

def print_menu():
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Size")
    print("5. Check if empty")
    print("6. Exit")

if __name__ == "__main__":
    queue = Queue()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
            print("Enqueued", item)
        elif choice == "2":
            try:
                item = queue.dequeue()
                print("Dequeued", item)
            except IndexError as e:
                print(e)
        elif choice == "3":
            try:
                item = queue.peek()
                print("Front element:", item)
            except IndexError as e:
                print(e)
        elif choice == "4":
            print("Queue size:", queue.size())
        elif choice == "5":
            if queue.is_empty():
                print("Queue is empty")
            else:
                print("Queue is not empty")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
