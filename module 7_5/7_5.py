import  os, time

for dirpath, dirnames, filenames in  os.walk('.'):
    #print(dirpath)
    #print(dirnames)
    #print(filenames)
    for file in filenames:
        filepath = os.path.join(dirpath, file)
        #print(filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, \nВремя изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')