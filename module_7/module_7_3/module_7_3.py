class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name_file in self.file_names:
            with open(name_file, encoding='utf-8') as file:
                contents_file = file.read().lower()
                for mark in marks:
                    contents_file = contents_file.replace(mark, '')
            all_words[name_file] = list(contents_file.split())
        return all_words

    def find(self, word):
        word_position = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                word_position[name] = words.index(word.lower())+1
        return word_position

    def count(self, word):
        num_of_words = {}
        for name, words in self.get_all_words().items():
                num_of_words[name] = words.count(word.lower())
        return num_of_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))