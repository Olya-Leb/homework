from pprint import pprint # импорт функции "pretty-print", из модуля "pretty-print"

class Product:
    """Класс описывающий Продукт"""
    def __init__(self, name, weight, category):
        self.name = str(name) # название продукта (строка)
        self.weight = float(weight) # общий вес товара (дробное число) (5.4, 52.8 и т.п.)
        self.category = str(category) # категория товара (строка)

    def __str__(self):
        """Метод, который возвращает строку в формате '<название>, <вес>, <категория>'.
        Все данные в строке разделены запятой с пробелами."""
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    """Класс описывающий Магазин"""

    __file_name = 'products.txt'  # Инкапсулированный атрибут
    def get_products(self):
        """Метод, который считывает всю информацию из файла __file_name,
        закрывает его и возвращает единую строку со всеми товарами из файла __file_name."""

        file = open(self.__file_name, 'r') # открытие файла в режиме чтения и присваивание переменной "file"
        file_contents = file.read() # присваивание содержимого файла в переменную "file_contents"
        file.close() # закрытие файла
        # pprint(r)
        return file_contents # возвращает переменную "file_contents"

    def add(self, *products):
        """Метод, который принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' """

        file_get = self.get_products()
        for i in products:
                if file_get.find(f'{i.name}') == -1:
                    file = open(self.__file_name, 'a')
                    file.write(f'{i}\n')
                    file.close()
                else:
                    print(f'Продукт {i} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())