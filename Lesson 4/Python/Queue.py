class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def front(self):
        return self.peek()

    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0
