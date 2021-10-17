# Задание 1

my_int = 5
my_float = 1.2
my_str = "GeekBrains rules!"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'city': 'Сидней', 'country': 'Австралия'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')

# Задание 2

el_count = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка: "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)



# Задание 3

seasons_list = [
    ['Зимой', ['12', '1', '2']],
    ['Весной', ['3', '4', '5']],
    ['Летом', ['6', '7', '8']],
    ['Осенью', ['9', '10', '11']]
]

month_dict = {
    'Январь': ['1'],
    'Февраль': ['2'],
    'Март': ['3'],
    'Апрель': ['4'],
    'Май': ['5'],
    'Июнь': ['6'],
    'Июль': ['7'],
    'Август': ['8'],
    'Сентябрь': ['9'],
    'Октябрь': ['10'],
    'Ноябрь': ['11'],
    'Декабрь': ['12'],

}

while True:
    month_number = input('Введите номер месяца: ')
    if month_number not in sum(month_dict.values(), []):
        print('Несуществующий месяц. Попробуйте еще раз :-)')
        continue

    break

for season, months in month_dict.items():
    if month_number in months:
        print(f'Месяц с номером {month_number} это {season}')

for season, months in seasons_list:
    if month_number in months:
        print(f'Месяц с номером {month_number} является {season}')


# Задание 4

while True:
    var_str = input('Введите несколько слов, разделяя их пробелами: ')
    if len(var_str) < 3 or var_str.count(' ') < 1:
        print('Неправильные данные. Попробуйте еще раз :-)')
        continue

    break

for idx, word in enumerate(var_str.split()):
    print(idx + 1, (word, word[:11])[len(word) > 10])



# Задание 5

raiting = []

while True:
    item = input('Введите элемент рейтинга: ')
    if not item.isdigit():
        print("Введены некорректные данные :-( Попробуйте еще раз.")
        continue
    else:
        item = int(item)

    idx = None

    for i, num in enumerate(raiting):
        if item > num:
            idx = i
            break

    if idx is None:
        raiting.append(item)
    else:
        raiting.insert(idx, item)

    print(raiting)

    q = input('Формирование списка завершено? (y/n)) ')
    if q.lower() == 'y':
        break



# Задание 6

products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalnum():
            print('Наименование товара не может быть пустым. Попробуйте еще раз.')
            continue

        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть целым числомю. Попробуйте еще раз.')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз.')
            continue

        amount = int(tmp)

    tmp = input('Введите единицы измерения: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой. Попробуйте еще раз.')
        continue

    unit = tmp

    products.append((
        order,
        {
            'title': title,
            'price': price,
            'amount': amount,
            'unit': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Формирование списка завершено? (y/n)) ')
    if q.lower() == 'y':
        break

analitics = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()
}

for _, item in products:
    analitics['title'].append(item['title'])
    analitics['price'].append(item['price'])
    analitics['amount'].append(item['amount'])
    analitics['unit'].add(item['unit'])

print(analitics)
