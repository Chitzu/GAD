a = 2


# def functie():
#     global mesaj # mesaj este global
#     mesaj = "Buna seara"
#     print(mesaj)

# functie()
# print(mesaj)

msj = "buna ziua"

def functie():
    def functie2():
        print(f"a doua func: {msj}")
    global msj
    msj = "Buna seara"
    functie2()
    print(f"functie:{msj}")

functie()
msj = "buna ziua"
print(msj)
