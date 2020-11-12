def insertion_sort(a):  # stable - equal elements will not be re-arranged in final sort one to another
    n = len(a)
    for i in range(1, n):
        current_val = a[i]
        prev_index = i - 1

        while prev_index >= 0 and a[prev_index] > current_val:
            a[prev_index + 1] = a[prev_index]
            prev_index -= 1
        a[prev_index + 1] = current_val
    return a
# theoretically this list doesn't have to be returned, because it's changed already,
# but I'd like it to be returned anyway (in selection_sorts also)


def selection_sort_unstable(a):  # this one is not stable -
    # equal elements can be re-arranged in final sort order relative to one another
    n = len(a)
    for i in range(n):
        index_min = i
        for j in range(i + 1, n):
            if a[j] < a[index_min]:
                index_min = j
        a[index_min], a[i] = a[i], a[index_min]
    return a


def selection_sort_stable(a):  # this one is stable
    n = len(a)
    for i in range(n):
        index_min = i
        for j in range(i + 1, n):
            if a[j] < a[index_min]:
                index_min = j
            current_min = a[index_min]    # czy linijki 35-39 nie powinny mieć jedno wcięcie mniej?
            while index_min > i:
                a[index_min] = a[index_min - 1]
                index_min -= 1
            a[index_min] = current_min
    return a
