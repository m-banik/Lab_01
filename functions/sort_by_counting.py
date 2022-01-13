from .get_min_and_max_values import get_min_and_max_values


def sort_by_counting(input_data: list[int]):
    min_max = get_min_and_max_values(input_data)
    min = min_max[0]
    max = min_max[1]
    counters_size = max - min + 1
    counters = [0] * counters_size
    for i in range(len(input_data)):
        counters[input_data[i] - min] += 1
    last_index = 0
    for j in range(counters_size):
        k = last_index
        while k < counters[j] + last_index:
            input_data[k] = j + min
            k += 1
        last_index = k
