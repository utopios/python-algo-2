from fonctions.fonctions import dire_bonjour
from functools import *


liste_a = [1,5,4,3]

def main():
    dire_bonjour()
    print(reduce(lambda a,b: a+b, liste_a))


if __name__ == "__main__":
    main()