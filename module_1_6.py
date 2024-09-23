my_dict = {'Olya' : 2001, 'Vitaly' : 2000, 'Polina' : 1962, 'Sveta' : 1999}
print(my_dict)
print(my_dict['Olya'])
print(my_dict.get('Max','Не существует'))
my_dict['Alena'] = 1999
my_dict['Den'] = 1999
print(my_dict)
my_dict.pop('Alena')
print(my_dict)
my_set = {1,1,2,2,'str','str',4,4,False,True,False,True}
print(my_set)
my_set.add('Sasha'), my_set.add('Masha')
print(my_set)
my_set.discard(False)
print(my_set)
