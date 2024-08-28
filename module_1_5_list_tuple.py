immutable_var = 1, ['a',1,3], True
print(immutable_var)
print(immutable_var[1])
#immutable_var[0] = a Элемент строка является неизменяемым типом данных
immutable_var[1][0] = 'A'
print(immutable_var)
mutable_var = [1,False, 'Art']
print(mutable_var)
mutable_var[0] = 'a'
print(mutable_var)
mutable_var.append(5)
print(mutable_var)
mutable_var.extend(immutable_var)
print(mutable_var)
mutable_var.remove(1)
print(mutable_var)

