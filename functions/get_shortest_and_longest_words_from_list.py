def get_shortest_and_longest_words_from_list(str_list: list[str]):
    for _ in range(len(str_list) - 1):
        for i in range(0, len(str_list) - 1):
            if len(str_list[i]) > len(str_list[i + 1]):
                str_list[i], str_list[i + 1] = str_list[i + 1], str_list[i]
    return [str_list[0], str_list[len(str_list)-1]]
