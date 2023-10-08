class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # self.items.append(item)
        self.stack += [item]  # self.stack = self.stack + [item]

    def pop(self):
        if not self.is_empty():
            # return self.items.pop()

            item = self.stack[-1]  # -1 accesses the end of the list
            self.stack = self.stack[
                :-1
            ]  # this is called slicing, it excludes the last element of the list

            # item = self.stack[len(self.stack) - 1]
            # self.stack = self.stack[:len(self.stack) - 1]
            return item
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0
