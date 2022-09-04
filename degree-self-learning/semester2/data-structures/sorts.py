from avl_tree import MyAVLTree

def bubble_sort(array: list):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]


def mergesort(array: list):
    pass


def insertion_sort(array: list):
    pass


def avl_sort(array: list):
    avl_tree = MyAVLTree()
    for i in range(len(array)):
        avl_tree.insert(array[i], 0)
    return avl_tree.tree_traversal()


def heap_sort(array: list):
    pass


def quicksort_random(array: list):
    pass


def quicksort_deterministic(array: list):
    pass


def count_sort(array: list):
    pass


def radix_sort(array: list):
    pass
