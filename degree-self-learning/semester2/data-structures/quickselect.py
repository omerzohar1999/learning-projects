from random import Random


def quickselect_random(array: list, pos: int):  
    if len(array) == 1:
        return array[0]
    random = Random()
    pivot = random.randint(0, len(array) - 1)
    pivot_value = array[pivot]
    left_arr = []
    right_arr = []
    for num in array:
        if num < pivot_value:
            left_arr.append(num)
        elif num > pivot_value:
            right_arr.append(num)
    num_of_smaller = len(left_arr)
    if num_of_smaller == pos - 1:
        return pivot_value
    elif num_of_smaller > pos - 1:
        return quickselect_random(left_arr, pos)
    return quickselect_random(right_arr, pos - num_of_smaller - 1)


def test():
    for i in range(1, 6):
        print(quickselect_random([1, 5, 2, 3, 4], i))


test()
