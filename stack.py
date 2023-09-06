class Stack:
    def __init__(self, stack):
        self.stack = stack

    def __str__(self):
        return f"{self.stack}"

    def is_empty(self):
        return False if len(self.stack) > 0 else True

    def push(self, new_el):
        new_el = new_el
        self.stack.append(new_el)

    def pop(self):
        stack_top = self.stack[-1]
        del self.stack[-1]
        return stack_top

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)