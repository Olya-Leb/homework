import random

def def_cipher():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    new_num = list(range(3, 21))
    cipher = random.choice(new_num)
    return cipher

def def_passcode(n):
    passdict = {}
    passdict.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    passdict.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    passdict.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    passdict.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    passdict.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    passdict.update({20: 13141911923282183731746416515614713812911})
    passcode = passdict.get(n)
    return passcode

n = def_cipher()
# n = int(input('Введите шифр: '))
print(f'Шифр: {n}')

pair1 = list(range(1, n))
pair2 = list(range(1, n))
pairs = []
result = ''

for i in pair1:
    for j in pair2:
        p1 = i
        p2 = j
        if p1 >= p2:
            continue
        else:
            kratno = n % (p1 + p2)
            if kratno == 0:
                pairs.append([p1, p2])
                result = result + str(p1) + str(p2)
print('Пары чисел', *pairs)
print(f'Пароль для второго поля: {result}')
if int(result) == def_passcode(n):
    print('Сверка показала, что пароль подобран верно.')
else:
    print('Сверка показала, что пароль подобран неверно.')