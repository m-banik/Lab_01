from math import floor


# Modyfikuję funkcję z właściwego laboratorium o zmienną globalną do zliczania "domysłów" CPU.
def search_binary_for_number(input_data: list[int], searched_item: int, left: int = 0, right: int = None):
    number_of_tries = 0
    if right is None:
        right = len(input_data) - 1
    result: int or None = None
    while left <= right:
        number_of_tries += 1
        i = floor((left+right)/2)
        if searched_item == input_data[i]:
            result = input_data[i]
            break
        if searched_item > input_data[i]:
            left = i + 1
        else:
            right = i - 1
    return [result, number_of_tries]
