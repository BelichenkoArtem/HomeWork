from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

#def get_advanced_writer(file_name):
#        def write_everything(*data_set):
#            with open(file_name, 'a', encoding='utf-8') as file:
#                file.writelines(str(line) + '\n' for line in data_set)
#        return write_everything


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                existing_lines = {line.strip() for line in file}
        except FileNotFoundError:
            existing_lines = {}

        with open(file_name, 'a', encoding='utf-8') as file:
            for line_to_add in data_set:
                if str(line_to_add) not in existing_lines:
                    file.write(line_to_add + '\n')
                    existing_lines.add(line_to_add)
                else:
                    print(f'Строка {line_to_add} уже есть в файле.')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())