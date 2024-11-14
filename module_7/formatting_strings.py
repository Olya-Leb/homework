"""
Домашнее задание по теме "Форматирование строк".
"""

# Использование %:

team1_num = 5
print('В команде Мастера кода участников: %s !' % team1_num) # количество участников первой команды
team2_num = 6
print('Итого сегодня в командах участников: %s и %s !\n' % (team1_num, team2_num)) # количество участников в обеих командах

# Использование format():

score_2 = 42
print('Команда Волшебники данных решила задач: {} !'.format(score_2)) # количество задач решённых командой
# team1_time = 18015.2
print('Волшебники данных решили задачи за {team1_time} с !\n'.format(team1_time=18015.2)) # время за которое команда 2 решила задачи

# Использование f-строк:

score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.') # количество решённых задач по командам
challenge_result = 'победа команды Мастера кода!'
print(f'Пример итоговой строки: {challenge_result}') # исход соревнования
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!') # количество задач и среднее время решения
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg} секунды на задачу!\n') # количество задач и среднее время решения

# Пример входных данных:

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 2)} секунды на задачу!') # количество задач и среднее время решения

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(challenge_result)
