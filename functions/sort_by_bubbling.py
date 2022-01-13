def sort_by_bubbling(input_data: list[int]):
    for _ in range(len(input_data) - 1):
        for i in range(0, len(input_data) - 1):
            if input_data[i] > input_data[i + 1]:
                input_data[i], input_data[i + 1] = input_data[i + 1], input_data[i]
