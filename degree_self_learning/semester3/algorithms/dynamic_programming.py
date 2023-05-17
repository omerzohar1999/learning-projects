def fibonacci_nums_rec(n: int):
    nums = [0, 1]

    def calculate_fib_nums(curr_n: int):
        if curr_n < len(nums):
            return
        elif curr_n == len(nums):
            nums.append(nums[curr_n - 1] + nums[curr_n - 2])
        else:
            calculate_fib_nums(n - 2)
            calculate_fib_nums(n - 1)
            nums.append(nums[curr_n - 1] + nums[curr_n - 2])

    calculate_fib_nums(n)
    return nums[n]


def fibonacci_bottom_up(n: int):
    if n <= 1:
        return 1
    fib_i_minus_1 = 1
    fib_i = 1
    for i in range(n - 1):
        fib_i, fib_i_minus_1 = fib_i + fib_i_minus_1, fib_i
    return fib_i


def max_independent_set_in_arr(arr: list[int]):
    n = len(arr)
    sol = [arr[0], arr[1]]
    for i in range(2, n):
        sol.append(max(sol[i - 1], sol[i - 2] + arr[i]))


def longest_common_subsequence(a: list, b: list) -> list:
    # lemma 1: if a[-1]==b[-1], then lcs is lcs(a[:-1], b[:-1]) + [a[-1]]
    # lemma 2: if a[-1]!=b[-1], then lcs is the longest between lcs(a, b[:-1]) and lcs(a[:-1], b)
    n, m = len(a), len(b)
    lengths = [[0 for j in range(m + 1)] for i in range(n + 1)]
    dirs = [[5 for j in range(m + 1)] for i in range(n + 1)]  # 4 for left, 2 for up, 1 for up-left
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
                dirs[i + 1][j + 1] = 1
            else:
                if lengths[i][j + 1] > lengths[i + 1][j]:
                    lengths[i + 1][j + 1] = lengths[i][j + 1]
                    dirs[i + 1][j + 1] = 2
                else:
                    lengths[i + 1][j + 1] = lengths[i + 1][j]
                    dirs[i + 1][j + 1] = 4
    indexes_a = get_subsequence_from_dirs(dirs, a, n + 1, m + 1)
    subsequence = []
    for i in range(len(subsequence), 0, -1):
        subsequence.append(a[indexes_a[i]])
    return subsequence


def get_subsequence_from_dirs(dirs: list[list[int]], arr: list, i: int, j: int) -> list:
    if i == 0 or j == 0:
        return []
    if dirs[i][j] == 1:
        return get_subsequence_from_dirs(dirs, arr, i - 1, j - 1) + [arr[i - 1]]
    elif dirs[i][j] == 2:
        return get_subsequence_from_dirs(dirs, arr, i - 1, j)
    return get_subsequence_from_dirs(dirs, arr, i, j - 1)


def longest_increasing_subsequence_simple(arr: list):
    sorted_arr = sorted(arr)
    return longest_common_subsequence(arr, sorted_arr)


def longest_increasing_subsequence(arr: list):
    lis = []
    ptrs = []
    max_index = 0
    max_len = 0
    for i in range(len(arr)):
        curr_len = 1
        curr_ptr = None
        for j in range(i):
            if arr[i] >= arr[j] and lis[j] >= curr_len:
                curr_len = lis[j] + 1
                curr_ptr = j
        lis.append(curr_len)
        ptrs.append(curr_ptr)
        if curr_len > max_len:
            max_len = curr_len
            max_index = i
    indexes = get_subsequence_from_ptrs(max_index, ptrs)
    return [arr[i] for i in indexes]


def get_subsequence_from_ptrs(index: int, ptrs: list) -> list:
    if ptrs[index] is None:
        return [index]
    return get_subsequence_from_ptrs(ptrs[index], ptrs) + [index]


def knapsack_01(items: list[tuple[int, int]], knapsack_capacity: int):
    items.sort(key=lambda x: x[1])
    mat_values = [[0 for j in range(knapsack_capacity)] for i in range(len(items))]
    for i in range(1, len(items)):
        for j in range(1, knapsack_capacity):
            if j > items[i][0]:
                mat_values[i][j] = mat_values[i-1][j]
            else:
                mat_values[i][j] = max(mat_values[i-1][j], items[i][1] + mat_values[i-1][j-items[i][0]])
    return find_items_from_values_matrix(mat_values, items)


def find_items_from_values_matrix(mat: list[list[int]], items: list[tuple[int, int]]):
    items_in_knapsack = []
    ptr1, ptr2 = len(mat), len(mat[0])
    while ptr1 > 0 and ptr2 > 0:
        if mat[ptr1][ptr2] != mat[ptr1-1][ptr2]:
            items_in_knapsack.append(items[ptr1])
            ptr2 -= items[ptr1][0]
        ptr1 -= 1
    return items_in_knapsack


def optimal_static_bst(frequencies: list[float]):
    n = len(frequencies)
    mat = [[(float('inf'), None) if j < i else (.0, None) for j in range(n+1)] for i in range(n+1)]
    sums = [[None if j < i else .0 for j in range(n)] for i in range(n)]
    for i in range(n):
        sums[i][i] = frequencies[i]
    for i in range(n):
        for j in range(i+1, n):
            sums[i][j] = sums[i][j-1] + frequencies[j]
    inf = float('inf')

    def osb_rec(i: int, j: int) -> float:
        if mat[i][j][0] != inf:
            return mat[i][j][0]
        min_val = float('inf')
        min_index = i
        for k in range(i, j+1):
            curr_partition = osb_rec(i, k-1) + osb_rec(k+1, j)
            if curr_partition < min_val:
                min_val = curr_partition
                min_index = k
        mat[i][j] = (min_val + sums[i][j+1], min_index)
        return mat[i][j][0]

    return osb_rec(1, n)
