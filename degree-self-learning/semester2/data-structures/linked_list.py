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


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __init__(self, value):
        self.head = MyListNode(value)
        self.size = 1

    def insert_first(self, value):
        new_head = MyListNode(value)
        new_head.set_next(self.head)
        self.head = new_head
        self.size += 1

    def __sizeof__(self) -> int:
        return self.size

    def insert_last(self, value):
        pointer = self.head
        if pointer is None:
            self.insert_first(value)
        else:
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = MyListNode(value)
            self.size += 1

    def insert_at(self, value, pos):
        assert pos <= self.size
        new_node = MyListNode(value)
        i = 0
        pointer = self.head
        while i < pos:
            pointer = pointer.next
            i += 1
        new_node.set_next(pointer.next)
        pointer.set_next(new_node)
        self.size += 1

    def retrieve_at(self, position):
        assert position < len(self)
        i = 0
        pointer = self.head
        while i < position:
            pointer = pointer.next
            i += 1
        return pointer.get_value()

    def pop_first(self):
        if len(self) == 0:
            return None
        to_return = self.head.get_value()
        self.head = self.head.get_next()
        self.size -= 1
        return to_return

    def pop_at(self, position):
        assert position < self.size
        if position == 0:
            return self.delete_first()
        else:
            i = 0
            pointer = self.head
            while i < position - 1:
                pointer = pointer.get_next()
                i += 1
            to_return = pointer.get_next().get_value()
            pointer.set_next(pointer.get_next().get_next())
            self.size -= 1
            return to_return

    def delete(self, value):
        pointer = self.head
        while pointer.get_value() == value:
            pointer = pointer.get_next()
            self.head = pointer
        if pointer is not None:
            while pointer.get_next() is not None:
                if pointer.get_next().get_value() == value:
                    pointer.set_next(pointer.get_next().get_next())
                else:
                    pointer = pointer.get_next()
