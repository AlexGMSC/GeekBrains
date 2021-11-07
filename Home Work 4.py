def sal():
    try:
        time = float(input('Введите отработанное время: '))
        salary = int(input('Введите часовую оплату: '))
        bonus = int(input('Введите премию: '))
        res = time * salary + bonus
        print(f'Заработаня оплата сотрудника:  {res}')
    except ValueError:
        return print('Not a number')
sal()


## Задание 2.

my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')


## Задание 3.

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')


## Задание 4.

start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in start_list if start_list.count(i) == 1]
print(new_list)


## Задание 5.

from functools import reduce
new_list = [i for i in range(100,1000) if i % 2 == 0]
summa = reduce((lambda x, y: x * y), new_list)
print(summa)


## Задание 6.

from itertools import cycle, count

v_start = int(input('Введите число: '))
v_stop = v_start * 2 + 10 + 1

# v.1
for i in count(v_start):
    if i < v_stop:
        print(i)
    else:
        break
del i

# v.2
my_list = [i for i in range(v_stop)]
count = 0
for b in cycle(my_list):
    if count < v_stop + 10:
        print(b)
        count += 1
    else:
        break


## Задание 7.

from math import factorial


def fact(n: int):
     for i in range(1, n + 1):
        yield factorial(i)

if __name__ == '__main__':
    input_data = input('Введите количество вычисленных факториалов: ')

    try:
        value = int(input_data)
    except ValueError as e:
        print(e)
        exit(1)

    for el in fact(value):
        print(el)