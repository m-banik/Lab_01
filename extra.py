from random import randint
from functions.get_number_from_user import get_number_from_user
from functions.guess_number_variant_one import guess_number_variant_one
from functions.guess_number_variant_two import guess_number_variant_two
from functions.search_binary_for_number import search_binary_for_number
from functions.sort_by_counting import sort_by_counting
from functions.search_binary_for_number_index import search_binary_for_number_index


# Zadanie 1.
print()
print("Zadanie 1")
print()
# Zmienne globalne.
chosen_number: int
number_of_guesses: int

# Zadanie 1a.
print("Zadanie 1a")
chosen_number = get_number_from_user()
number_of_guesses = guess_number_variant_one(chosen_number)
print("Liczba zgadnięć: ", str(number_of_guesses))
print()

# Zadanie 1b.
# Dla pewności zeruję zmienne globalne.
chosen_number = 0
number_of_guesses = 0
print("Zadanie 1b")
chosen_number = get_number_from_user()
number_of_guesses = guess_number_variant_two(chosen_number)
print("Liczba zgadnięć: ", str(number_of_guesses))
print()

# Zadanie 1c
# Dla pewności zeruję zmienne globalne.
chosen_number = 0
number_of_guesses = 0
# Tworzę dane do wyszukiwania binarnego.
numbers: list[int] = []
for i in range(1, 1001):
    numbers.append(i)


print("Zadanie 1c")
chosen_number = get_number_from_user()
number_of_guesses = search_binary_for_number(numbers, chosen_number)[1]
print("Liczba iteracji w wyszukiwaniu binarnym: ", str(number_of_guesses))
print()


# Zadanie 2
print()
print("Zadanie 2")
print()

print("Zmniejszyłem ilość prób do 10000 wbrew zadaniu dla przyśpieszenia prac.")
print("Trwają obliczenia. Proszę czekać...")

checked_functions = [guess_number_variant_one, guess_number_variant_two, search_binary_for_number]
average_number_of_guesses: list[float] = []
for i in range(0, len(checked_functions)):
    # Dla pewności zeruję zmienne globalne.
    chosen_number = 0
    number_of_guesses = 0
    # Zmniejszyłem ilość prób do 10000 wbrew zadaniu dla przyśpieszenia prac.
    for _ in range(0, 10000):
    # for _ in range(0, 1000000):
        chosen_number = randint(1, 1000)
        if i == len(checked_functions) - 1:
            numbers = []
            for j in range(1, 1001):
                numbers.append(j)
            number_of_guesses += checked_functions[i](numbers, chosen_number)[1]
        else:
            number_of_guesses += checked_functions[i](chosen_number)
    # To samo. Zmniejszyłem ilość prób do 10000 wbrew zadaniu dla przyśpieszenia prac.
    average_number_of_guesses.append(number_of_guesses/10000)
    # average_number_of_guesses.append(number_of_guesses/1000000)


print()
for i in range(0, len(average_number_of_guesses)):
    task_id = "A"
    if i == 1:
        task_id = "B"
    elif i == 2:
        task_id = "C"
    stringified_result = str(average_number_of_guesses[i])
    print("Średnia liczba prób dla podpunktu " + task_id + ":", stringified_result)


# Zadanie 3
print()
print("Zadanie 3")
print()


# Tworzę ścieżki do plików i tablicę dwuwymiarową na dane(krotka/tuple - ma dokładnie dwa elementy).
file_paths = ['./assets/plik1.txt', './assets/plik2.txt']
data: list[list[int], list[int]] = [
  [],
  []
]

for i in range(0, len(file_paths)):
    data_from_file = open(file_paths[i], "r").readlines()[0].split()
    data_from_file = list(map(int, data_from_file))
    sort_by_counting(data_from_file)
    data[i] = data_from_file


# Krotka/tuple - ma dokładnie trzy elementy.
results: list[list[int], list[int], list[int]] = [[], [], []]
for number in data[0]:
    index = search_binary_for_number_index(data[1], number)
    if index is None:
        is_to_be_added = True
        for first_list_element in results[0]:
            if first_list_element == number:
                is_to_be_added = False
                break
        if is_to_be_added is True:
            results[0].append(number)
    else:
        is_to_be_added = True
        for common_list_element in results[2]:
            if common_list_element == number:
                is_to_be_added = False
                break
        if is_to_be_added is True:
            results[2].append(number)


for number in data[1]:
    index = search_binary_for_number_index(results[2], number)
    if index is None:
        is_to_be_added = True
        for second_list_element in results[2]:
            if second_list_element == number:
                is_to_be_added = False
                break
        if is_to_be_added is True:
            results[1].append(number)


print("Lista liczb unikatowych dla pierwszego zbioru: ", results[0])
print("Lista liczb unikatowych dla drugiego zbioru: ", results[1])
print("Lista liczb współdzielonych przez oba zbiory: ", results[2])
