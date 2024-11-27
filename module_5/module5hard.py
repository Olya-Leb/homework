from time import sleep

class User:
    def __init__(self, nickname, password, age):
            self.nickname = nickname
            self.password = hash(password)
            self.age = int(age)

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = str(title) # заголовок
        self.duration = int(duration) # продолжительность, секунды
        self.time_now = 0 # секунда остановки
        self.adult_mode = adult_mode # ограничение по возрасту (False по умолчанию)

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
            #     print(f'Пользователь {nickname} вошел в систему')
            # else:
            #     print('Неправильный логин или пароль')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # вход после регистрации
        # print(f'Успешная регистрация! Пользователь {nickname} вошел в систему')

    def log_out(self):
        self.current_user = None
        # print(f'Пользователь вышел из системы')

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
            #     print(f'Видео "{video.title}" добавлено')
            # else:
            #     print(f'Видео "{video.title}" уже существует')

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for second in range(video.time_now, video.duration):
                    print(second + 1, end=' ')
                    sleep(1)
                video.time_now = 0
                print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')