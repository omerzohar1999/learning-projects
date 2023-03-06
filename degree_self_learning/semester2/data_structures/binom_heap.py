import math


class MyBinomialHeapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.son = None
        self.rank = 0


class MyBinomialHeap:
    def __init__(self):
        self.size = 0
        self.min_node = None
        self.head_node = None

    def insert(self, key, value):
        to_insert = MyBinomialHeapNode(key, value)
        if self.min_node is None or self.min_node.key > key:
            self.min_node = to_insert
        to_insert.right = self.head_node
        if self.head_node is not None:
            self.head_node.left = to_insert
        self.head_node = to_insert
        self.size += 1
        self.consolidate()
        return to_insert

    def get_min(self):
        return None, None if self.min_node is None else self.min_node.key, self.min_node.value

    def find_new_min(self):
        pointer = self.head_node
        if pointer is None:
            self.min_node = None
            return
        min_pointer = pointer
        while pointer.right is not None:
            pointer = pointer.right
            if pointer.key < min_pointer.key:
                min_pointer = pointer
        self.min_node = min_pointer

    def pop_min(self):
        min_node = self.min_node
        ret = min_node.key, min_node.value
        if min_node.right is not None:
            min_node.right.left = min_node.left
        if min_node.left is not None:
            min_node.left.right = min_node.right
            self.size -= 1
        first_son = self.min_node.son
        if first_son is not None:
            ptr = first_son
            while ptr is not None:
                ptr.parent = None
                next_ptr = ptr.right
                ptr.left = None
                ptr.right = self.head_node
                self.head_node = ptr
                ptr = next_ptr
            self.consolidate()
        self.find_new_min()
        return ret

    def consolidate(self):
        arr_size = int(math.log2(self.size)) + 1
        arr = [None for i in range(arr_size)]
        ptr = self.head_node
        while ptr is not None:
            curr_rank = ptr.rank
            while arr[curr_rank] is not None:
                to_link = arr[curr_rank]
                arr[curr_rank] = None
                if to_link.key < ptr.key:
                    ptr, to_link = to_link, ptr
                to_link.left = None
                to_link.right = ptr.son
                if ptr.son is not None:
                    ptr.son.left = to_link
                ptr.son = to_link
                to_link.parent = ptr
                ptr.rank += 1
                curr_rank = ptr.rank
            arr[curr_rank] = ptr
            ptr = ptr.right
        new_head = arr[len(arr)-1]
        ptr = new_head
        for i in range(len(arr)-2, -1, -1):
            if arr[i] is not None:
                ptr.right = arr[i]
                arr[i].left = ptr
        ptr.right = None
        self.head_node = new_head
        self.find_new_min()

    def decrease_key(self, node: MyBinomialHeapNode, new_key: int):
        node.key = new_key
        self.heapify_up(node)

    def heapify_up(self, node: MyBinomialHeapNode):
        if node.parent is not None and node.key < node.parent.key:
            node.key, node.parent.key = node.parent.key, node.key
            node.value, node.parent.value = node.parent.value, node.value
            self.heapify_up(node.parent)

    def delete(self, node: MyBinomialHeapNode):
        self.decrease_key(node, node.key - self.min_node.key + 1)
        self.pop_min()

    def is_empty(self):
        return self.size == 0
