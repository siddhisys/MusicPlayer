class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"↩️ Added to Stack: {item}")

    def pop(self):
        if not self.stack:
            print("⚠ Stack empty")
            return None
        item = self.stack.pop()
        print(f"↪️ Removed from Stack: {item}")
        return item

    def display(self):
        if not self.stack:
            print("Stack: []")
        else:
            print("Stack (latest first):", list(reversed(self.stack)))

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"➡️ Added to Queue: {item}")

    def dequeue(self):
        if not self.queue:
            print("⚠ Queue empty")
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)

class PriorityQueue:
    def __init__(self):
        self.queue = []  # list of (priority, item)

    def enqueue(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(reverse=True)
        print(f"⭐ Added with priority {priority}: {item}")

    def dequeue(self):
        if not self.queue:
            print("⚠ Priority Queue empty")
            return None
        priority, item = self.queue.pop(0)
        return item

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Priority Queue:", self.queue)
