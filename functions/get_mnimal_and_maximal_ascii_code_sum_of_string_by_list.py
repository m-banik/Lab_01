def get_mnimal_and_maximal_ascii_code_sum_of_string_by_list(input_list: list[str or int]):
    for i in range(0, len(input_list)):
        ascii_sum = 0
        for letter in input_list[i]:
            ascii_sum += ord(letter)
        input_list[i] = ascii_sum
    for _ in range(len(input_list) - 1):
        for j in range(0, len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return [input_list[0], input_list[len(input_list) - 1]]
