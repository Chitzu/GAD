# cuvant = ' o n o m a t o p e e '
# daca literea de inceput si lit de sfarsit
# se gasesc in interiorul cuvantului , litera trb sa fie vizibila
# cuvant = ' o _ o _ _ _ o _ e e'
# 7 incercari

import random
from cuvinte_spanzuratoarea import cuvinte_de_ghicit as lista_cuvinte

cuvant_de_ghicit = random.choice(lista_cuvinte).lower()
cuvant = list(cuvant_de_ghicit)


def parcurgere_cuvant(word: str, simbol_de_inlocuit: str, cuvant_ascuns: list) -> list:
    """

    :param word: reprezinta cuv care trebuie ghicit
    :param simbol_de_inlocuit: simbolul cu care se inlocuieste
    :param cuvant_ascuns: cuvantul modificat dupa introducerea de caracter
    :return: cuvantul modificat
    """
    for index, value in enumerate(cuvant):
        if simbol_de_inlocuit == '_' and word[0] != value and word[-1] != value:
            cuvant_ascuns[index] = simbol_de_inlocuit
        elif value == simbol_de_inlocuit and word[0] != value and word[-1] != value:
            cuvant_ascuns[index] = simbol_de_inlocuit
    return cuvant_ascuns


cuvant_de_afisat = ' '.join(parcurgere_cuvant(cuvant_de_ghicit, '_', cuvant))
print(f"Cuvantul de ghicit este : {cuvant_de_afisat}")

# sa nu fie cifra    =>  string.isdigit()
# sa nu introduca mai mult de 1 caracter  => len(string) > 1
# sa nu fie spatiu

litere_incercate = set()
nr_incercari = 0

while nr_incercari < 7:
    if len(list(litere_incercate)) > 0:
        print(f"Literele incercate sunt :{','.join(litere_incercate)}")
    litera_de_incercat = input("Adauga o litera: ").lower()
    while litera_de_incercat.isalpha() is False or len(litera_de_incercat) > 1 or litera_de_incercat in ["", " "]:

        if litera_de_incercat.isalpha() is False:
            print(f"Ai adaugat o cifra ")

        if len(litera_de_incercat) > 1:
            print(f"Ai adaugat mai multe caractere")

        if litera_de_incercat == "":
            print("Ai adaugat un spatiu")
        litera_de_incercat = input("Adaugat mai multe : ").lower()

    if litera_de_incercat not in cuvant_de_ghicit:
        nr_incercari += 1
        litere_incercate.add(litera_de_incercat)

    elif litera_de_incercat in cuvant_de_ghicit and (
            cuvant_de_ghicit[0] != litera_de_incercat and cuvant_de_ghicit[-1] != litera_de_incercat):
        # for index , value in enumerate(cuvant_de_ghicit):
        #     if value == litera_de_incercat:
        #         cuvant[index] = litera_de_incercat
        cuvant = parcurgere_cuvant(cuvant_de_ghicit, litera_de_incercat, cuvant)

    if nr_incercari == 7:
        print(f"Ai pierdut . Cuvantul era:{cuvant_de_ghicit}")
    elif '_' not in cuvant:
        print("Ai castigat")
        break
    if (numar_incercercari_ramase := 7 - nr_incercari) and numar_incercercari_ramase > 0:
        print(f"Mai ai {numar_incercercari_ramase} incercari")
    print(" ".join(cuvant))

