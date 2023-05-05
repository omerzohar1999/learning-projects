class MyListNode:
    def __init__(self, value):
        self.value = None
        self.set_value(value)
        self.next = None
        self.prev = None

    def set_value(self, value):
        self.value = value

    def set_next(self, next_node):
        self.next = next_node

    def set_prev(self, prev):
        self.prev = prev

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev


class MyLinkedList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.size = 0
        for val in args:
            self.insert_last(val)

    def insert_first(self, value):
        new_head = MyListNode(value)
        new_head.set_next(self.head)
        self.head = new_head
        if self.size == 0:
            self.tail = new_head
        else:
            self.head.get_next().set_prev(new_head)
        self.size += 1

    def __len__(self) -> int:
        return self.size

    def insert_last(self, value):
        pointer = self.head
        if pointer is None:
            self.insert_first(value)
        else:
            new_tail = MyListNode(value)
            self.tail.set_next(new_tail)
            new_tail.set_prev(self.tail)
            self.tail = new_tail
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
        if self.size > 1:
            self.head.set_prev(None)
        self.size -= 1
        return to_return

    def pop_at(self, position):
        assert position < self.size
        if position == 0:
            return self.pop_first()
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
            self.size -= 1
        if pointer is not None:
            while pointer.get_next() is not None:
                if pointer.get_next().get_value() == value:
                    pointer.set_next(pointer.get_next().get_next())
                    self.size -= 1
                else:
                    pointer = pointer.get_next()

    def concat(self, to_add_at_end):
        if not to_add_at_end.size:
            return
        self.size += to_add_at_end.size
        self.tail.set_next(to_add_at_end.head)
        to_add_at_end.head.set_prev(self.tail)
        self.tail = to_add_at_end.tail
    
    def is_empty(self):
        return self.size == 0

    def __sizeof__(self):
        return self.size

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if not self.iterator:
            raise StopIteration
        ret = self.iterator.value
        self.iterator = self.iterator.next
        return ret

    def __getitem(self, key):
        return self.retrieve_at(key)

    def __contains__(self, item):
        ptr = self.head
        while ptr and ptr.value != item:
            ptr = ptr.next
        if ptr:
            return True
        else:
            return False

    def __str__(self):
        ret = ""
        pointer = self.head
        while pointer is not None:
            ret += str(pointer.get_value())
            if pointer.get_next() is not None:
                ret += ", "
            pointer = pointer.get_next()
        return ret


def test():
    new_list = MyLinkedList(5)
    new_list.pop_first()
    print(len(new_list))


test()
