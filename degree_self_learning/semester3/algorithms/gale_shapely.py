import sys
sys.path[0] = sys.path[0][:-21]
sys.path.insert(0, '..')
from semester2.data_structures.linked_list import MyLinkedList


def stable_coupling(num_of_people: int, men_pref: list, women_pref: list):  # TODO
    """
    num_of_people: even number 

    """
    women_rank = calculate_women_rank(women_pref)
    proposed = []
    engaged = []
    proposed.append(-1)
    engaged.append(-1)
    free_men = MyLinkedList((num_of_people // 2) - 1)
    for i in range(1, num_of_people//2):
        free_men.insert_first((num_of_people // 2) - i - 1)
        proposed.append(-1)
        engaged.append(-1)
    while not free_men.is_empty():
        current_man = free_men.pop_first()
        proposed[current_man] += 1
        preferred_woman = men_pref[current_man][proposed[current_man]]
        print(current_man, ",", preferred_woman)
        print(engaged)
        if engaged[preferred_woman] == -1:
            engaged[preferred_woman] = current_man
        else:
            opponent = engaged[preferred_woman]
            if women_rank[preferred_woman][current_man] < women_rank[preferred_woman][opponent]:
                engaged[preferred_woman] = current_man
                free_men.insert_first(opponent)
            else:
                free_men.insert_first(current_man)
    return engaged


def calculate_women_rank(women_pref: list) -> list:
    women_rank = []
    for i in range(len(women_pref)):
        print("working on woman", i)
        print(women_pref[i])
        current_woman_rank = []
        for j in range(len(women_pref[i])):
            current_woman_rank.append(0)
        print(current_woman_rank)
        for j in range(len(women_pref[i])):
            current_woman_rank[women_pref[i][j]] = j
        women_rank.append(current_woman_rank)
    print(women_rank)
    return women_rank


def test():
    men_pref = [[1, 3, 2, 0], [3, 0, 1, 2], [3, 1, 2, 0], [0, 1, 2, 3]]
    women_pref = [[0, 1, 2, 3], [1, 2, 3, 0], [1, 3, 0, 2], [0, 2, 3, 1]]
    num_of_people = 8
    coupling = stable_coupling(num_of_people, men_pref, women_pref)
    for i in range(len(coupling)):
        print(i + 1, ",", coupling[i] + 1)


test()
