# def my_lambda(x, y):
#     return x+y
# FUNCTII care ne ajuta sa scriem functii pe un singur rand

# my_lambda = lambda x, y: x + y

# suma = my_lambda(2, 3)
# print(suma)

player = [
    {
        "first_name": 'Ion',
        "last_name": "Popescu",
         "varsta": 12
     },
    {
        "first_name": 'Ana',
         "last_name": "Maria",
        "varsta": 13
     },
    {
        "first_name": 'Iza',
        "last_name": "Enache",
        "varsta": 20
     }
]

jucatori_sortati = sorted(player, key=lambda jucator: jucator["last_name"])
print(jucatori_sortati)
