# Задание 1.

def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    except ValueError:
        return "Вводить можно только цифры/числа."
print(my_func(int(input("Введите делимое: ")), int(input("Введите делитель: "))))


# Задание 2.

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Гвоздков', name='Алексей', year='1992', city='Москва', email='email@gmail.com',
              telephone='+7 (977) 977-97-97'))


# Задание 3.

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Результат: {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')


# Задание 4.

def my_func(x, y):
    return 1 / x ** abs(y)
    #return x ** y
print(my_func(2, -3))


# Задание 5.

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_sum()


# Задание 6.

def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()