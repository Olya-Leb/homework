from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name) # название продукта (строка)
        self.weight = float(weight) # общий вес товара (дробное число) (5.4, 52.8 и т.п.)
        self.category = str(category) # категория товара (строка)

    def __str__(self): # возвращает строку в формате '<название>, <вес>, <категория>
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        file_contents = file.read()
        file.close()
        # pprint(r)
        return file_contents

    def add(self, *products):
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