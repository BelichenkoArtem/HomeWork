def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    #if isinstance(numbers, str):
    #    mod_numbers = numbers.split(',')
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
    return incorrect_data, result

def calculate_average(numbers):
    try:
        #if isinstance(numbers, str):
        #    numbers = [x.strip() for x in numbers.split(',')]
        incorrect_data, summ = personal_sum(numbers)

        return summ / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0
    except TypeError as e:
        print(f'В numbers записан некорректный тип данных')



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать