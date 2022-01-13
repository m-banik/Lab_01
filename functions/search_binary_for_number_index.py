from math import floor


def search_binary_for_number_index(input_data: list[int], searched_item: int, left: int = 0, right: int = None):
    if right is None:
        right = len(input_data) - 1
    while left <= right:
        i = floor((left+right)/2)
        if searched_item == input_data[i]:
            return i
        if searched_item > input_data[i]:
            left = i + 1
        else:
            right = i - 1
