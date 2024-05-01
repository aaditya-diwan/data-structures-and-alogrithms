class Stack(object):
    def __init__(self):
        self.items = list()

    def push(self, num):
        self.items.append(num)

    def pop(self):
        self.items.pop()

    def display(self):
        print(f"Following is the Stack : {self.items}")


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    stack.pop()
    stack.display()