def get_multiplied_digits(number):
    str_number = str(number)
    while str_number and str_number[-1] == '0':
        str_number = str_number[:-1]
    list_number = list(str_number)
    first = list_number[0]
    if len(list_number) == 1:
        return int(first)
    else:
        return int(first) * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(4020)
print(result)
