def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])

    if str_number.endswith('0'):
        str_number = str_number.rstrip('0')

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result1 = get_multiplied_digits(402030)
print(result1)
result2 = get_multiplied_digits(40203)
print(result2)
result3 = get_multiplied_digits(0)
print(result3)
