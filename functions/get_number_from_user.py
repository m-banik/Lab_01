# Funkcja pomocnicza.
def get_number_from_user():
    chosen_number: int
    while True:
      try:
          chosen_number = int(input("Proszę podać liczbę całkowitą z przedziału 1-1000. "))
          if chosen_number < 1 or 1000 < chosen_number:
            raise ValueError
          break
      except ValueError:
          print("Podano nieprawidłową danę!")
    return chosen_number
