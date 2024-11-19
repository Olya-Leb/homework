# Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print(f'{a}{b}')

add_everything_up(5, '5')
add_everything_up('5', 0)
add_everything_up('string', 5.5)
add_everything_up(5.5, '5')
add_everything_up('5.5', '5')