def sort_by_placing(input_data: list[int]):
    for i in range(1, len(input_data)):
        element = input_data[i]
        j = i
        while j > 0 and input_data[j - 1] > element:
            input_data[j] = input_data[j - 1]
            j -= 1
        input_data[j] = element
