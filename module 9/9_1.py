def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        try:
            result = function(int_list)
        except Exception as e:
            result = f'Ошибка при применении {function.__name__}: {e}' # Обработка ошибок
        results[function.__name__] = result
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([1, 2, 'a'], sum))  # Пример с некорректным типом в списке
print(apply_all_func([], sum)) # Пример с пустым списком

