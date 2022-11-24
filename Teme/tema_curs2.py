# ex 1
def your_function(*args, **kwargs):
    suma=0
    for i in args:
        if type(i) == int or type(i) == float:
            suma += i
    return suma
 print(your_function(1, 5, -3 , "abc", [12,56,'cad']))

# ex 2
def suma_recurs(param, tip):
    # tip == 0 -> suma totala
    # tip == 1 -> suma para
    # tip == 2 -> suma impara
    if tip == 0:
        if param <= 1:
            return param
        return param + suma_recurs(param - 1, 0)

    elif tip == 1:
        if param <= 2:
            return param
        if param % 2 == 0:
            return param + suma_recurs(param - 1, 1)
        else:
            return suma_recurs(param - 1, 1)

    elif tip == 2:
        if param <= 1:
            return param
        if param % 2 != 0:
            return param + suma_recurs(param - 1, 2)
        else:
            return suma_recurs(param - 1, 2)

 print(5,0)

# ex 3
def citire():
    a = input("Adauga un numar: ")
    if a.isdigit() is True:
        return a
    else:
        return 0

print(citire())