lista=[7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afisare lista ascendent
lista_ascen=lista.copy()
lista_ascen.sort()
# print(lista)
print(lista_ascen)

# afisare lista descendent
lista_descen=lista_ascen.copy()
lista_descen.reverse()
print(lista_descen)

# afisare nr pare

print(lista_ascen[1::2])
# afisare nr impare

print(lista_ascen[::2])

# multiplii 3

print(lista_ascen[2::3])