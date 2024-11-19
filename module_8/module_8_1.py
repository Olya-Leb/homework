# Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        result2 = f'{a}{b}'
        return result2

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
