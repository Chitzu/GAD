# num_calls = 0
#
# def exercitiu(x):
#     global num_calls
#     num_calls = 3
#     print(num_calls, '7')
#     num_calls += 2
#     return x * x
#
# print(num_calls, '12')
# print(exercitiu(4))
# print(num_calls, '14')


#2

#cauta val in fisier si o ia de unde o gaseste

# x = 1
#
# def f():
#     return x
#
# print(x)
# print(f())


#3

# x = [1, 2, 'hello' , "cinci" , ['another', 'list']]
# print(len(x[3]))

#4

# x = (1, 2, 3)
# x[1] = 4
# print(x)

#5

#
# a = [1, 2, 3]
# b = [4, 5]
# print(a + b * 3)   #[1, 2, 3, 4, 5, 4, 5, 4, 5]


#6

# x = [1, 2, 3, 4]
# print(x[-1:])

#7

# x = [0, 1, [2]]
# x[2][0] = 3
# print(x)
# x[2].append(4)
# x[2] = 2  # pune 2 in loc de lista de acolo
# print(x)

#8

#
# def exercitiu(i):
#     for i in range(i):
#         return i
#
# x = exercitiu(3)
# print(x)



#9

# a = range(10)
# y = [x * x for x in a if x % 2 == 0]
# print(y)

#10

# def make_account():
#     return {'balance': 0}
#
# def deposit(account, amount):
#     account['balance'] += amount
#     return account['balance']
#
# a = make_account()
# print(deposit(a,10))
