def apply_to_list(data, func):
    try:
        return func(data)
    except TypeError:
        return None
    
def apply_to_each(data, func):
    try:
        return list(map(func, data))
    except TypeError:
        return None

def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        try:
            result = apply_to_list(int_list, function)
            if result is None:
                result = apply_to_each(int_list, function)
        except Exception as e:
            result = f'Ошибка при применении {function.__name__}: {e}'
        results[function.__name__ ] = result
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))