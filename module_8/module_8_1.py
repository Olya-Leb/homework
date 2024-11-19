# Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        result2 = f'{a}{b}'
        return result2

print(add_everything_up(5, '5'))
print(add_everything_up('5', 0))
print(add_everything_up('string', 5.5))
print(add_everything_up(5.5, '5'))
print(add_everything_up('5.5', '5'))
