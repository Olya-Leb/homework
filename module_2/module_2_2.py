first = input('Введите первое целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третие целое число: ')
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else: print(0)
