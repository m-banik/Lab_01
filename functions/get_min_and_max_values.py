# Funkcja pomocnicza.
def get_min_and_max_values(input_data: list[int]):
    min = input_data[0]
    max = input_data[0]
    for i in input_data:
        if i > max:
            max = i
        if i < min:
            min = i
    return [min, max]
