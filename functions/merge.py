# Funkcja pomocnicza.
def merge(input_data: list[int], left_border: int, middle_border: int, right_border: int):
    left_size = middle_border - left_border + 1
    right_size = right_border - middle_border
    left = [0] * left_size
    right = [0] * right_size
    # Tablice pomocnicze.
    for i in range(left_size):
        left[i] = input_data[left_border + i]
    for j in range(right_size):
        right[j] = input_data[middle_border + j + 1]
    # Zmienne pomocnicze z indeksami.
    left_index = 0
    right_index = 0
    current_index = left_border
    while left_index < left_size and right_index < right_size:
        if left[left_index] <= right[right_index]:
            input_data[current_index] = left[left_index]
            left_index += 1
        else:
            input_data[current_index] = right[right_index]
            right_index += 1
        current_index += 1
    while left_index < left_size:
        input_data[current_index] = left[left_index]
        current_index += 1
        left_index += 1
    while right_index < right_size:
        input_data[current_index] = right[right_index]
        current_index += 1
        right_index += 1
