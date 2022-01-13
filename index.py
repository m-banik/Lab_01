import numpy as np
from functions.get_shortest_and_longest_words_from_list import get_shortest_and_longest_words_from_list
from functions.get_mnimal_and_maximal_ascii_code_sum_of_string_by_list import get_mnimal_and_maximal_ascii_code_sum_of_string_by_list
from functions.get_first_and_last_word_of_alphabetically_sorted_list import get_first_and_last_word_of_alphabetically_sorted_list
from classes.checker import Checker
from functions.sort_by_bubbling import sort_by_bubbling
from functions.sort_by_selection import sort_by_selection
from functions.sort_by_placing import sort_by_placing
from functions.sort_by_merging import sort_by_merging
from functions.sort_by_counting import sort_by_counting
from functions.search_binary_for_number_index import search_binary_for_number_index


# Zadanie 1
print()
print("Zadanie 1")
print()
file_path = './assets/dane.txt'

# Zadanie 1a
# Każdorazowo na nowo pobieram dane, by mieć pewność, że operuję na ich oryginalnej postaci.
data: list[str] = np.loadtxt(file_path, delimiter=',', skiprows=0, dtype=str)
result = get_shortest_and_longest_words_from_list(data)
print("Długość najkrótszego słowa:", result[0], str(len(result[0])), ", najdłuższego: ", result[1], str(len(result[1])))


# Zadanie 1b
data: list[str] = np.loadtxt(file_path, delimiter=',', skiprows=0, dtype=str)
result = get_mnimal_and_maximal_ascii_code_sum_of_string_by_list(data)
print("Min:", str(result[0]), ", max: ", str(result[1]))


# Zadanie 1c
data: list[str] = np.loadtxt(file_path, delimiter=',', skiprows=0, dtype=str)
result = get_first_and_last_word_of_alphabetically_sorted_list(data)
print("Pierwsze:", str(result[0]), ", ostatnie: ", str(result[1]))


# Zadanie 2
print()
print("Zadanie 2")
print()

# Testy
print("Ostatni zbiór danych okazał się zbyt opasły i absorbujący.")
print("Ograniczyłem się do badania dwóch pierwszych plików z danymi.")
print()

checker = Checker()
print("Test sortowania bąbelkowego:")
checker.check(sort_by_bubbling)
print()
print("Test sortowania przez wybieranie:")
checker.check(sort_by_selection)
print()
print("Test sortowania przez wstawianie:")
checker.check(sort_by_placing)
print()
print("Test sortowania przez scalanie:")
checker.check(sort_by_merging)
print()
print("Test sortowania przez zliczanie:")
checker.check(sort_by_counting)


# Zadanie 3
print()
print("Zadanie 3")
print()

# Testy.
try:
    samples = [0,1,2,3,4,5,6,7,8,9]
    found_index: int or None = search_binary_for_number_index(samples, 7)
    assert found_index == 7
    found_index = search_binary_for_number_index(samples, 10)
    assert found_index == None
    samples.append(9)
    found_index = search_binary_for_number_index(samples, 9)
    assert found_index == 9
    print("Testy przeszły pomyślnie.")
except AssertionError:
    print("Testy nie przeszły pomyślnie!")
