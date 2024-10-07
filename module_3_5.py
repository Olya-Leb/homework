def get_multiplied_digits(number):
    str_number = str(number)
    new_str_number = str_number.rstrip('0')
    first = int(new_str_number[0])
    if len(new_str_number) > 1:
        return first * get_multiplied_digits(int(new_str_number[1:]))
    else:
        return first

result1 = get_multiplied_digits(402030)
print(result1)
result2 = get_multiplied_digits(40203)
print(result2)
