#referencing gave me some problems, so i just copied this class.
class MyListNode:
    def __init__(self, value):
        self.set_value(value)
        self.next = None

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __init__(self, value):
        self.head = MyListNode(value)
        self.size = 1

    def __len__(self) -> int:
        return self.size

    def pop(self):
        assert len(self) > 0
        to_return = self.head.get_value()
        self.head = self.head.get_next()
        self.size -= 1
        return to_return

    def push(self, value):
        to_add = MyListNode(value)
        to_add.set_next(self.head)
        self.head = to_add
        self.size += 1


def test():
    new_stack = MyStack(3)
    new_stack.push(5)
    print(new_stack.pop())
    print(new_stack.pop())
    

# test()
