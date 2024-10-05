immutable_var = (0,'str',True)
print(immutable_var)
#immutable_var[0] = 5 #т.к. "tuple" являеться неизменяемым типом данных, то соответсвенно мы не можем изменить значение какого-либо элемента после создания переменной типа tuple.

mutable_list = [1,"string",False]
print(mutable_list)
mutable_list[0]='777'
mutable_list[1]=True
mutable_list[2]=777
print(mutable_list)
