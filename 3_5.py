def get_multiplied_digits(number):
    #print(type(number))
    str_number = str(number)
    list_number = list(str_number)
    first = list_number[0]
    if len(list_number) == 0:
        return 0
    elif len(list_number) == 1:
        return int(first)
    else:
        return int(first) * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)