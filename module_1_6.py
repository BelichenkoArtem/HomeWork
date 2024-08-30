my_dict = {'Artem' : 2001, 'Grisha' : 2002, 'Ilya' : 2008}
print(my_dict)
print(my_dict['Artem'])
print(my_dict.get('Uliana'))
my_dict.update({'Uliana' : 2002, 'Olya' : 2001})
print(my_dict.pop('Artem'))
print(my_dict)

my_set = {1.2, 1, 1, 2, True, True, 'Alex'}
print(my_set)
my_set.update([10, 20])
print(my_set)
my_set.discard(1)
print(my_set)