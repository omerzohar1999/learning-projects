from linked_list import MyListNode

class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __init__(self, value):
        self.head = MyListNode(value)
        self.size = 1

    def __sizeof__(self) -> int:
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
