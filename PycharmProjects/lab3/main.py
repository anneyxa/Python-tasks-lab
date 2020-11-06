from counter import count_forms, count_di_grams, count_tri_grams
from sorter import insertion_sort, selection_sort_unstable, selection_sort_stable

if __name__ == '__main__':
    sample = [2, 5, 1, 9, 9, 6, 3]
    print(f'{sample} sorted by selection_sort_unstable: {selection_sort_unstable(sample)}')
    sample = [2, 5, 1, 9, 9, 6, 3]
    print(f'{sample} sorted by selection_sort_stable: {selection_sort_stable(sample)}')
    sample = [2, 5, 1, 9, 9, 6, 3]
    print(f'{sample} sorted by insertion_sort: {insertion_sort(sample)}')

    print(count_forms("potop.txt"))
    print(count_di_grams("potop.txt"))
    print(count_tri_grams("potop.txt"))



