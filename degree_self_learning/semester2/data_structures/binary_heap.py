class MyBinaryHeap:  # TODO
    def __init__(self):
        self.heap_arr = []

    def insert(self, value):
        self.heap_arr.append(value)
        self.heapify_up(len(self.heap_arr) - 1)

    def heapify_up(self, index):
        if not (index == 0 or self.heap_arr[index] > self.heap_arr[index // 2]):
            self.heap_arr[index], self.heap_arr[index // 2] = self.heap_arr[index // 2], self.heap_arr[index]
            self.heapify_up(index // 2)
    
    def heapify_down(self, index):
        right = index * 2 + 1
        left = index * 2
        if left < len(self.heap_arr):
            if right >= len(self.heap_arr):
                if self.heap_arr[index] < self.heap_arr[left]:
                    self.heap_arr[index], self.heap_arr[left] = self.heap_arr[left], self.heap_arr[index]
            else:
                if self.heap_arr[index] > self.heap_arr[right] or self.heap_arr[index] > self.heap_arr[left]:
                    new_index = right if self.heap_arr[right] < self.heap_arr[left] else left
                    self.heap_arr[index], self.heap_arr[new_index] = self.heap_arr[new_index], self.heap_arr[index]
                    self.heapify_down(new_index)
                
    
    def delete(self, index):
        self.heap_arr[len(self.heap_arr) - 1], self.heap_arr[index] = self.heap_arr[index], self.heap_arr[len(self.heap_arr) - 1]
        self.heap_arr.pop()
        self.heapify_down(index)

    def pop_min(self):
        to_return = self.heap_arr[0]
        self.delete(0)
        return to_return



def test():
    my_heap = MyBinaryHeap()
    my_heap.insert(9)
    my_heap.insert(3)
    my_heap.insert(4)
    my_heap.insert(6)
    my_heap.insert(2)

    print(my_heap.pop_min())
    print(my_heap.pop_min())
    print(my_heap.pop_min())
    print(my_heap.pop_min())
    print(my_heap.pop_min())

test()
