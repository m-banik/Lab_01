def sort_by_selection(input_data: list[int]):
    # Zagnieżdżona funkcja pomocnicza.
    def max_element_index(n: int):
        max = 0
        for i in range(1, n):
            if input_data[i] > input_data[max]:
                max = i
        return max
    
    for i in range(len(input_data), 1, -1):
        max = max_element_index(i)
        if max != i - 1:
            input_data[i - 1], input_data[max] =  input_data[max], input_data[i - 1]
