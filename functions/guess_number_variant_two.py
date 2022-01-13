from random import randint


def guess_number_variant_two(chosen_number: int, min: int = 1, max: int = 1000):
    if max <= min or min <= -1:
      print("Wartość minimalna musi być liczbą całkowitą i mniejszą od maksymalnej.")
      return
    tries = 0
    guess: int = -1
    while guess != chosen_number:
      tries += 1
      guess = randint(min,max)
      if guess < chosen_number:
          min = guess
      elif guess > chosen_number:
          max= guess
    return tries
