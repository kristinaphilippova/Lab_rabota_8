from typing import List


def taxi_assignment(N, distances, tariffs):
    # Создаем список индексов такси от 0 до N-1
    taxi_indexes = list(range(N))

    # Сортируем такси по тарифу за 1 км
    sorted_taxis = sorted(taxi_indexes, key=lambda x: tariffs[x])

    # Выбираем такси с минимальным тарифом для каждого сотрудника
    assignment = [sorted_taxis[i] + 1 for i in range(N)]

    # Считаем суммарную стоимость поездок
    total_cost = sum(distances[i] * tariffs[assignment[i] - 2] for i in range(N))

    return assignment, total_cost


def convert_to_words(number):
    ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
             'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = ['', 'тысяча', 'тысячи', 'тысяч']

    # Проверка введенного числа
    if not 1 <= number <= 100000:
        return "Введенное число не входит в диапазон от 1 до 100000"

    # Функция для преобразования двух последних цифр числа
    def convert_last_two_digits(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        else:
            tens_digit = num // 10
            ones_digit = num % 10
            return tens[tens_digit] + ' ' + ones[ones_digit]

    # Преобразование числа в словесное представление
    if number == 0:
        word = 'ноль'
    else:
        word = ''
        # Обработка тысяч
        if number >= 1000:
            thousands_digit = number // 1000
            if thousands_digit == 1:
                word += 'одна '
            elif thousands_digit == 2:
                word += 'две '
            else:
                word += convert_last_two_digits(thousands_digit) + ' '
            word += thousands[get_thousands_index(thousands_digit)] + ' '
            number %= 1000

        # Обработка сотен
        if number >= 100:
            hundreds_digit = number // 100
            word += hundreds[hundreds_digit] + ' '
            number %= 100

        # Обработка десятков и единиц
        if number >= 20:
            tens_digit = number // 10
            word += tens[tens_digit] + ' '
            number %= 10
        word += convert_last_two_digits(number)

    # Вывод словесного представления суммы с правильным окончанием валюты
    if word.endswith('один'):
        word += ' рубль'
    elif word.endswith('два') or word.endswith('три') or word.endswith('четыре'):
        word += ' рубля'
    else:
        word += ' рублей'

    # Первое слово с большой буквы
    word = word.capitalize()

    return word
def get_thousands_index(num):
    if 5 <= num % 100 <= 20 or num % 10 >= 5 or num % 10 == 0:
        return 3
    elif 2 <= num % 10 <= 4:
        return 2
    else:
        return 1

# Ввод исходных данных
N = int(input("Введите количество сотрудников компании: "))
distances = [int(x) for x in input("Введите расстояния в километрах через пробел: ").split()]
tariffs = [int(x) for x in input("Введите тарифы в рублях через пробел: ").split()]

# Получение результатов
assignment, total_cost = taxi_assignment(N, distances, tariffs)

# Вывод результата
print("Вариант рассадки сотрудников (номера такси):", *assignment)
if total_cost < 11 or total_cost > 20:
        if total_cost % 10 == 1:
            print("Сумма в рублях:", total_cost, ' рубль')
        elif total_cost % 10 == 2 or total_cost % 10 == 3 or total_cost % 10 == 4:
             print("Сумма в рублях:", total_cost, ' рубля')
        else:
            print("Сумма в рублях:", total_cost, ' рублей')
else:
    print("Сумма в рублях:", total_cost, ' рублей')
print("Сумма словами в рублях:", convert_to_words(total_cost))
