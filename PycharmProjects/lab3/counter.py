from collections import Counter


def count_forms(path):
    form_list = get_list_of_forms(path)
    counter = Counter(form_list)
    return counter.most_common()


def count_di_grams(path):
    form_list = get_list_of_forms(path)
    di_grams = [(form_list[i], form_list[i + 1]) for i in range(len(form_list) - 1)]    # ta lista bardzo rośnie ze wzrostem n
    most_common = Counter(di_grams).most_common()
    return get_top_20_with_ex_equo(most_common)


def count_tri_grams(path):  # DRY
    form_list = get_list_of_forms(path)
    tri_grams = [(form_list[i], form_list[i + 1], form_list[i + 2]) for i in range(len(form_list) - 2)]
    most_common = Counter(tri_grams).most_common()
    return get_top_20_with_ex_equo(most_common)


def get_list_of_forms(path):
    try:
        with open(path, "r+") as txt_file:
            txt_string = txt_file.read()    # trzeba całość wczytywać do pamięci?
            for punct in '.,?!:;-':
                txt_string = txt_string.replace(punct, "")  # jeśli usuwa Pani łącznik (-) to lepiej zastępować spacją; vide biało-czerwona

            return txt_string.lower().split()
    finally:
        txt_file.close()    # jeśli używa Pani bloku with to close jest już niepotrzebne


def get_top_20_with_ex_equo(most_common):
    top_results = most_common[:20]
    value = most_common[19][1]
    i = 20
    while most_common[i][1] == value:
        top_results.append(most_common[i])
        i += 1
    return top_results
