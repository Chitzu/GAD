#ordinea din try este importanta , nu cea de jos
#IndexError , nameerr.. inainte de Exception
variabila = input("Adauga un nr: ")
# variabila = int(variabila)

lista = [1,2,3]
try:
    if variabila.isdigit():
        raise ValueError  #Ne arunca pe Exceptia ValueError
    print(lista[3])
    print(a)  # NameError - nu e variabila def
    variabila = int(variabila)

except ValueError:   # ValueError apartine in Exception
    print("exceptie")
    if variabila.isdigit():
        variabila = int(variabila)
    a = None

except NameError:
    print('variabila nedef')

except IndexError:
    print('eroare de index')
    print(lista[3:4])

except Exception:   # clasa cu toate exceptiile din py
    print('clasa default')

else:
    print("nu exista nicio exceptie")
finally:
    print("se ruleaza oricum")

print(variabila,'variabila')
print(a,'a')
