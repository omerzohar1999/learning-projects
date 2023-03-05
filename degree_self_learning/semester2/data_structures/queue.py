class MyDoubleListNode:
    def __init__(self, value):
        self.set_value(value)
        self.next = None
        self.last = None

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def set_last(self, last):
        self.last = last

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next
    
    def get_last(self):
        return self.last


class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __init__(self, value):
        self.head = MyDoubleListNode(value)
        self.tail = self.head
        self.size = 1

    def Enqueue(self, value):
        new_head = MyDoubleListNode(value)
        new_head.set_next(self.head)
        if len(self) == 0:
            self.tail = new_head
        else:
            new_head.get_next().set_last(new_head)
        self.head = new_head
        self.size += 1

    def Dequeue(self):
        assert len(self) > 0
        to_return = self.tail.get_value()
        if len(self) == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.last
            self.tail.set_next(None)
        self.size -= 1
        return to_return

    def __len__(self) -> int:
        return self.size
