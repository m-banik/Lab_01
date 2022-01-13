def get_first_and_last_word_of_alphabetically_sorted_list(str_list: list[str]):
    for _ in range(len(str_list) - 1):
        for j in range(0, len(str_list) - 1):
            if str_list[j] > str_list[j + 1]:
                str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]
    return [str_list[0], str_list[len(str_list)-1]]
