class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category},'


class Shop:
    __file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    def add(self, *products):
        with open(self.__file_name, 'a+') as file:
            file.seek(0)
            content_1 = file.readlines()
            for product in products:
                product_str = str(product) + '\n'
                if product_str not in content_1:
                    file.write(str(product_str))
                else:
                    print(f'Продукт {product} уже есть в магазине')






s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())