def test_funcrion():
    def inner_function():
        print(f'Я в области видимости функции test_function')
    inner_function()

#test_funcrion()
inner_function()
#Код не будет работать при вызове функции inner_function вне функции test_function,
# так как локальные функции не видны за пределами их области видимости.