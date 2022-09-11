from linked_list import MyLinkedList

class MyHashTable:
    def __init__(self, size: int, func: function):
        self.arr = []
        for i in range(size):
            self.arr.append(None)
        self.func = func

    def insert(self, key: int, value: int):
        this_hash = self.func(key)
        if self.arr[this_hash] is None:
            self.arr[this_hash] = MyLinkedList((key, value))
        
    def find(self, key):
        this_hash = self.func(key)
        if self.arr[this_hash] is not None:
            current_chain = self.arr[this_hash]
            for i in range(len(current_chain)):  # add iterator to linked list for improved complexity
                current_node = current_chain.retreive_at(i)
                if current_node[0] == key:
                    return current_node[1]
        return None
    
    def delete(self, key):
        value = self.find(key)
        to_delete = (key, value)
        this_hash = self.func(key)
        self.arr[this_hash].delete(to_delete)