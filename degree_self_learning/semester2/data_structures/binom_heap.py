class MyBinomialHeapNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class MyBinomialHeap:
    def __init__(self):
        self.head = None

    def __init__(self, value):
        self.head = MyBinomialHeapNode(value)

    def insert(self, value):
        pass  # TODO

    def pop_min(self):
        return 0  # TODO