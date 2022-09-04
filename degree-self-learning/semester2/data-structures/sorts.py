from random import Random
from avl_tree import MyAVLTree
from binom_heap import MyBinomialHeap


def bubble_sort(array: list):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


def selection_sort(array: list):
    for i in range(len(array)):
        min = array[i]
        min_pos = i
        for j in range(i, len(array)):
            if array[j] < min:
                min = array[j]
                min_pos = j
        array[i], array[min_pos] = array[min_pos], array[i]
    return array


def merge(left: list, right: list):
    res = []
    while len(left) and len(right):
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if len(left):
        res += left
    if len(right):
        res += right
    return res


def mergesort(array: list):
    if len(array) == 1:
        return array
    mid_pivot = len(array) // 2
    left = mergesort(array[:mid_pivot])
    right = mergesort(array[mid_pivot:])
    return merge(left, right)


def insertion_sort(array: list):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]


def avl_sort(array: list):
    avl_tree = MyAVLTree()
    for i in range(len(array)):
        avl_tree.insert(array[i], 0)
    return avl_tree.tree_traversal()


def heap_sort(array: list):
    my_heap = MyBinomialHeap()
    for n in array:
        my_heap.insert(n)
    to_ret = []
    for i in range(len(array)):
        to_ret.append(my_heap.pop_min())
    return to_ret


def quicksort_deterministic(array: list):  # I used the first value as the pivot
    if len(array) == 1:
        return array
    pivot = 0
    i = 1
    j = len(array) - 1
    while i < j:
        if array[i] < array[pivot]:
            i += 1
        if array[j] > array[pivot]:
            j -= 1
        if array[i] > array[pivot] and array[j] < array[pivot]:
            array[i], array[j] = array[j], array[i]
    while array[pivot] < array[i]:
        i -= 1
    array[pivot], array[i] = array[i], array[pivot]
    pivot = i
    return quicksort_deterministic(array[:pivot]) + quicksort_deterministic(array[pivot:])


def quicksort_random(array: list):
    if len(array) == 1:
        return array
    random = Random()
    pivot = random.randint(0, len(array))
    array[0], array[pivot] = array[pivot], array[0]
    
    i = 1
    j = len(array) - 1
    while i < j:
        if array[i] < array[pivot]:
            i += 1
        if array[j] > array[pivot]:
            j -= 1
        if array[i] > array[pivot] and array[j] < array[pivot]:
            array[i], array[j] = array[j], array[i]
    while array[pivot] < array[i]:
        i -= 1
    array[pivot], array[i] = array[i], array[pivot]
    pivot = i
    return quicksort_deterministic(array[:pivot]) + quicksort_deterministic(array[pivot:])


def count_sort(array: list, max_val: int):  # TODO
    pass


def radix_sort(array: list, max_digits: int):  # TODO
    pass
