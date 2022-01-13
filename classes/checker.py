from types import FunctionType
import time


class Checker():
    
    def __init__(self, file_paths: list[str] = ['./assets/sort1.txt', './assets/sort2.txt']):
        self.__file_paths = file_paths
        # Pełna lista zasobów - zakomentowana, bo ostatni zbiór danych okazał się zbyt opasły i absorbujący.
        # self.__file_paths = ['./assets/sort1.txt', './assets/sort2.txt', './assets/sort3.txt']
    
    # Metoda do sprawdzenia czasu wykonywania danego programu.
    # Używam Pythona w wersji 3.9.5 x64. Kod zaproponowany przez doktora Żelaznego u mnie nie działał.
    def __check_for_how_long_programm_works(self, programm: FunctionType, argument: list[int]):
        global time
        start = time.process_time()
        programm(argument)
        stop = time.process_time()
        print("--- %s sekund ---" % round(stop - start,2))
    
    def check(self, programm: FunctionType):
        for file_path in self.__file_paths:
            data = open(file_path, "r").readlines()[0].split()
            data = list(map(int, data))
            print("Dla ścieżki: ", file_path)
            self.__check_for_how_long_programm_works(programm, data)
