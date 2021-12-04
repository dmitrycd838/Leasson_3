# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devision(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    except TypeError:
        return "Неверные входные данные"
print(devision(5, 7))
print(devision(21, 7))
print(devision(90, 9))
print(devision("10", 2))
print(devision(5, 0))