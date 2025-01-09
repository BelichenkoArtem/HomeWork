import  os, time

for dirpath, dirnames, filenames in  os.walk('.'):
    #print(dirpath)
    #print(dirnames)
    #print(filenames)
    for file in filenames:
        filepath = os.path.join(r'D:\Homework for Urban\pythonProject\Module_7\7_5_file_in_os', file)
        #print(filepath)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, \nВремя изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')



