class MyBinaryHeap:  # TODO
    def __init__(self):
        self.heap_arr = []

    def insert(self, value, key):
        self.heap_arr.append((value, key))
        self.heapify_up(len(self.heap_arr) - 1)

    def heapify_up(self, index):
        if not (index == 0 or self.heap_arr[index][0] > self.heap_arr[index // 2][0]):
            self.heap_arr[index], self.heap_arr[index // 2] = self.heap_arr[index // 2], self.heap_arr[index]
            self.heapify_up(index // 2)
    
    def heapify_down(self, index):
        right = index * 2 + 1
        left = index * 2
        heap_arr = self.heap_arr
        if left < len(heap_arr):
            if right >= len(heap_arr):
                if heap_arr[index][0] < heap_arr[left][0]:
                    heap_arr[index], heap_arr[left] = heap_arr[left], heap_arr[index]
            else:
                if heap_arr[index][0] > heap_arr[right][0] or heap_arr[index][0] > heap_arr[left][0]:
                    new_index = right if heap_arr[right][0] < heap_arr[left][0] else left
                    heap_arr[index], heap_arr[new_index] = heap_arr[new_index], heap_arr[index]
                    self.heapify_down(new_index)

    def delete(self, index):
        n = len(self.heap_arr)
        self.heap_arr[n - 1], self.heap_arr[index] = self.heap_arr[index], self.heap_arr[n - 1]
        self.heap_arr.pop()
        self.heapify_down(index)

    def pop_min(self):
        to_return = self.heap_arr[0]
        self.delete(0)
        return to_return


def test():
    my_heap = MyBinaryHeap()
    my_heap.insert(9, 0)
    my_heap.insert(3, 0)
    my_heap.insert(4, 0)
    my_heap.insert(6, 0)
    my_heap.insert(2, 0)

    print(my_heap.pop_min())
    print(my_heap.pop_min())
    print(my_heap.pop_min())
    print(my_heap.pop_min())
    print(my_heap.pop_min())


test()
