"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def shifter_1(num, sh=''):
    if int(num) > 0:
        last_digit = int(num) % 10
        sh = sh + str(last_digit)
        num = int(num) // 10
        return shifter_1(num, sh)
    return sh


def shifter():
    num = input('Введите число, которое требуется перевернуть: ')
    if not num.isdigit():
        print('Введено недопустимае значение. Повторите ввод.')
        return shifter()
    else:
        return shifter_1(num)


print(shifter())
