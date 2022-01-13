from .merge import merge


def sort_by_merging(input_data: list[int], left: int = 0, right: int = None):
    if right is None:
        right = len(input_data) - 1
    if right > left:
        middle = int((left + right) / 2)
        sort_by_merging(input_data, left, middle)
        sort_by_merging(input_data, middle + 1, right)
        merge(input_data, left, middle, right)
